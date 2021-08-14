#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/8/14
# @Author   : Shufei Lei
# @Software : PyCharm
import base64
import binascii
import json
import random

import requests
from Crypto.Cipher import AES

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
    "Referer": "https://music.163.com/",
    "Content-Type": "application/x-www-form-urlencoded"
}

public_key = "010001"
modulus = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
origin_key = "0CoJUm6Qyw8W8jud"
iv = "0102030405060708"


def get_random_str(n):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_str = ""
    for i in range(n):
        index = random.randint(0, len(chars) - 1)
        random_str += chars[index]
    return random_str


def AES_encrypt(data, key, iv):
    mode = AES.MODE_CBC

    pad = 16 - len(data) % 16
    if isinstance(data, str):
        data = data + pad * chr(pad)
    else:
        data = data.deocde("utf-8") + pad * chr(pad)

    cipher = AES.new(key.encode("utf-8"), mode, iv.encode("utf-8"))
    encrypted_data = cipher.encrypt(data.encode("utf-8"))
    encrypted_data = base64.b64encode(encrypted_data).decode("utf-8")
    return encrypted_data


def RSA_encrypt(data):
    data = data[::-1]
    rsa = int(binascii.hexlify(data.encode("utf-8")), 16) ** int(public_key, 16) % int(modulus, 16)
    return format(rsa, "x").zfill(256)


def get_encText(data, random_str):
    encText1 = AES_encrypt(data, origin_key, iv)
    encText2 = AES_encrypt(encText1, random_str, iv)
    return encText2


def get_encSecKey(random_str):
    encSecKey = RSA_encrypt(random_str)
    return encSecKey


def main():
    page = 1
    csrf_token = ""
    cursor = ""  # 上一个请求结果中的 cursor
    data = {
        "rid": "R_SO_4_427542189",
        "threadId": "R_SO_4_427542189",
        "pageNo": page,
        "pageSize": "20",
        "cursor": cursor,
        "offset": "40",  # 这个是固定值，并不是偏移量
        "orderType": "1",
        "csrf_token": csrf_token
    }
    random_str = get_random_str(16)
    encText = get_encText(json.dumps(data).replace(" ", ""), random_str)
    print(f"encText: {encText}")
    encSecKey = get_encSecKey(random_str)
    print(f"encSecKey: {encSecKey}")

    url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token=" + csrf_token
    form_data = {
        "params": encText,
        "encSecKey": encSecKey
    }
    resp = requests.post(url, data=form_data, headers=headers)
    print(resp.text)


main()
