#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/2/5
# @Author   : Shufei Lei
# @Software : PyCharm
import execjs
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56'
}
with open(r'encrypt.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())


def encrypt(data):
    encrypt_data = ctx.call('encrypt', data)
    return encrypt_data


def decrypt(data):
    decrypt_data = ctx.call('decrypt', data)
    return decrypt_data


def query(url, data):
    resp = requests.post(url, data=data, headers=headers)
    print(decrypt(resp.text))


t = '{}'
url = 'https://www.macau-slot.com/API_SEV/cn/D/FB/coming/all/-/threeinone/-'
post_data = {
    'request_data': encrypt(t),
    'token': ''
}

query(url, post_data)
