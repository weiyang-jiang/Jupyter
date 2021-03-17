__author__= "姜维洋"

# Scrapy settings for ZhiHu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ZhiHu'

SPIDER_MODULES = ['ZhiHu.spiders']
NEWSPIDER_MODULE = 'ZhiHu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ZhiHu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Cache-Control': 'max-age=0',
# 'Cookie': 'SESSIONID=wzsiUD5XnUjXfCDqmUpGB2fcoCjbTbMPiyRN1YqKQgz; JOID=U1gcAU3Kqef8cKkhLMmvOaM7p6k1jui7vgTKT36pn9mcQMhBbVqB4KB2oSMjH1qME86ZRRrZUEfyxS9Ze0mSZDM=; osd=V18SAUPOrun8fq0mIsmhPaQ1p6cxiea7sADNQX6nm96SQMZFalSB7qRxryMtG12CE8CdQhTZXkP1yy9Xf06cZD0=; _zap=b150dafc-e5e7-4331-96eb-a6973d6d13cb; d_c0="ABBQXggifRGPTlyFqHZBn8AbRaDFbOBy5gE=|1593235305"; _ga=GA1.2.1413905039.1593235307; _xsrf=86d5fd94-478e-4755-9d6b-1730f62f237b; _gid=GA1.2.810732245.1594364879; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1594105242,1594364878,1594365701,1594367083; capsion_ticket="2|1:0|10:1594370129|14:capsion_ticket|44:NjRlMjc4NzY0ZWNkNGZhODllYTMzM2U1OTI3ODlkMDk=|8a9c26c43d7beb1458502fb5ef12157ccbaf02038a8c409beadc3bf2ea19c30d"; z_c0="2|1:0|10:1594370161|4:z_c0|92:Mi4xR2twN0NnQUFBQUFBRUZCZUNDSjlFU1lBQUFCZ0FsVk5jWGIxWHdCcmdQTHlrV1VobzNFWkJoZ1lXSEZfR2JjY1N3|b5d82546d25afd95466404bbc91fd76559bca65d22322def264dc743c0311199"; tst=r; KLBRSID=d1f07ca9b929274b65d830a00cbd719a|1594370738|1594370709; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1594370738',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-site',
'Sec-Fetch-User': '?1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ZhiHu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ZhiHu.middlewares.ZhihuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'ZhiHu.pipelines.ZhihuPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
