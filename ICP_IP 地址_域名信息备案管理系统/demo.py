#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/11
# @Author   : Shufei Lei
# @Software : PyCharm
import hashlib
import time

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
    "content-type": "application/x-www-form-urlencoded",
    'Referer': 'https://beian.miit.gov.cn/',
    'Host': 'hlwicpfwc.miit.gov.cn',
    'token': ''
}
session = requests.Session()
session.headers = headers


def _md5(data):
    encrypted_data = hashlib.md5(data.encode()).hexdigest()
    return encrypted_data


def get_token():
    timestamp = int(float(time.time()) * 1000)
    data = 'testtest' + str(timestamp)
    auth_key = _md5(data)
    print('auth_key:', auth_key)

    url = "https://hlwicpfwc.miit.gov.cn/icpproject_query/api/auth"
    form_data = {
        'authKey': auth_key,
        'timeStamp': timestamp
    }
    resp = session.post(url=url, data=form_data)
    print(resp.text)
    token = resp.json()['params']['bussiness']
    return token


def get_image():
    token = get_token()
    session.headers['token'] = token
    url = 'https://hlwicpfwc.miit.gov.cn/icpproject_query/api/image/getCheckImage'
    resp = session.post(url)
    print(resp.text)


# get_token()
get_image()
