__author__= "姜维洋"
# 运行文件
def run_scrapy():
    from scrapy import cmdline
    cmdline.execute("scrapy crawl UNNCSPIDER".split())

if __name__ == '__main__':
    run_scrapy()