#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/2/3
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import hashlib
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56',
    'Referer': 'http://lib.xcz.im/',
    'Content-Type': 'application/json;charset=UTF-8',
    'x-lc-id': '9pq709je4y36ubi10xphdpovula77enqrz27idozgry7x644',
    'x-lc-prod': '0',
    'x-lc-sign': '',
    'x-lc-ua': 'LeanCloud-JS-SDK/3.15.0 (Browser)'
}


def md5_encrypt(md5_str):
    md5 = hashlib.md5()
    md5.update(md5_str.encode('utf-8'))
    return md5.hexdigest()


def get_sign(timestamp):
    x_lc_sign = '364g5iu6q1f3hhwz8wruvmayu3vsap995wh4ws7tszor43np'
    data = timestamp + x_lc_sign
    sign = md5_encrypt(data)
    return sign


def query():
    url = 'https://avoscloud.com/1.1/call/getHotAuthors'
    payload = {}

    timestamp = str(int(float(time.time() * 1000)))
    sign = get_sign(timestamp)
    headers['x-lc-sign'] = sign + ',' + timestamp
    resp = requests.post(url, json=payload, headers=headers)
    print(resp.text)


if __name__ == "__main__":
    query()
