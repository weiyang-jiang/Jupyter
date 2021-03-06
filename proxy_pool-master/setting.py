# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setting.py
   Description :   配置文件
   Author :        JHao
   date：          2019/2/15
-------------------------------------------------
   Change Activity:
                   2019/2/15:
-------------------------------------------------
"""

BANNER = r"""
****************************************************************
*** ______  ********************* ______ *********** _  ********
*** | ___ \_ ******************** | ___ \ ********* | | ********
*** | |_/ / \__ __   __  _ __   _ | |_/ /___ * ___  | | ********
*** |  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | | ********
*** | |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___  ****
*** \_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____/ ****
****                       __ / /                          *****
************************* /___ / *******************************
*************************       ********************************
****************************************************************
"""

SHOW_CONFIG = True            # print key config

# ############### server config ###############
HOST = "127.0.0.1"

PORT = 5010

# ############### db config ###################
# db connection uri
# example:
#      Redis: redis://:password@ip:port/db
#      Ssdb:  ssdb://:password@ip:port
DB_CONN = "redis://@127.0.0.1:6379"

# proxy table name
TABLE_NAME = 'use_proxy'


# ###### config the proxy fetch function ######
PROXY_FETCHER = [
    "freeProxy01",
    # "freeProxy02",
    # "freeProxy03",
    "freeProxy04",
    "freeProxy05",
    # "freeProxy06",
    "freeProxy07",
    # "freeProxy08",
    "freeProxy09",
    "freeProxy13",
    "freeProxy14",
    "freeProxy15",
]

# ############# proxy validator #################
VERIFY_RUL = "http://www.baidu.com"

VERIFY_TIMEOUT = 10

MAX_FAIL_COUNT = 0


