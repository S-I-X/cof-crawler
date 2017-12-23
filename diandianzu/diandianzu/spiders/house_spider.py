# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
import requests, json
from scrapy.http import Request
import re
from diandianzu.items import HouseItem
import sys


class hotelSpider(CrawlSpider):
    name = 'HouseSpider'
    download_delay = 5
    custom_settings = {'ITEM_PIPELINES': {'diandianzu.pipelines.HousePipeline': 200}}
    mainUrl = 'http://%s.diandianzu.com'
    start_url = 'http://%s.diandianzu.com/listing'
    cityList = ['bj', 'sh', 'gz', 'sz', 'hz', 'xa', 'su', 'nj', 'nb']
    urlList = []
    def start_requests(self):
        for c in self.cityList:
            url = self.start_url %(c)
            print '*********************start_url:', url
            yield Request(url=url, callback=self.parse)
    def parse(self,response):
        res = Selector(response)
        self.urlList =self.urlList + res.xpath('//div[@class="info fl"]/div[@class="part1 clearfix"] \
        /h2[@class="fl"]/a/@href').extract()
        pageUrl = res.xpath('//div[@class="page fr"]/div/a[@class="next"]/@href').extract()
        print '*********************pageUrl:', pageUrl
        if pageUrl:
            url = response.url.split('/listing')
            print '******************split_url:', url[0]
            yield Request(url=url[0] + pageUrl[0], callback=self.parse)

        for u in self.urlList:
            url = response.url.split('/listing')
            yield Request(url=url[0] + u, callback=self.parse_detail)
    def parse_detail(self, response):
        res = Selector(response)
        item = HouseItem()

        print '********************response_url:', response.url
        url = response.url
        name = res.xpath('//div[@class="top-title clearfix"]/div[@class="top-buildingName fl"]/h1/text()').extract()
        city = res.xpath('//div[@class="top-attribute"]/p[@class="attr-location"]/a/text()').extract()
        address = res.xpath('//div[@class="clearfix donetime-address"]/ul[@class="feature clearfix"]'\
                            '/li[@class="full"]/span[@class="f-con"]/a/text()').extract()
        layer = res.xpath('//div[@class="clearfix ul-layer"]/ul[@class="feature clearfix"]/li'\
                          '/span[@class="f-con"]/text()').extract()
        numList = res.xpath('//div[@class="top-price fr"]/span[@class="price-num"]/text()').extract()
        #unitList = res.xpath('//div[@class="top-price fr"]/text()').extract()
        price = ''
        for i in range(len(numList)):
            #unit = unitList[i].replace('\&nbsp;', '').replace('0xc2', '').decode('utf-8')

            #print '___________________________unit:', unit
            price = numList[i]  #+ ' ' + unit
        print '************************price:', price
        print '************************name:', name
        print '************************city:', city
        print '************************address:', address
        if layer:
            print '************************layer:', layer[1]
        item['url'] = url
        item['name'] = name
        if city:
            item['city'] = city[0]
        else :
            item['city'] =city
        item['address'] = address
        if layer:
            item['layer'] = layer[1]
        else :
            item['layer'] = layer
        item['price'] = str(price)


        yield item

