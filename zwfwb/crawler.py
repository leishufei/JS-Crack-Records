#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/2/22
# @Author   : Shufei Lei
# @Software : PyCharm
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import re
import base64

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74',
}


def get_encrypted_url(url):
    id_ = re.search(r'/(\d+)\.', url).group(1)
    key = 'qnbyzzwmdgghmcnm'
    mode = AES.MODE_ECB
    cipher = AES.new(key.encode('utf-8'), mode)
    encrypt_text = cipher.encrypt(pad(id_.encode('utf-8'), AES.block_size))
    encrypt_text = str(base64.encodebytes(encrypt_text), encoding='utf-8').strip()
    encrypt_text = encrypt_text.replace('=', '').replace('/', '^')
    new_url = re.sub(r'\d{4,}', encrypt_text, url)
    print(new_url)
    return new_url


url = 'http://ggzy.zwfwb.tj.gov.cn:80/jyxxzbjb/960290.jhtml'
get_encrypted_url(url)
