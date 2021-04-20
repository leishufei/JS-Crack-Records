#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/4/18
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import execjs
from bs4 import BeautifulSoup
import time
import openpyxl
import csv
import re
from traceback import print_exc
import os
import json
from retry import retry

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
    'Referer': 'http://www.shipxy.com/',
    'Host': 'www.shipxy.com',
    'Cookie': ''
}
with open(r'assets/encrypt.js', 'r', encoding="utf-8") as f:
    ctx = execjs.compile(f.read())


def decrypt(data):
    decrypted_data = ctx.call('decrypt', data)
    return decrypted_data


def get_track_list(ship_id, b_time, e_time):
    url = f'http://www.shipxy.com/Ship/GetTrack?shipid={ship_id}&btime={b_time}&etime={e_time}&limit=1&enc=0'
    resp = requests.get(url, headers=headers)
    _json = resp.json()
    track_list = decrypt(_json['data'])
    print(track_list)
    print(len(track_list))

ship_id = 413837367
begin_time = 1616169600
end_time = 1618804800
get_track_list(ship_id, begin_time, end_time)

