#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/2/7
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import time
import hashlib
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63',
    'Referer': 'https://ggzyjd.fj.gov.cn/web/index.html',
    'Content-Type': 'application/json;charset=UTF-8',
    'portal-sign': '',
}


def sort(dic):
    dic_keys = list(dic.keys())
    # print(dic_keys)
    sorted_dic = {}
    lower_sorted_keys = sorted([i.lower() for i in dic.keys()])
    # print(lower_sorted_keys)
    for i in lower_sorted_keys:
        for j in dic_keys:
            if i == j.lower():
                if dic[j] != '':
                    sorted_dic[j] = dic[j]
    # print(sorted_dic)
    return sorted_dic


def get_sign(dic):
    dic = sort(dic)
    str_ = "".join([key + f'{value}' if isinstance(value, list) else key + str(value) for key, value in dic.items()])
    # print(str_)
    text = 'E9498112A6CD42E0A4B2939CEBBC94CB' + str_
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()


def add_to_16(data):
    # 如果text不足16位的倍数就用空格补足为16位
    if len(data.encode('utf-8')) % 16:
        add = 16 - (len(data.encode('utf-8')) % 16)
    else:
        add = 0
    text = data + '\0' * add
    return text.encode('utf-8')


def pkcs7padding(text):
    """
    明文使用PKCS7填充
    最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
    """
    bs = AES.block_size  # 16
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    # tips：utf-8编码时，英文占1个byte，而中文占3个byte
    padding_size = length if (bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
    padding_text = chr(padding) * padding
    return text + padding_text


def pkcs7unpadding(text):
    """
    处理使用PKCS7填充过的数据
    """
    length = len(text)
    unpadding = ord(text[length - 1])
    return text[0:length - unpadding]


def decrypt(data):
    key = '79D819C6BB98D55CBCD62CB5CA435B42'.encode('utf8')
    iv = '82A6AB682F393347'.encode('utf-8')
    mode = AES.MODE_CBC
    cipher = AES.new(key, mode, iv)
    # data = add_to_16(data)
    base64_str = base64.b64decode(data)
    decrypt_data = cipher.decrypt(base64_str)
    result = str(decrypt_data, encoding='utf-8')
    result = pkcs7unpadding(result)
    print(result)
    return result


timestamp = int(float(time.time() * 1000))
# url = 'https://ggzyjd.fj.gov.cn/Article/PageList'
# payload = {
#     'IS_IMPORT': 1,
#     'pageSize': 3,
#     'ptype': 'jd',
#     'ts': timestamp,
#     'type': 1073
# }
url = 'https://ggzyjd.fj.gov.cn/Project/JdPortalProjectTypeTree'
payload = {
    'BeginTime': '2020-08-07 00:00:00',
    'EndTime': '2021-02-07 23:59:59',
    'PLATFORM_CODE': '',
    'PROJECT_CATEGORY': 1,
    'PROJECT_TYPE': '',
    'createTime': [],
    'timeType': '7',
    'ts': timestamp,
}
headers['portal-sign'] = get_sign(payload)
resp = requests.post(url, json=payload, headers=headers)
data = decrypt(resp.json()['Data'])
print(data)
