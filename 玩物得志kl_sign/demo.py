#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/2/5
# @Author   : Shufei Lei
# @Software : PyCharm
import hmac
import math
import random
import time
from hashlib import sha256, md5

import requests
from loguru import logger

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-length": "39",
    "content-type": "application/json",
    "kl_device_id": "a29f1210-f0db-11eb-9b5e-f573c88cf216",
    "kl_display_type": "2",
    "kl_os_type": "3",
    "kl_os_version": "1.0.0",
    "kl_platform": "3",
    "kl_sdk_ver": "1.0.3",
    "kl_sign": "",
    "kl_sign_ver": "1.0.0",
    "kl_t": "",
    "kl_trace_id": "",
    "kl_ver": "4.2.3",
    "origin": "https://h5.wanwudezhi.com",
    "pragma": "no-cache",
    "referer": "https://h5.wanwudezhi.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76"
}
CONFIG = {
    'ALGORITHM': "WWDZ-HMAC-SHA256",
    'AUTHORIZATIONHEADER_ALGORITHM': "Algorithm",
    'AUTHORIZATIONHEADER_CREDENTIAL': "Credential",
    'AUTHORIZATIONHEADER_SIGNATURE': "Signature",
    'AUTHORIZATIONHEADER_SIGNEDHEADERS': "SignedHeaders",
    'SIGNEDHEADERSAUTHORIZATION': "Authorization",
    'SIGNEDHEADERSPARAMS': "Signed-Headers",
    'SIGNEDPARAM_APIPATH': "apiPath",
    'SIGNEDPARAM_APPVERSION': "appVersion",
    'SIGNEDPARAM_DEVICETOKEN': "deviceToken",
    'SIGNEDPARAM_END': "wwdz_request",
    'SIGNEDPARAM_METHOD': "method",
    'SIGNEDPARAM_PAYLOAD': "payload",
    'SIGNEDPARAM_SID': "sId",
    'SIGNEDPARAM_SIGNVERSION': "signVersion",
    'SIGNEDPARAM_TIMESTAMP': "denifednumestamp",
    'SIGNSALT': "e680d60e7e6bd5931cb46d30c91d6d0d",
    'SIGNSECRETKEY': "bbcc71f7b26a82ea97196366558a8ef0"
}
BASE_UUID = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'


def gen_uuid():
    t = int(time.time() * 1000)
    uuid = ''
    for i in BASE_UUID:
        r = int((t + 16 * random.random()) % 16) | 0
        t = math.floor(t / 16)
        if i == 'x':
            uuid += format(r, 'x')
        elif i == '4' or i == '-':
            uuid += i
        else:
            uuid += format(3 & r | 8, 'x')
    logger.info(f'kl_trace_id: {uuid}')
    return uuid


def md5_encrypt(data):
    return md5(data.encode('utf8')).hexdigest()


def hmac_sha256_encrypt(key, data):
    return hmac.new(key.encode('utf8'), data.encode('utf8'), digestmod=sha256).hexdigest()


def get_kl_sign(arg1: dict, arg2: dict):
    data1 = {}
    data1.update(arg1)
    data1.update(arg2)
    logger.info(f'data1: {data1}')
    key = md5_encrypt(CONFIG['SIGNSECRETKEY'] + CONFIG['SIGNSALT'] + data1['signVersion'])
    payload = hmac_sha256_encrypt(key, data1['payload'])
    logger.info(f'payload: {payload}')
    data1.update({'payload': payload})
    data2 = '&'.join([key + '=' + str(data1[key]) for key in sorted(data1.keys())]).upper()
    logger.info(f'data2: {data2}')
    sign = hmac_sha256_encrypt(key, data2)
    logger.info(f'sign: {sign}')
    O = str(data1['timestamp']) + '_' + CONFIG['SIGNEDPARAM_END']
    kl_sign = CONFIG['AUTHORIZATIONHEADER_ALGORITHM'] + '=' + CONFIG['ALGORITHM'] + '/' + \
              CONFIG['AUTHORIZATIONHEADER_SIGNEDHEADERS'] + '=' + 'kl_path;kl_trace_id;kl_device_id' + \
              '/' + CONFIG['AUTHORIZATIONHEADER_CREDENTIAL'] + '=' + O + '/' + CONFIG['AUTHORIZATIONHEADER_SIGNATURE'] + \
              '=' + sign
    logger.info(f'kl_sign: {kl_sign}')
    return kl_sign


kl_trace_id = gen_uuid()
kl_t = int(time.time())
data1 = {
    'kl_path': '/activitysearch/bashuhome/all',
    'kl_trace_id': kl_trace_id,
    'kl_device_id': 'a29f1210-f0db-11eb-9b5e-f573c88cf216',
}
data2 = {
    "sId": "300100",
    "timestamp": kl_t,
    "appVersion": "4.2.3",
    "signVersion": "1.0.0",
    "payload": '{"pageIndex":3,"pageSize":20}'
}
kl_sign = get_kl_sign(data1, data2)
headers.update({'kl_trace_id': kl_trace_id, 'kl_sign': kl_sign, 'kl_t': str(kl_t)})

payload = {
    'kl_data': data2['payload']
}
POST_URL = 'https://kunlun.wanwudezhi.com/activitysearch/bashuhome/all'
r = requests.post(url=POST_URL, json=payload, headers=headers)
logger.info(r.text)
