#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/2/22
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import hashlib
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74',
    'Referer': 'https://www.cls.cn/telegraph',
}


def _md5(data):
    return hashlib.md5(data.encode()).hexdigest()


def _sha1(data):
    return hashlib.sha1(data.encode()).hexdigest()


def get_sign(data):
    data = _sha1(data)
    data = _md5(data)
    return data


url = 'https://www.cls.cn/nodeapi/telegraphList'
timestamp = str(int(time.time()))
params = {
    'app': 'CailianpressWeb',
    'category': '',
    'lastTime': timestamp,
    'last_time': timestamp,
    'os': 'web',
    'refresh_type': 1,
    'rn': 20,
    'sv': '7.5.5',
    'sign': ''
}
data = f'app=CailianpressWeb&category=&lastTime={timestamp}&last_time={timestamp}&os=web&refresh_type=1&rn=20&sv=7.5.5'
# print(data)
params['sign'] = get_sign(data)
# print(params['sign'])
resp = requests.get(url, params=params, headers=headers)
print(resp.json())
