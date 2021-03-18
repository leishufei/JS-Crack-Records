#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/8
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import execjs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45',
    'Referer': 'https://star.toutiao.com/ad/author/douyin/6774914600774139912',
    # 必须要登录
    'Cookie': ''
}
with open(r'encrypt.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())


def sort_dict(item):
    sorted_key_list = sorted([key for key in item.keys() if key != 'sign'])
    ordered_item = {}
    for key in sorted_key_list:
        ordered_item[key] = key if item[key] == 'true' else item[key]
    # print(ordered_item)
    return ordered_item


def get_sign(item):
    ordered_item = sort_dict(item)
    str_ = ''.join([key + value for key, value in ordered_item.items()])
    # print(str_)
    sign = ctx.call('getSign', str_)
    # print(sign)
    return sign


params = {
    'author_id': '6774914600774139912',
    'num': '10',
    'without_emoji': 'true',
    'service_name': 'data.AdStarDataService',
    'service_method': 'GetAuthorHotCommentTokens',
    'sign': '',
}
sign = get_sign(params)
params['sign'] = sign
# 获取词云图内容
url = 'https://star.toutiao.com/h/api/gateway/handler_get/'
resp = requests.get(url, params=params, headers=headers)
print(resp.text)
