# -*- coding: utf-8 -*-
__author__= "姜维洋"
import re
import time
import scrapy
from scrapy import Request,FormRequest
from WEIBOSEARCH.items import WeibosearchItem
from WEIBOSEARCH.settings import TOPIC, max_page

class WeibosearchSpider(scrapy.Spider):
    name = 'WeiboSearch'
    search_url = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword={topic}&advancedfilter=1&endtime={time}&sort=hot'
    # allowed_domains = ['weibo.cn']
    # start_urls = ['http://weibo.cn/']
    keyword_search = 100


    def parse_time(self,datetime):
        if re.match("今天.*", datetime):
            datetime = time.strftime("%Y-%m-%d", time.localtime()) + re.match("今天(.*)", datetime).group(1)
        if re.match("\d+分钟前", datetime):
            minute = re.match("(\d+)分钟前", datetime).group(1)
            datetime = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time() - float(minute) * 60))
        if re.match("\d+月\d+日", datetime):
            month = re.match("(\d+)月(\d+)日", datetime).group(1)
            day = re.match("(\d+)月(\d+)日", datetime).group(2)
            datetime = time.strftime("%Y", time.localtime()) + "-" + month + "-" + day
        return datetime

    def start_requests(self):
        print("按照搜索信息爬取数据")
        for topic in TOPIC:
            for page in range(max_page):
                form_data = {
                    "mp": str(self.keyword_search),
                    "page": str(page)
                }
                yield FormRequest(url=self.search_url.format(topic=topic, time=time.strftime("%Y%m%d", time.localtime())),
                                  callback=self.parse_search, formdata=form_data)
                break  # 测试代码
    def parse_search(self, response):
        content_urls = response.xpath("//div[@class='c']//a[@class='cc']")
        for content_url in content_urls:
            content_url = content_url.xpath(".//@href").get().strip()
            yield Request(url=content_url, callback=self.parse_search_comment)

    def parse_search_comment(self,response):
        url = response.url
        url_id = re.search(r".*/(.+)\?.+?", url).group(1)
        share_count = response.xpath("//a[contains(.,'转发[')]/text()").re_first("转发\[(.*?)\]")
        comment_count = response.xpath("//span[contains(.,'评论[')]/text()").re_first("评论\[(.*?)\]")
        like_count = response.xpath("//a[contains(.,'赞[')]/text()").re_first("赞\[(.*?)\]")
        author = response.xpath("//div[@id='M_']//a[1]/text()").get().strip()
        pub_time = response.xpath("//div[@id='M_']//span[@class='ct']/text()").get().strip()
        pub_time = self.parse_time(pub_time)
        content_comments = response.xpath("//div[@id='M_']//span[@class='ctt']/text()").getall()
        content_comment = "".join(content_comments)
        item = WeibosearchItem(url_id=url_id,share_count=share_count,comment_count=comment_count,like_count=like_count,author=author,pub_time=pub_time,content_comment=content_comment,url=url)
        return item