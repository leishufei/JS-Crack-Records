#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/2
# @Author   : Shufei Lei
# @Software : PyCharm
import requests
import execjs
import re
import hashlib
import random


UA_LIST = [
    'User-Agent,Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    'User-Agent,Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
    'User-Agent,Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
    'User-Agent,Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    'User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    'User-Agent,Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
]


headers = {
    'User-Agent': random.choice(UA_LIST),
}


def encrypt(value, mode):
    hash_value = eval(f'hashlib.{mode}(value.encode("utf-8")).hexdigest()')
    return hash_value


def get_item(url):
    # 第一次请求
    resp1 = session.get(url)
    gen_cookie_code = re.search(r'cookie=(.*?);location', resp1.text).group(1)
    first_cookie = execjs.eval(gen_cookie_code)
    session.cookies.update({first_cookie.split('=')[0]: first_cookie.split('=')[1]})
    # 第二次请求
    resp2 = session.get(url)
    item = eval(re.search(r'go\(({"bts":(.*?),"chars":".*?","ct":".*?","ha":".*?","tn":"__.*?","vt":".*?","wt":".*?"})\)', resp2.text).group(1))
    # print(item)
    return item


def get_cookie(url):
    item = get_item(url)
    ct = item['ct']
    bts = item['bts']
    chars = item['chars']
    tn = item['tn']
    hash_mode = item['ha']
    chars_length = len(chars)
    for i in range(chars_length):
        for j in range(chars_length):
            value = bts[0] + chars[i] + chars[j] + bts[1]
            if encrypt(value, hash_mode) == ct:
                # print('__jsl_clearance=' + value)
                return {tn: value}


def get_html(url):
    global session
    session = requests.Session()
    cookie = get_cookie(url)
    session.cookies.update(cookie)
    resp = session.get(url)
    html = resp.text
    print(html)


url = 'https://www.mps.gov.cn/n2253534/n2253535/index.html'
get_html(url)
