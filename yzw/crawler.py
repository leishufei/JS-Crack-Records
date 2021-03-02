#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/2/8
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import json
import execjs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63',
    'Content-Type': 'application/json;charset=UTF-8'
}
with open(r'decrypt.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())


def decrypt(data):
    decrypt_data = ctx.call('decrypt', data)
    return decrypt_data


def query(url, data, request_type):
    if request_type == 'GET':
        resp = requests.get(url, params=data, headers=headers)
    else:
        resp = requests.post(url, data=json.dumps(data), headers=headers)
    print(decrypt(resp.json()['data']))


# 测试 1
# url = 'https://news.yaozh.com/api/Common/getadvlist'
# data = {
#     'id': '24'
# }
# 测试 2
# url = 'https://news.yaozh.com/api/Archive/getarchivelist'
# data = {
#     'id': '24',
#     'has_cateid': '',
#     'uid': ''
# }
# 测试 3
url = 'https://news.yaozh.com/api/Common/getsearcharticle'
data = {
    'user_id': '',
    'search_name': '',
    'page': 1,
    'limits': 10,
    'is_index': 0,
    'navid': 24,
    'has_cateid': '',
    'artid': '',
    'uid': ''
}
query(url, data, 'GET')
