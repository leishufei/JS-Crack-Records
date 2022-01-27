#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/1/27
# @Author   : Shufei Lei
# @Software : PyCharm
import requests

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "cookie": "_zap=e6edd8e6-f72c-4a87-b50f-dbdef1edf219; _xsrf=84f9ebf6-7875-4931-8f46-befcdac5c40c; d_c0=\"ALDQODSHZhSPTpHFSuIP0qp7puKVHbZjuFw=|1643257930\"; ISSW=1; SESSIONID=NUSHmElV0znE9NM8YsYW7uR1rZ8PU698klkhJDuxHEi; KLBRSID=0a401b23e8a71b70de2f4b37f5b4e379|1643263280|1643257930",
    "pragma": "no-cache",
    "referer": "https://www.zhihu.com/search?type=content&q=%E7%90%86%E8%B4%A2",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "x-ab-param": "top_test_4_liguangyi=1;pf_noti_entry_num=0;qap_question_visitor= 0;pf_adjust=0;zr_slotpaidexp=1;se_ffzx_jushen1=0;qap_question_author=0;zr_expslotpaid=1;tp_topic_style=0;tp_contents=2;tp_zrec=0;tp_dingyue_video=0",
    "x-ab-pb": "CtYBDwuABaIDFQWMBdcCeQcRBaIGeAfaBD8GowfYB90HOwLpBDMEsgVXB+QKtADTB8IFKgONBEEGJwfsCjcMaQFPB08DfQI3BQsEmwv0A1ILAghWBX4GpgbrBlEF8wNSBYsFxgb6BnsHVAeJDKEDlAYbAD8AhAKeBbIH1wu3A2AL4AvPC0MAMgMWBrkHBwdyB9wLMgUwBmYHNAwBC/YCjAQpBQEGQAEzBdwHBwy1C9gCmwdqAXQB1gRWDEcAVwSrBncHtApQA6ADpgTjBecF9Au5AswCKgYxBhJrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAEBAAAAAAAAAgABAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAsYAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAEAAAAAAAAAAAAAAAsAAAA=",
    "x-api-version": "3.0.91",
    "x-app-za": "OS=Web",
    "x-requested-with": "fetch",
    "x-zse-93": '101_3_2.0',
    "x-zse-96": ""
}


def get_x_zse_96(data):
    r = requests.post(url='http://127.0.0.1:3002/get_signature', data={'data': data})
    x_zse_96 = r.text
    print('x_zse_96:', x_zse_96)
    return x_zse_96


QUERY_URL = 'https://www.zhihu.com/api/v4/search_v3?t=general&q=%E7%90%86%E8%B4%A2&correction=1&offset=40&limit=20&filter_fields=&lc_idx=40&show_all_topics=0&search_hash_id=1cdbd8f2d7403410fc239dac20f0c710&search_source=Normal&vertical_info=0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C1'
x_zse_96 = get_x_zse_96(QUERY_URL.replace('https://www.zhihu.com', ''))
headers['x-zse-96'] = x_zse_96
print(headers)
r = requests.get(url=QUERY_URL, headers=headers)
print(r.json())
