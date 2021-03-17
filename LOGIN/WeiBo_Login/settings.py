
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     settings.py
   Description :   cookie池的配置文件
   Author :       weiyang
   date：          2020-7-27
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""

from os.path import dirname, abspath
import os

Driver_path = r'../lib/chromedriver' # chromdriver的引擎路径
# Driver_path = r'D:\chromedriver\chromedriver.exe' # chromdriver的引擎路径
verify_url = "https://weibo.cn/u/3960916077" # 准备验证的微博网址



COOKIES_FILE_PATH = os.path.join(dirname(abspath(__file__)) + '/templates/',"weibo_login_cookies{username}.json")


infos = [
    {"username":"bopo7542110362@163.com","password":"vcezhloyba"},
    {"username":"muzhong85746197@163.com","password":"lvusfiz4jq"},
    {"username":"gehc06450208bu@163.com","password":"mxayn0i06j"},
    {"username":"de96325918quhanj@163.com","password":"hqhqtgqkct"},
    {"username":"bztj2053333han@163.com","password":"qgodd9losq"},
]
# bopo7542110362@163.com----vcezhloyba
# muzhong85746197@163.com----lvusfiz4jq
# gehc06450208bu@163.com----mxayn0i06j
# de96325918quhanj@163.com----hqhqtgqkct
# bztj2053333han@163.com----qgodd9losq


DEFAULT_REQUEST_HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "",
        "Referer": "https://weibo.cn/u/3960916077?page=2",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }


# DATABASE_INFO = {
#             "host": "localhost",
#             "port": 3306,
#             "user": "root",
#             "password": "200046",
#             # "password":"root",
#             "database": "data",
#             "charset": "utf8",
#         }

# Jerrio's Database
DATABASE_INFO = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "root",
            "database": "Jupiter",
            "charset": "utf8",
        }

COOKIES_URL = "http://127.0.0.1:5001/jumbox"
