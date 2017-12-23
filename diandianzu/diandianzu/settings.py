# -*- coding: utf-8 -*-

# Scrapy settings for diandianzu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'diandianzu'

SPIDER_MODULES = ['diandianzu.spiders']
NEWSPIDER_MODULE = 'diandianzu.spiders'

DOWNLOADER_MIDDLEWARES = {
"diandianzu.middlewares.UserAgentMiddleware":401,
"diandianzu.middlewares.ProxyMiddleware":402,
}
COOKIES_ENABLED=False
REDIRECT_ENABLED=False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'diandianzu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

