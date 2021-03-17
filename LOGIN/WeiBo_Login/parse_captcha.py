
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     parse_captcha.py
   Description :   处理验证码
   Author :       weiyang
   date：          2020-7-27
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""


from WeiBo_Login.driver_setting import create_driver


def parse_image():
    pass


# def get_position(self):
    #     """
    #     获取验证码位置
    #     :return: 验证码位置元组
    #     """
    #     try:
    #         img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'patt-shadow')))
    #     except TimeoutException:
    #         print('未出现验证码')
    #         self.open()
    #     time.sleep(2)
    #     location = img.location
    #     size = img.size
    #     top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
    #         'width']
    #     return (top, bottom, left, right)

    # def get_screenshot(self):
    #     """
    #     获取网页截图
    #     :return: 截图对象
    #     """
    #     screenshot = self.browser.get_screenshot_as_png()
    #     screenshot = Image.open(BytesIO(screenshot))
    #     return screenshot

    # def get_image(self, name='captcha.png'):
    #     """
    #     获取验证码图片
    #     :return: 图片对象
    #     """
    #     top, bottom, left, right = self.get_position()
    #     print('验证码位置', top, bottom, left, right)
    #     screenshot = self.get_screenshot()
    #     captcha = screenshot.crop((left, top, right, bottom))
    #     return captcha
    #
    # def is_pixel_equal(self, image1, image2, x, y):
    #     """
    #     判断两个像素是否相同
    #     :param image1: 图片1
    #     :param image2: 图片2
    #     :param x: 位置x
    #     :param y: 位置y
    #     :return: 像素是否相同
    #     """
    #     # 取两个图片的像素点
    #     pixel1 = image1.load()[x, y]
    #     pixel2 = image2.load()[x, y]
    #     threshold = 20
    #     if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
    #             pixel1[2] - pixel2[2]) < threshold:
    #         return True
    #     else:
    #         return False
    #
    # def same_image(self, image, template):
    #     """
    #     识别相似验证码
    #     :param image: 待识别验证码
    #     :param template: 模板
    #     :return:
    #     """
    #     # 相似度阈值
    #     threshold = 0.99
    #     count = 0
    #     for x in range(image.width):
    #         for y in range(image.height):
    #             # 判断像素是否相同
    #             if self.is_pixel_equal(image, template, x, y):
    #                 count += 1
    #     result = float(count) / (image.width * image.height)
    #     if result > threshold:
    #         print('成功匹配')
    #         return True
    #     return False
    #
    # def detect_image(self, image):
    #     """
    #     匹配图片
    #     :param image: 图片
    #     :return: 拖动顺序
    #     """
    #     for template_name in listdir(TEMPLATES_FOLDER):
    #         print('正在匹配', template_name)
    #         template = Image.open(TEMPLATES_FOLDER + template_name)
    #         if self.same_image(image, template):
    #             # 返回顺序
    #             numbers = [int(number) for number in list(template_name.split('.')[0])]
    #             print('拖动顺序', numbers)
    #             return numbers
    #
    # def move(self, numbers):
    #     """
    #     根据顺序拖动
    #     :param numbers:
    #     :return:
    #     """
    #     # 获得四个按点
    #     try:
    #         circles = self.browser.find_elements_by_css_selector('.patt-wrap .patt-circ')
    #         dx = dy = 0
    #         for index in range(4):
    #             circle = circles[numbers[index] - 1]
    #             # 如果是第一次循环
    #             if index == 0:
    #                 # 点击第一个按点
    #                 ActionChains(self.browser) \
    #                     .move_to_element_with_offset(circle, circle.size['width'] / 2, circle.size['height'] / 2) \
    #                     .click_and_hold().perform()
    #             else:
    #                 # 小幅移动次数
    #                 times = 30
    #                 # 拖动
    #                 for i in range(times):
    #                     ActionChains(self.browser).move_by_offset(dx / times, dy / times).perform()
    #                     time.sleep(1 / times)
    #             # 如果是最后一次循环
    #             if index == 3:
    #                 # 松开鼠标
    #                 ActionChains(self.browser).release().perform()
    #             else:
    #                 # 计算下一次偏移
    #                 dx = circles[numbers[index + 1] - 1].location['x'] - circle.location['x']
    #                 dy = circles[numbers[index + 1] - 1].location['y'] - circle.location['y']
    #     except:
    #         return False

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
from six import BytesIO
import time
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import requests
# import chaojiying  #超级鹰提供的模块，需要去官网下载


class Verifycode():

    def __init__(self,username,password,url):
        self.browser = create_driver()
        self.username = username
        self.password = password
        self.url = url
        self.wait = WebDriverWait(self.browser, 10)

    def get_url(self):
        self.browser.delete_all_cookies() # 删除所有的cookie信息
        self.browser.maximize_window() # 最大化窗口
        self.browser.get(self.url) # 访问指定的url
        username = self.wait.until(EC.presence_of_element_located((By.ID, 'loginName')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'loginPassword')))
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginAction')))
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(1)
        submit.click()
        # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_radar_btn')))
        # user_input, pwd_input, *_ = self.browser.find_elements_by_css_selector('input.ivu-input')
        # print(user_input)
        # btn = self.browser.find_element_by_css_selector('.geetest_radar_btn')
        # user_input.send_keys(user)
        # pwd_input.send_keys(password)
        # btn.click()
        # time.sleep(1)
        if self.login_successfully():
            return True
        else:
            self.click_btn()
            return self.login_successfully()

    def login_successfully(self):
        """
        判断是否登录成功
        :return:
        """
        try:
            return bool(
                WebDriverWait(self.browser, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'lite-iconf-profile'))))
        except TimeoutException:
            return False

    def click_btn(self):
        time.sleep(1)
        click_verify = self.browser.find_element_by_class_name("geetest_radar_tip")
        click_verify.click()
        print("点击成功")

     # 获取显示结果的标签

    # def get_position(self, img_label):
    #     location = img_label.location
    #     size = img_label.size
    #     top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
    #         'width']
    #     return (left, top, right, bottom)

    # def get_screenshot(self):
    #     screenshot = self.browser.get_screenshot_as_png()
    #     f = BytesIO()
    #     f.write(screenshot)
    #     return Image.open(f)

    # def get_position_scale(self, screen_shot):
    #     height = self.browser.execute_script('return document.documentElement.clientHeight')
    #     width = self.browser.execute_script('return document.documentElement.clientWidth')
    #     x_scale = screen_shot.size[0] / (width + 10)
    #     y_scale = screen_shot.size[1] / (height)
    #     return (x_scale, y_scale)

    # def get_slideimg_screenshot(self, screenshot, position, scale):
    #     x_scale, y_scale = scale
    #     position = [position[0] * x_scale, position[1] * y_scale, position[2] * x_scale, position[3] * y_scale]
    #     return screenshot.crop(position)

    # def compare_pixel(self, img1, img2, x, y):
    #     pixel1 = img1.load()[x, y]
    #     pixel2 = img2.load()[x, y]
    #     threshold = 50
    #     if abs(pixel1[0] - pixel2[0]) <= threshold:
    #         if abs(pixel1[1] - pixel2[1]) <= threshold:
    #             if abs(pixel1[2] - pixel2[2]) <= threshold:
    #                 return True
    #     return False

    # def compare(self, full_img, slice_img):
    #     left = 65
    #     for i in range(full_img.size[0]):
    #         for j in range(full_img.size[1]):
    #             if not self.compare_pixel(full_img, slice_img, i, j):
    #                 return i
    #     return left

    # def get_track(self, distance):
    #     """
    #     根据偏移量获取移动轨迹
    #     :param distance: 偏移量
    #     :return: 移动轨迹
    #     """
    #     # 移动轨迹
    #     track = []
    #     # 当前位移
    #     current = 0
    #     # 减速阈值
    #     mid = distance * 4 / 5
    #     # 计算间隔
    #     t = 0.2
    #     # 初速度
    #     v = 0
    #
    #     while current < distance:
    #         if current < mid:
    #             # 加速度为正 2
    #             a = 4
    #         else:
    #             # 加速度为负 3
    #             a = -3
    #         # 初速度 v0
    #         v0 = v
    #         # 当前速度 v = v0 + at
    #         v = v0 + a * t
    #         # 移动距离 x = v0t + 1/2 * a * t^2
    #         move = v0 * t + 1 / 2 * a * t * t
    #         # 当前位移
    #         current += move
    #         # 加入轨迹
    #         track.append(round(move))
    #     return track

    # def move_to_gap(self, slider, tracks):
    #     """
    #     拖动滑块到缺口处
    #     :param slider: 滑块
    #     :param tracks: 轨迹
    #     :return:
    #     """
    #     ActionChains(self.browser).click_and_hold(slider).perform()
    #     for x in tracks:
    #         ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
    #     time.sleep(0.5)
    #     ActionChains(self.browser).release().perform()

    # def is_slide(self):
    #     time.sleep(1)
    #     try:
    #         slie_img = self.browser.find_element_by_css_selector('canvas.geetest_canvas_slice')
    #         if slie_img:
    #             return slie_img
    #     except NoSuchElementException:
    #         return False

    # def slide_code(self):
    #     slice_img_label = self.browser.find_element_by_css_selector('div.geetest_slicebg')  # 找到滑动图片标签
    #     self.browser.execute_script(
    #         "document.getElementsByClassName('geetest_canvas_slice')[0].style['display'] = 'none'")  # 将小块隐藏
    #     full_img_label = self.browser.find_element_by_css_selector('canvas.geetest_canvas_fullbg')  # 原始图片的标签
    #     position = self.get_position(slice_img_label)  # 获取滑动验证图片的位置
    #     screenshot = self.get_screenshot()  # 截取整个浏览器图片
    #     position_scale = self.get_position_scale(screenshot)  # 获取截取图片宽高和浏览器宽高的比例
    #     slice_img = self.get_slideimg_screenshot(screenshot, position, position_scale)  # 截取有缺口的滑动验证图片
    #
    #     self.browser.execute_script(
    #         "document.getElementsByClassName('geetest_canvas_fullbg')[0].style['display'] = 'block'")  # 显示原图
    #     screenshot = self.get_screenshot()  # 获取整个浏览器图片
    #     full_img = self.get_slideimg_screenshot(screenshot, position, position_scale)  # 截取原图
    #     self.browser.execute_script(
    #         "document.getElementsByClassName('geetest_canvas_slice')[0].style['display'] = 'block'")  # 将小块重新显示
    #     left = self.compare(full_img, slice_img)  # 将原图与有缺口图片进行比对，获得缺口的最左端的位置
    #     left = left / position_scale[0]  # 将该位置还原为浏览器中的位置
    #
    #     slide_btn = self.browser.find_element_by_css_selector('.geetest_slider_button')  # 获取滑动按钮
    #     track = self.get_track(left)  # 获取滑动的轨迹
    #     self.move_to_gap(slide_btn, track)  # 进行滑动
    #     time.sleep(2)

    # def is_pick(self):
    #     try:
    #         pick_img = self.browser.find_element_by_css_selector('img.geetest_item_img')
    #         return pick_img
    #     except NoSuchElementException:
    #         return False

    # def pick_code(self):
    #     time.sleep(1)
    #     pick_img_label = self.browser.find_element_by_css_selector('img.geetest_item_img') #获取点触图片标签
    #     src = pick_img_label.get_attribute('src')  #获取点触图片链接
    #     img_content = requests.get(src).content  #获取图片二进制内容
    #     f = BytesIO()
    #     f.write(img_content)
    #     img0 = Image.open(f)  #将图片以文件的形式打开，主要是为了获取图片的大小
    #     scale = [pick_img_label.size['width'] / img0.size[0], pick_img_label.size['height'] / img0.size[1]] #获取图片与浏览器该标签大小的比例
    #     cjy = chaojiying.Chaojiying_Client('*******', '******', '901489') #登录超级鹰
    #     result = cjy.PostPic(img_content, '9005') #发送图片并获取结果
    #     if result['err_no'] == 0:  #对结果进行分析
    #         position = result['pic_str'].split('|')  # position = ['110,234','145,247','25,185']
    #         position = [[int(j) for j in i.split(',')] for i in position]  # position = [[110,234],[145,247],[25,185]]
    #         for items in position:  #模拟点击
    #             ActionChains(self.browser).move_to_element_with_offset(pick_img_label, items[0] * scale[0],
    #                                                                    items[1] * scale[1]).click().perform()
    #             time.sleep(1)
    #         certern_btn = self.browser.find_element_by_css_selector('div.geetest_commit_tip')
    #         certern_btn.click()
    #     return cjy,result


if __name__ == '__main__':

    verifycode = Verifycode('15636486842','aaa123','https://passport.weibo.cn/signin/login?entry=mweibo&r=https://m.weibo.cn/')
    verifycode.get_url()

    # elif verifycode.is_slide():
    #     verifycode.slide_code()
    #     if verifycode.is_success():
    #         print('slide success')
    #     else:
    #         print('slide failure')
    # elif verifycode.is_pick():
    #     cjy,result = verifycode.pick_code()
    #     if verifycode.is_success():
    #         print('pick click success')
    #     else:
    #         print('pick click failure')
    #         if result['err_no'] == 0:
    #             r = cjy.ReportError(result['pic_id'])
    #             print(r)