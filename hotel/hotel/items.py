# -*- coding: utf-8 -*-
import scrapy
class hotelItem(scrapy.Item):
    url=scrapy.Field()
    name=scrapy.Field()
    address=scrapy.Field()
    price=scrapy.Field()
