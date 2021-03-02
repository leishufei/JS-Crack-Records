#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/1
# @Author   : Shufei Lei
# @Software : PyCharm
import re

import requests
import execjs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81'
}
session = requests.Session()

# url = 'http://www.pbc.gov.cn/tiaofasi/144941/144957/index.html'
url = 'http://www.pbc.gov.cn/tiaofasi/144941/144957/4168458/index.html'
html = session.get(url).text
js_code = re.search(r'<script type="text/javascript">([\w\W]*)</script>', html, re.S).group(1).strip()
js_code = re.sub(r'atob\(', r'window.atob(', js_code)
func = 'function getRedirectUrl() { var window = {};\n' + js_code + '\nreturn window["location"];}'
ctx = execjs.compile(func)
redirect_url = 'http://www.pbc.gov.cn' + ctx.call('getRedirectUrl')
print(redirect_url)
resp = session.get(redirect_url)
resp.encoding = 'utf-8'
print(resp.text)
