#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : %s
# @Author   : Shufei Lei
# @Software : PyCharm
import execjs
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'https://www.qcc.com/web/search?key=%E5%8C%BA%E5%9D%97%E9%93%BE&p=7',
    'Cookie': 'zg_did=%7B%22did%22%3A%20%22178b4cf2c259ec-0c5ad9531c369c-7166786d-144000-178b4cf2c26c6d%22%7D; QCCSESSID=9epdmh6vbb4mnj2lpikfdkkm12; acw_tc=701cc88f16231506136601303ee82f7e9a87a32fb56e413a590e161c2e; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201623151533692%2C%22updated%22%3A%201623151615614%2C%22info%22%3A%201623047951859%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E4%BC%81%E6%9F%A5%E6%9F%A5%E7%BD%91%E7%AB%99%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%2C%22cuid%22%3A%20%22e6cbc023fac9641bc60d4200ef0724a5%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%7D'
}
with open(r'encrypt.js', 'r', encoding="utf-8") as f:
    ctx = execjs.compile(f.read())


def get_headers_param(url, data):
    url = url.replace("https://www.qcc.com", '')
    return ctx.call('getHeadersParam', url, data)


url = 'https://www.qcc.com/api/search/searchMulti'
payload = {"searchKey": "区块链", "pageIndex": 1, "pageSize": 20}
headers_param = get_headers_param(url, payload)
print(headers_param)
headers.update(headers_param)
resp = requests.post(url, json=payload, headers=headers)
print(resp.text)
