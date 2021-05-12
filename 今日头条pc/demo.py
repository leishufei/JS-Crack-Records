#!usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/5/12
# @Author   : Shufei Lei
# @Software : PyCharm
import execjs
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
    'Referer': 'https://www.toutiao.com/?wid=1620098370866',
    'Cookie': 'tt_webid=6958269494939895326; csrftoken=6391a1325f841d6bfa9d26183d103c8a; ttcid=36df49b6234144e7827bd209044a2c0e33; s_v_web_id=verify_ko9gqomm_A8RiZIKz_3KNr_42OZ_A1XP_KGFayXnoah7R; _S_DPR=1.25; _S_IPAD=0; _S_WIN_WH=1536_366; tt_anti_token=BeQuM60e3q3-df8cfc0eaf270ecadb30fbfd1cce001157885615ff7414215157c4a2e454c6b8; MONITOR_WEB_ID=28f9a528-9755-44ef-8050-8d9a03458893; ttwid=1%7CeJMh3Kg-lvbULz9EeRTY9ZB2yURhjWjdCBZ0JFNWj1g%7C1620776532%7C1a38cba4eb24d4141bb8477b42341681b3c8b416508872a473ca9a54f7a38e49; tt_scid=1-raH3.-87elJ.rMkG9rVz0RfDHeY4uH-m0RzpB5upteOgTTbv8sM4DtxKy4P4tNfcbc'
}
with open(r'js1.js', 'r', encoding="utf-8") as f:
    ctx = execjs.compile(f.read())


def get_signature(p):
    signature = ctx.call('get_signature', p)
    return signature


max_behot_time = 1620730781
p = f'/api/pc/list/feed?channel_id=0&max_behot_time={max_behot_time}&category=pc_profile_recommend'
signature = get_signature(p)
url = 'https://www.toutiao.com' + p + '&_signature=' + signature
print(url)
resp = requests.get(url=url, headers=headers)
print(resp.text)
