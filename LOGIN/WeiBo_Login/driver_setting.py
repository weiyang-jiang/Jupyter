
"""
-------------------------------------------------
   File Name：     driver_setting.py
   Description :   chromedriver 的配置文件
   Author :       weiyang
   date：          2020-7-27
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""
from selenium import webdriver
from WeiBo_Login.settings import Driver_path

def create_driver():
    '''
    初始化 webdriver
    '''
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2
        }
    }
    chrome_options.add_experimental_option('prefs', prefs)
    # 禁用gpu加速，防止出一些未知bug

    chrome_options.add_argument('--disable-gpu')
    # 如果验证码可以处理的话就可以设置无头模式
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-infobars")

    # 这里我用 chromedriver 作为 webdriver
    # 可以去 http://chromedriver.chromium.org/downloads 下载你的chrome对应版本
    browser = webdriver.Chrome(executable_path=Driver_path,
                                    chrome_options=chrome_options)
    # 设置一个隐性等待 5s
    browser.implicitly_wait(5)

    return browser

if __name__ == '__main__':
    browser = create_driver()
    browser.get("https://blog.csdn.net/qq_42145862/article/details/92103811?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task")
