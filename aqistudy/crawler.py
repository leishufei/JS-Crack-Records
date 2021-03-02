#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/1
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import execjs


with open(r'encrypt.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81'
}
url = 'https://www.aqistudy.cn/historydata/api/historyapi.php'
# 测试 1
# method = 'GETMONTHDATA'
# city = '天津'
# 测试 2
method = 'GETDAYDATA'
city = '北京'
month = '201401'
form_data = {
    'hmebd5PRa': ctx.call('getParam', method, city, month)
}
resp = requests.post(url, data=form_data, headers=headers)
data = ctx.call('getData', resp.text)
print(data)
