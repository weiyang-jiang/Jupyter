__author__= "姜维洋"

# import json
#
# from WeiBo.settings import FILE_PATH
#
# data = {'author': '每天都有新实习',
#  'comment_count': '18',
#  'content_comment': ':咨询公司里面现在综排第一的是德勤，虽然大家并不太认。',
#  'like_count': '44',
#  'pub_time': '2020-07-04',
#  'share_count': '2',
#  'url': 'https://weibo.cn/comment/J9GyQbTAe?uid=3960916077&rl=0'}
# data_json = json.dumps(data,ensure_ascii=False)
# print(data_json)
# with open(FILE_PATH, 'a+', encoding='utf-8') as file:
#         file.writelines(data_json + "\n")
#         print("成功")

# import time
# print(time.localtime())
# print(time.strftime("%Y%m%d",time.localtime()))
# import re
#
# url = 'https://weibo.cn/comment/J6TUoqRDZ?uid=1000'
# url_id = re.search(r".*/(.+)\?.+?",url).group(1)
# print(url_id)
import re

# import requests
# import json
#
from WeiBo.settings import COOKIES_URL
#
# url = "http://127.0.0.1:5000/api"
#
# resp = requests.get(url)
#
# content = resp.content.decode("utf8")
#
# datas = json.loads(content)["cookies"]

url_path = re.match(r".+:\d+/(.+)",COOKIES_URL).group(1)
print(url_path)


