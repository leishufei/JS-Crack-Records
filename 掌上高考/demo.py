#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/9
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import execjs


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75',
    'Host': 'api.eol.cn',
    'Content-Type': 'application/json;charset=UTF-8'
}
with open(r'js.js', 'r', encoding="utf-8") as f:
    ctx = execjs.compile(f.read())


def get_signsafe(param):
    print(param)
    signsafe = ctx.call('getSignsafe', param)
    return signsafe


def decrypt(text):
    decrypted_data = ctx.call('decrypt', text)
    return decrypted_data


url = 'https://api.eol.cn/gkcx/api/'
params = {
    'access_token': '',
    'local_province_id': 12,
    'local_type_id': 3,
    'page': 1,
    'school_id': 35,
    'signsafe': '',
    'size': 10,
    'uri': 'apidata/api/gk/score/province',
    'year': ''
}
param = f'api.eol.cn/gkcx/api/?local_province_id={params["local_province_id"]}&local_type_id={params["local_type_id"]}&' \
        f'page={params["page"]}&school_id={params["school_id"]}&size={params["size"]}&uri={params["uri"]}&year={params["year"]}'
signsafe = get_signsafe(param)
print(signsafe)
params.update({'signsafe': signsafe})
payload = params

resp = requests.post(url, json=payload, headers=headers)
# print(resp.text)

text = resp.json()['data']['text']
decrypted_data = decrypt(text)
print(decrypted_data)
