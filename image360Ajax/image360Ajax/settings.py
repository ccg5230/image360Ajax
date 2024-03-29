# -*- coding: utf-8 -*-

# Scrapy settings for image360Ajax project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'image360Ajax'

SPIDER_MODULES = ['image360Ajax.spiders']
NEWSPIDER_MODULE = 'image360Ajax.spiders'

MAX_PAGE = 50

ITEM_PIPELINES = {
    'image360Ajax.pipelines.ImagePipeline': 300,
    'image360Ajax.pipelines.MongoPipeline': 301,
    'image360Ajax.pipelines.MysqlPipeline': 302,
}
# 'mongodb://' + user + ':' + pwd + '@' + server + ':' + port +'/'+ db_name
MONGO_URI='mongodb://superAdmin:superAdmin@localhost:27017'
MONGO_DB='studyTest'
#MYSQL
MYSQL_HOST='localhost'
MYSQL_DATABASE='mybatis_example'
MYSQL_USER='root'
MYSQL_PASSWORD='root'
MYSQL_PORT=3306

IMAGES_STORE='./images'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'image360Ajax (+http://www.yourdomain.com)'

# Obey robots.txt rules
#告诉搜索引擎爬虫，本网站哪些目录下的网页 不希望 你进行爬取收录。我们并不是在做搜索引擎，
# 而且在某些情况下我们想要获取的内容恰恰是被 robots.txt 所禁止访问的。所以，
# 某些时候，我们就要将此配置项设置为 False ，拒绝遵守 Robot协议 ！
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'image360Ajax.middlewares.Image360AjaxSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'image360Ajax.middlewares.Image360AjaxDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'image360Ajax.pipelines.Image360AjaxPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
