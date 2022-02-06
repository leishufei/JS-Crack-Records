#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/1/28
# @Author   : Shufei Lei
# @Software : PyCharm
from loguru import logger
import random
import re
import time
from urllib.parse import quote

import execjs
import requests


class LagouSpider:
    def __init__(self):
        headers = {
            'Host': 'www.lagou.com',
            'referer': 'https://www.lagou.com/jobs/list_python?&cl=false&fromSearch=true&labelWords=&suginput=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        }
        self.session = requests.Session()
        self.session.headers = headers
        self.data = {
            'first': 'true',  # first=true代表从第一页开始
            'pn': '1',
            'kd': ''
        }

    @staticmethod
    def get_head_js(search):
        head_js = 'window = this;\nwindow.location = {' + '"search": "{}",'.format(search) + '"hostname": "www.lagou.com"};\n'
        return head_js

    @staticmethod
    def get_tail_js():
        tail_js = "function get_lg_stoken() {g = window.gt;return (new g()).a()}"
        return tail_js

    def get_name_and_location(self):
        keyword = quote(self.keyword)
        url = f'https://www.lagou.com/jobs/list_{keyword}?&cl=false&fromSearch=true&labelWords=&suginput='
        response = self.session.get(url, allow_redirects=False)
        location = response.headers['Location']
        logger.info(f'location: {location}')
        name = re.search(r'&name=(.*?)&', location).group(1)
        if name is not None:
            return name, location
        logger.info(response.headers)
        raise Exception('访问频繁')

    def init_cookie(self):
        name, location = self.get_name_and_location()
        search = '?' + location.split('?', 1)[1]
        logger.info(f'name: {name}')
        logger.info(f'location: {location}')
        logger.info(f'search: {search}')

        head_js = self.get_head_js(search)
        tail_js = self.get_tail_js()
        
        url = f'https://www.lagou.com/common-sec/dist/{name}.js'
        response = self.session.get(url)
        main_js = response.text
        js_code = head_js + main_js + tail_js
        with open('./js_code.js', 'w', encoding='utf8') as f:
            f.write(js_code)
        ctx = execjs.compile(js_code)
        lg_stoken = ctx.call('get_lg_stoken')
        logger.info(f'lg_stoken: {lg_stoken}')
        self.session.cookies.update({'__lg_stoken__': lg_stoken})

    def get_data(self, page):
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        if page > 1:
            self.data['first'] = 'false'
        self.data['pn'] = str(page)
        logger.info(self.session.headers['referer'])
        response = self.session.post(url, data=self.data)
        if response.status_code == 200:
            _json = response.json()
            logger.info(_json)
            results = _json['content']['positionResult']['result']
            for each in results:
                logger.info(each)

            self.data['sid'] = _json['content']['showId']

    def crawl(self, keyword, max_page):
        self.keyword = keyword
        self.data['kd'] = keyword
        self.init_cookie()
        for page in range(1, max_page + 1):
            self.get_data(page)
            time.sleep(random.randint(3, 5))


if __name__ == '__main__':
    keyword = 'python'
    pages = 100
    lg = LagouSpider()
    lg.crawl(keyword, pages)
