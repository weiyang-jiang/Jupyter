# -*- coding: utf-8 -*-
__author__ = "姜维洋"


import json
import requests

PROXY_POOL_URL = 'http://127.0.0.1:5010/get/'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            response = requests.get(PROXY_POOL_URL)
            content = response.content.decode("utf8")
            proxy = json.loads(content)["proxy"]
            return proxy
    except Exception as e:
        print(e)
        return get_proxy()


def get_html():
    try:
        r = requests.get(url = 'http://httpbin.org/get',proxies={'http':'http://%s' % get_proxy()},timeout=2)
        if r.status_code == 200:
            print(r.text)
    except Exception as e:
        print(e)
        pass

for i in range(10):
    get_html()

def verify_ip(ip_port):
    pass



# import json
# import requests
#
# PROXY_POOL_URL = 'http://127.0.0.1:5010/get/'
#
# def get_proxy():
#     try:
#         response = requests.get(PROXY_POOL_URL)
#         if response.status_code == 200:
#             response = requests.get(PROXY_POOL_URL)
#             content = response.content.decode("utf8")
#             proxy = json.loads(content)["proxy"]
#             return proxy
#     except Exception as e:
#         print(e)
#         return get_proxy()
#
#
# def get_html():
#     try:
#         r = requests.get(url = 'http://httpbin.org/get',proxies={'http':'http://%s' % get_proxy()},timeout=2)
#         if r.status_code == 200:
#             print(r.status_code)
#     except Exception as e:
#         print(e)
#         pass
#
# for i in range(10):
#     get_html()
#
# def verify_ip(ip_port):
#     pass
import pymysql
INFO = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "root",
            # "password":"200046",
            "database": "data",
            "charset": "utf8",
        } # 数据库配置文件
conn = pymysql.connect(**INFO)
cur = conn.cursor()
sql = "select * from cookies where username = %s and cookies = %s;"
cur.execute(sql,("gehc06450208bu@163.com","_2A25yGWXeDeRhGeFN6VMV9CnLyzqIHXVR4guWrDV6PUJbkdAKLXTckW1NQEM9jS_rfeIKMOsnEPqs0RvXC1ci9-sV;"))
c= cur.fetchone()
print(c)

