# coding: utf-8

from datetime import datetime
import time
import random
import json
import requests
from requests.adapters import HTTPAdapter

s = requests.Session()
requests.adapters.DEFAULT_RETRIES = 5
s.mount('http://', HTTPAdapter(max_retries=5))
s.mount('https://', HTTPAdapter(max_retries=5))


def search(open_id, search_key, keyword):

    print "process keywords: %s" % keyword.encode("UTF8")

    s_url = "https://search.weixin.qq.com/cgi-bin/searchweb/wxindex/querywxindexgroup?wxindex_query_list=%s&gid=&openid=%s&search_key=%s" % (keyword, open_id, search_key)
    headers = {
        "Referer": "https://servicewechat.com/wxc026e7662ec26a3a/7/page-frame.html",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.117 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/WIFI Language/zh_CN Process/appbrand0",
    }
    ss = s.get(s_url, headers=headers, timeout=3)
    content = json.loads(ss.content)

    wxindex_str = content["data"]["group_wxindex"][0]["wxindex_str"]

    if wxindex_str == "":
        pass

    return wxindex_str.split(",")


def sleep():
    time.sleep(random.randint(2, 4))


if __name__ == '__main__':
    t = datetime.now()
    print "start time: %s" % t

    keywords = ["华为", "小米", "OPPO", "VIVO"]
    open_id = "open_id"
    search_key = "search_key"

    for keyword in keywords:

        wis = search(open_id, search_key, keyword)
        print wis

    print "execution time: %s [%s]" % (datetime.now() - t, datetime.now())

