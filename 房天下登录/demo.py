#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/2/1
# @Author   : Shufei Lei
# @Software : PyCharm
import execjs
import requests


headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "316",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # "Cookie": "",
    "Host": "passport.fang.com",
    "Origin": "https://passport.fang.com",
    "Pragma": "no-cache",
    "Referer": "https://passport.fang.com/?backurl=https%3A%2F%2Fneijiang.fang.com%2F",
    "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Microsoft Edge\";v=\"97\", \"Chromium\";v=\"97\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76",
    "X-Requested-With": "XMLHttpRequest"
}
with open(r'./core.js', 'r', encoding='utf8') as f:
    ctx = execjs.compile(f.read())


LOGIN_URL = 'https://passport.fang.com/login.api'
form_data = {
    'uid': 'xxx',
    'pwd': ctx.call('encrypt_pwd', 'xxx'),
    'Service': 'soufun-passport-web',
    'AutoLogin': 1
}
r = requests.post(url=LOGIN_URL, data=form_data, headers=headers)
print(r.json())
