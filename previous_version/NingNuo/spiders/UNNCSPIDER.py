# -*- coding: utf-8 -*-
__author__= "姜维洋"
# 爬虫文件
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from NingNuo.items import NingnuoItem

class UnncspiderSpider(CrawlSpider):
    name = 'UNNCSPIDER'
    # allowed_domains = ['www.nottingham.edu.cn']
    start_urls = ['https://www.nottingham.edu.cn/en/press-release/news-listing.aspx?pageIndex=0']

    # rules = (
    #     Rule(LinkExtractor(allow=r'.+pageIndex=\d+$'), callback='parse_item', follow=True),
    # )
    rules = (
        Rule(LinkExtractor(allow=r'.+pageIndex=1'), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        lis = response.xpath("//ul[@class='article-listing']/li")
        for li in lis:
            url = "https://www.nottingham.edu.cn"+li.xpath(".//div/h2/a/@href").get().strip()
            datetime = li.xpath(".//div[@class='article-listing__content']/p/text()").get().strip()
            title = li.xpath(".//div/h2/a/text()").get().strip()
            yield scrapy.Request(url=url, callback=self.parse_page, meta={"datetime": datetime, "title": title, "url": url})

    def parse_page(self, response):
        item = NingnuoItem()
        contents = []
        summary = response.xpath("//div[@class='summary']/p/text()").get()
        if summary:
            summary = summary.strip()
        else:
            summary = "NONE"
        pages = response.xpath("//article[contains(@class,'article-body')]/div[not(@class='summary')]//p")
        item["summary"] = summary
        item["datetime"] = response.meta["datetime"]
        item["title"] = response.meta["title"]
        item["url"] = response.meta["url"]
        for page in pages:
            content = page.xpath(".//text()").get()
            if content:
                contents.append(content.strip())
        item["contents"] = contents
        return item