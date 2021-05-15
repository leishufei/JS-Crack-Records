#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/15
# @Author   : Shufei Lei
# @Software : PyCharm
import hashlib

import execjs
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
    'Referer': 'https://www.zhihu.com/question/32762402',
    'x-ab-param': 'qap_question_author=0;zr_expslotpaid=1;li_sp_mqbk=0;pf_adjust=0;qap_question_visitor= 0;se_ffzx_jushen1=0;pf_noti_entry_num=0;zr_slotpaidexp=1;tp_contents=2;top_test_4_liguangyi=1;tp_topic_style=0;tp_dingyue_video=0;li_panswer_topic=0;li_paid_answer_exp=0;tp_zrec=0;li_vip_verti_search=0;li_edu_page=old',
    'x-ab-pb': 'Cnp0AcICUguJDBsAhAKxAsACNwxPAQ8LNAxYAX0CnwLXAgoCxwJrAYgBYAu0AMECKgI/ALcARwA7AokCaQGMAtoCzwtnANkC1wu7ApsLbQIHDPQLTAu/AmoBygJWDOwKQwC0CkUC4AvcC+QKzALYArkCQAEBC7ULjQGmARI9AAABAAAAAAABAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAALAAAAAAIAAAAAAAAAAQEYAAAAAAAAAAsAAAMAAA==',
    'x-app-version': '6.42.0',
    'x-zse-83': '3_2.0',
    'x-zse-86': '2.0_a0FqFJe0gG2fbLt0hqYqb6e8c8FXghNB8TF8kAUBQ_2x',
    'x-zst-81': '3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTcMtuQ_F0K6P0EQuy-LS9-hp1DufI-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_Ie8FL7AtqM6O1VDQyQ6nxrRPCHukMoCXBEgOsiRP0XL2ZUBXmDDV9qhnyTXFMnXcTF_ntRueThXgf19L82DHYwgOMbhp1c4pGUqx80UYqR9eq3U9BfBOsSbeY0hC_Dwe8AwOPvLe01TC8r7o0FDO1tqgfsvx0zJoGQ9VmLBVK7DOfWu3LqUSuUDe1D9pMwCxC6CCBU9eBTwHLXho9Q9HxbR2qFhgqSqU0JugBhBg0JvwMphO00JO1LqV04qfzwh30YqcxYqt0lqL_DuOGD92V9UtMHCLLEqcfaGSs19wyPcfLxvS_iuV_qwCq5bL8kJ38tUNm8cXmRutKQ7efYgpVJT2YcrefAUr9rQS9TCtY-wLLWJrC',
}
with open(r'encrypt.js', 'r', encoding="utf-8") as f:
    ctx = execjs.compile(f.read())


def _md5(data):
    return hashlib.md5(data.encode()).hexdigest()


def get_x_zse_86(u):
    # x-zse-83、dc0、x-zst-81、dc0参数都是固定的，可以直接抓包拿到
    # dc0 来自 cookie 中的 d_c0 字段
    x_zse_83 = headers['x-zse-83']
    dc0 = '"AKDdA4NK_xKPTlpLqYEKH7icXnZjxYKrim8=|1619149938"'
    x_zst_81 = headers['x-zst-81']
    d = '+'.join([x_zse_83, u, dc0, x_zst_81])
    x_zse_86 = ctx.call('b', _md5(d))
    return x_zse_86


offset = 0
u = f'/api/v4/answers/58707616/root_comments?order=normal&limit=10&offset={offset}&status=open'
x_zse_86 = get_x_zse_86(u)
print('x_zse_86:' + x_zse_86)
headers['x-zse-86'] = x_zse_86
url = 'https://www.zhihu.com' + u
resp = requests.get(url=url, headers=headers)
print(resp.text)
