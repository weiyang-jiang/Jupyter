__author__= "姜维洋"

# from settings import COOKIES_URL, HEADERS, verify_url
# import requests
# import json
# import  logging
# logger = logging.getLogger(__name__)
# url = COOKIES_URL
# headers = {'User-agent': 'jumbox'}
# resp = requests.get(url=url,headers = headers)
# content = resp.content.decode("utf8")
# datas = json.loads(content)["cookies"]
#
# def verify_cookies(username,cookie):
#     try:
#         HEADERS["Cookie"] = "SUB=" + cookie
#         response = requests.get(verify_url,headers=HEADERS)
#         if response.url == verify_url:
#             logger.info(f"[{username}]用户的{cookie}没有过期，成功登录")
#             return True
#         else:
#             logger.info(f"[{username}]用户的{cookie}过期，登录失败")
#             return False
#     except Exception as e:
#         print(f"{username}登录出错，原因{e}")
#         return False
#
# def verify_spider():
#     is_id = True
#     for data in datas:
#         if verify_cookies(data[0],data[1]):
#             pass
#         else:
#             is_id = False
#             return is_id
#     return is_id

def run_scrapy():
    from scrapy import cmdline
    pin = input("""
请输入你要爬取数据的形式
1.按照博主爬取请输入 ：1
2.按照搜索话题爬取数据请输入 ：2
："""
)
    if pin == "1" or "2":
        cmdline.execute(f"scrapy crawl WEIBO -a pin={pin}".split())
    else:
        print("输入格式不正确")

if __name__ == '__main__':
    run_scrapy()
