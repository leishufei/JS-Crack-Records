#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/2/7
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import json
import time
import execjs


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63',
    'Referer': 'https://share.wcsz.top/',
    'Content-Type': 'application/json;charset=UTF-8'
}
with open(r'js1.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())


def get_params(phone_number):
    sign, time_ = ctx.call('getSign', phone_number, '86')
    return sign, time_


timestamp = int(float(time.time()) * 1000)
url = 'https://api.wcsz.top/go/user/phone/sendMsg'
phone_number = '15512345678'
payload = {
    'countryCode': '86',
    'phoneNo': phone_number,
    'sign': get_params(phone_number)[0],
    'time': get_params(phone_number)[1]
}
resp = requests.post(url, data=json.dumps(payload), headers=headers)
print(resp.text)