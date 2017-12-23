# -*- coding: utf-8 -*-
BOT_NAME='hotel'
SPIDER_MODULES = ['hotel.spiders']
NEWSPIDER_MODULE = 'hotel.spiders'
DOWNLOADER_MIDDLEWARES = {  
"hotel.middlewares.UserAgentMiddleware":401,
"hotel.middlewares.ProxyMiddleware":402,
}
COOKIES_ENABLED=False
REDIRECT_ENABLED=False