#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/13
# @Author   : Shufei Lei
# @Software : PyCharm
import execjs
import requests

headers = {
    'Referer': 'https://www.qimai.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
with open(r'encrypt.js', 'r', encoding="utf-8") as f:
    ctx = execjs.compile(f.read())


def get_analysis(url, params):
    analysis = ctx.call('getAnalysis', url, params)
    print('Analysis:', analysis)
    return analysis


base_url = 'https://api.qimai.cn'
path = '/andapp/appinfo'
params = {
    'market': 100,
    'appid': 5388170
}
analysis = get_analysis(path, params)
params.update({'analysis': analysis})
url = base_url + path
resp = requests.get(url, params=params, headers=headers)
print(resp.text)
