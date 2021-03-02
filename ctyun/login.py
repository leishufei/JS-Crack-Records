#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/1/27
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import execjs
import time
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import base64


class CTYun(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.timestamp = int(float(time.time()) * 1000)
        self.login_url = 'https://m.ctyun.cn/account/login'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',
            'Referer': 'https://m.ctyun.cn/wap/main/auth/login?redirect=%2Fmy'
        }

    def get_encrypt_params(self):
        with open(r'encrypt.js', 'r', encoding='utf-8') as f:
            ctx = execjs.compile(f.read())
        params = ctx.call('M', self.timestamp)
        return params

    def encrypt_password(self):
        key = self.username
        if len(key) < 24:
            key += '0' * (24 - len(key))
        else:
            key = key[:24]
        crypto = DES3.new(key=key.encode(), mode=DES3.MODE_ECB)
        data = crypto.encrypt(pad(self.password.encode(), DES3.block_size))
        encrypt_password = base64.b64encode(data).decode()
        # print(encrypt_password)
        return encrypt_password

    def login(self):
        seq_code, signature = self.get_encrypt_params().split(';')
        params = {
            'userName': self.username,
            'password': self.encrypt_password(),
            'referrer': 'wap',
            'mainVersion': '300021100',
            'comParam_curTime': f'{self.timestamp}',
            'comParam_seqCode': seq_code,
            'comParam_signature': signature,
            'isCheck': 'true',
            'locale': 'zh-cn',
        }
        response = requests.get(self.login_url, params=params, headers=self.headers)
        print(response.text)


if __name__ == '__main__':
    username = ''
    password = ''
    ctyun = CTYun(username, password)
    ctyun.login()
