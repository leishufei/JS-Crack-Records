#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/21
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import execjs
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
    'Referer': 'https://www.qimao.com/shuku/a-a-a-a-a-a-a-click-1/',
    'Host': 'www.qimao.com'
}
with open(r'js_code.js', 'r', encoding="utf-8") as f:
    ctx1 = execjs.compile(f.read())


def get_acw_sc__v2(arg):
    acw_sc__v2 = ctx1.call('get_acw_sc__v2', arg)
    return acw_sc__v2


url = 'https://www.qimao.com/shuku/a-a-a-a-a-a-a-click-1/'
resp = requests.get(url, headers=headers, allow_redirects=False)
cookies = resp.cookies.get_dict()
print(cookies)
arg1 = re.search(r"var arg1='(.*?)';", resp.text).group(1)

acw_sc__v2 = get_acw_sc__v2(arg1)
cookies.update({'acw_sc__v2': acw_sc__v2})
print(cookies)

resp = requests.get(url, headers=headers, cookies=cookies)
print(resp.text)
