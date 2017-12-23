# -*- coding: utf-8 -*-
import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    city = scrapy.Field()
    address = scrapy.Field()
    layer = scrapy.Field()
    price = scrapy.Field()
