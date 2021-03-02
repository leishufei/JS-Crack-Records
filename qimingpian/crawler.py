#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/1/26
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import execjs


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',
    'Cookie': 'gw_unionid=QnJgn52eSILNz7+YZviUfGxGE9Sp7QCiq9voVFQMIVa7nBXWFTNgrj6YjukGRD2AeJWqqIs6kiQsM8IbOYgM5A=='
}
union_id = headers['Cookie'].split('=')[1]
with open(r'decrypt.js', 'r', encoding='utf-8') as f:
    js = f.read()
ctx = execjs.compile(js)


def decrypt(data):
    decrypted_data = ctx.call('o', data)
    return decrypted_data


def get_json_data(url, data):
    try:
        response = requests.post(url, data=data, headers=headers)
        return response.json()
    except:
        return {}


def get_product_info():
    url = 'https://vipapi.qimingpian.com/ProductDetail/productInfo'
    data = {
        'ticket': '5d728467c5d955f68bd21dfccc62c970',
        'unionid': union_id
    }
    json = get_json_data(url, data)
    # print(json)
    encrypt_data = json['encrypt_data']
    decrypt_data = decrypt(encrypt_data)
    print(decrypt_data)


get_product_info()
