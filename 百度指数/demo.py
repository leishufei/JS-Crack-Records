#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/10
# @Author   : Shufei Lei
# @Software : PyCharm
from urllib.parse import quote

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
    'Referer': 'https://index.baidu.com/v2/main/index.html',
    'Host': 'index.baidu.com',
    # 需要带上 Cookie
    'Cookie': ''
}
session = requests.Session()
session.headers = headers


def decrypt(t, e):
    n = list(t)
    i = list(e)
    a = {}
    r = []
    n_length = len(n)
    for o in range(int(n_length / 2)):
        a[n[o]] = n[int(n_length / 2) + o]
    for s in range(len(e)):
        r.append(a[i[s]])
    result = ''.join(r)
    return result


def get_key(uniqid):
    url = 'https://index.baidu.com/Interface/ptbk?uniqid=' + uniqid
    resp = session.get(url)
    _json = resp.json()
    key = _json['data']
    return key


def get_data(keyword):
    url = f'https://index.baidu.com/api/SearchApi/index?area=0&word=[[%7B%22name%22:%22{quote(keyword)}%22,%22wordType%22:1%7D]]&days=30'
    resp = session.get(url)
    _json = resp.json()
    # print(_json)
    uniqid = _json['data']['uniqid']
    print(uniqid)
    key = get_key(uniqid=uniqid)
    print(key)
    data = _json['data']['userIndexes'][0]['all']['data']
    decrypted_data = decrypt(key, data)
    print(decrypted_data)


# # 测试
# key = 'R1lyuvNPjUH3bWJ-9058%+3746,2.1'
# data = 'JjUyU3JJPjy3juUl3jHl13Hy1b3H1JH3jj1b3Jjjjy3111H3HHbU3HPlU3yuP13yjJy3jJyJ3JjjHH3ujyy3Huul3HjPb3HlHP3HPJU3ubll3JjUPu3Jlyuy31bbj3uHUu3jub13H1lJ3Hlb13JyyJj3JJyyJ'
# decrypted_data = decrypt(key, data)
# print(decrypted_data)

keyword = '斗罗大陆'
get_data(keyword=keyword)
