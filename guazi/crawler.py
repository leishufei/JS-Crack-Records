#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/2/1
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import execjs
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53',
    'Cookie': ''
}
with open(r'encrypt.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())


url = 'https://www.guazi.com/bj/1ee803b7c1c8263cx.htm#fr_page=list&fr_pos=city&fr_no=0'
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
html = response.text
# print(html)

string, key = re.findall(r"var value=anti\('(.*?)','(.*?)'\);var name", html, re.S)[0]
cookie = ctx.call('getCookie', string, key)
headers['Cookie'] = cookie

response2 = requests.get(url, headers=headers)
response2.encoding = 'utf-8'
html2 = response2.text
print(html2)
