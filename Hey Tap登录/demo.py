#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/13
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import json
import base64
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
    'Content-Type': 'application/encrypted-json;charset=UTF-8',
    'X-BusinessSystem': 'HeyTap',
    'X-From-HT': 'true',
    'X-Key': 'PT7pPFLPdjt4FqoiDjOHyX7RHfZ1sHt37so1N2UnmAMGJ/cnxuxRV8LjZT8raBNZY2W+7dL88YiPaem2xA1Eygpup9HvkKWXMNBQFIAn4oNUDsyp8LijotqD26xx48Y69z16YKkB6BTEmBYZdIk4YsNqIiL2GGmXiMqgYBkoITo=',
    'X-Protocol-Version': '1.0',
    'X-Session-Ticket': 'g7exNanKzd+Vi8POwNfGaGYMSs6pEi4c341Fz3ANiKw=',
    'X-Timezone': 'GMT+8'
}


def _md5(data):
    return hashlib.md5(data.encode()).hexdigest()


def _aes(data):
    key = "2pzYwr8Uhr8PPDvA"
    mode = AES.MODE_ECB
    cipher = AES.new(key.encode('utf-8'), mode)
    cipher_text = base64.b64encode(cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))).decode()
    return cipher_text


def get_sign(item):
    list_ = sorted([key + '=' + str(value) for key, value in item.items() if value != ''])
    data = '&'.join(list_) + '&key=FdjydGAAKasmht1nFnR4MS5itFeh4R1Lk'
    return _md5(data)


def get_body(username, password):
    timestamp = int(float(time.time()) * 1000)
    data = {
        "timestamp": timestamp,
        "nonce": timestamp,
        "appKey": "CuGsbe6HdAe6vDBHFew2Di",
        "accountType": "MOBILE",
        "loginName": username,
        "countryCallingCode": "+86",
        "password": _md5(password),
        "deviceId": "895040608968d28092308b9aa1f77c54",
        "captchaTicket": "",
        "callbackUrl": "https%3A%2F%2Fwww.heytap.com%2Fcn%2Fm%2Fucenter%2Findex",
        "processTicket": "",
        "agreeUpgrade": "false"
    }
    sign = get_sign(data)
    data['sign'] = sign
    encrypted_body = _aes(json.dumps(data).replace(' ', ''))
    print(encrypted_body)
    return encrypted_body


def login(username, password):
    body = get_body(username, password)
    login_url = 'https://id.heytap.com/api/login/v1/validate-password'
    resp = requests.post(login_url, data=body, headers=headers)
    print(resp.text)


username = '12345678901'
password = '123'
login(username, password)
