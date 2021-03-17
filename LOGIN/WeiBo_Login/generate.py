
"""
-------------------------------------------------
   File Name：     generate.py
   Description :   cookie池总的调度器
   Author :       weiyang
   date：          2020-7-27
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""


from WeiBo_Login.Cookies_Get import WeiboCookies
from WeiBo_Login.driver_setting import create_driver
from WeiBo_Login.settings import *
from WeiBo_Login.verify_cookies import *
from WeiBo_Login.read_cookie import *
from WeiBo_Login.save_cookie import *
import os
import logging
from WeiBo_Login import LOGGER_SPIDER # 导入自定义的logging配置
logger = logging.getLogger(__name__)  # 生成logger实例
LOGGER_SPIDER.load_my_logging_cfg()

def run_cookies_pool():
    for info in infos:
        username = info["username"]
        conn = pymysql.connect(**DATABASE_INFO)
        cursor = conn.cursor()
        sql = "select * from cookies where username=%s;"
        if cursor.execute(sql,(username,)) == 1:
            try:
                username,cookie = read_cookie_mysql(username) # 从数据库中读取数据
                # username,cookie = read_cookie(username) # 从json文件中读取数据
                if verify_cookies(username,cookie):
                    logger.info(f"{username}的{cookie}没过期继续用")
                else:
                    os.remove(COOKIES_FILE_PATH.format(username=username))
                    get_cookies(info)
                    logger.info(f"{username}已经更新")
            except Exception as e:
                logger.info("文件操作出错")
        else:
            get_cookies(info)

def get_cookies(info):
    browser = create_driver()
    username = info["username"]
    password = info["password"]
    cookie = WeiboCookies(username, password, browser).main()
    if cookie.startswith("_"):
        verify_cookies(username, cookie)
        save_cookies_mysql(username, cookie) # 存储到数据库中
        # save_cookies(username, cookie)  # 存储到json文件中
    browser.close()