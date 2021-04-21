#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/21
# @Author   : Shufei Lei
# @Software : PyCharm
import hashlib
import time

import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'Referer': 'https://servicewechat.com/wx5bfb6b535af31da3/2/page-frame.html',
    'Host': 'm.toutiao.com',
    'Content-Type': 'application/json',
    'X-Traffic-Type': 'wxapp'
}


def ascp():
    now_time = int(time.time())
    t_hex = hex(now_time).upper()[2:]
    t_md5 = hashlib.md5(str(now_time).encode('utf-8')).hexdigest().upper()
    pre = t_md5[:5]
    last = t_md5[-5:]
    as_cy = ''
    for i in range(5):
        as_cy += pre[i] + t_hex[i]
    cp_cy = ''
    for i in range(5):
        cp_cy += t_hex[i + 3] + last[i]
    return {
        'as': "A1" + as_cy + t_hex[-3:],
        'cp': t_hex[:3] + cp_cy + "E1"
    }


url = 'https://m.toutiao.com/list/wxapp/'
ASCP = ascp()
params = {
    'ac': 'wap',
    'aid': '1162',
    'as': ASCP['as'],
    'count': '20',
    'cp': ASCP['cp'],
    'enable_stick': '',
    'format': 'json_raw',
    'max_behot_time': '1618977893',
    'tag': 'news_entertainment'
}
resp = requests.get(url, params=params, headers=headers, verify=False)
print(resp.text)
