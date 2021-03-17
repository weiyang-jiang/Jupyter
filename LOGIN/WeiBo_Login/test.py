
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test.py
   Description :   测试文件
   Author :       weiyang
   date：          2020-7-27
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""

import json, requests

url = "http://127.0.0.1:5010/get"


# server返回的请求
response = requests.get(url=url)

# response.json()是dict格式， .values()是dict_value格式,通过sorted()转换成list格式[{}]
content = response.content.decode("utf8")
cookies = json.loads(content)["proxy"]
print("http://" + cookies)
# 这是server返回的data的格式, 具体实现请看main.py的return
# list [ ] 中的内容
# {
# 	cookies:
# 		[
# 			{
# 				'username': '...'
# 				'cookies' : '...'
# 				'id' : '...'
# 			}
# 			{
# 				...
# 			}
# 		]
# }
#
# list 中的内容
# cookies = list[0]
# print(type(cookies))
# 获取每一条数据的内容
# for cookie in cookies:
# 	print("------------username: ")
# 	print(cookie[0])
# 	print("------------cookie")
# 	print(cookie[1])
# HEADERS = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "zh-CN,zh;q=0.9",
#         "Cookie": "SUB=_2A25yEincDeRhGeBG4loZ9y7Jzz2IHXVRZhwUrDV8PUNbmtANLRDZkW9NQcvZIWzvUMPHZW28M1pbcFL90mZkypcY;",
#         "Sec-Fetch-Dest": "document",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-Site": "same-origin",
#         "Sec-Fetch-User": "?1",
#         "Upgrade-Insecure-Requests": "1",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
#     }
# import requests
# res = requests.get(url="https://m.weibo.cn/profile/3960916077",headers=HEADERS)
# print(res.text)
# print(res.url)
import time
#
# from WeiBo_Login.driver_setting import *
#
# browers = create_driver()
# browers.delete_all_cookies()
# browers.get("https://login.sina.com.cn/sso/login.php")
# browers.add_cookie(cookie_dict={"name":"SUB","value":"_2A25yEincDeRhGeBG4loZ9y7Jzz2IHXVRZhwUrDV8PUNbmtANLRDZkW9NQcvZIWzvUMPHZW28M1pbcFL90mZkypcY"})
# browers.get("https://weibo.com/u/3960916077")
# content = browers.find_elements_by_xpath('//h1[@class="username"]/text()')
# cookies = browers.get_cookies()
# print(content)
# print(cookies)






# import pymysql
# import random
# from WeiBo_Login.settings import *
# username = random.choice(infos)["username"]
# conn = pymysql.connect(**DATABASE_INFO)
# cursor = conn.cursor()
# sql = "select * from cookies;"
# try:
#     cursor.execute(sql)
#     conn.commit()
#     cookies = cursor.fetchall()
#     print(type(cookies))
#     print(cookies)
# except Exception as e:
#     conn.rollback()
#     print(e)
#     cookies = None
# finally:
#     cursor.close()
#     conn.close()
# print(time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time())))
