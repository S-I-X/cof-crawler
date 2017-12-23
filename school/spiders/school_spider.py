# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from school.items import SchoolItem
import sys


class schoolSpider(CrawlSpider):
    name = 'SchoolSpider'
    download_delay = 5
    custom_settings = {'ITEM_PIPELINES': {'school.pipelines.SchoolPipeline': 200}}
    mainUrl = 'http://www.xuexiaodaquan.com/'
    start_url = 'http://www.xuexiaodaquan.com/'
    nameList = []
    addressList = []
    url =''
    def start_requests(self):
        url = self.start_url
        yield Request(url=url, callback=self.parse_page)
    def parse_page(self,response):
        res = Selector(response)
        urlList = res.xpath('//div[@class="city-all"]/dl/dd/a/@href').extract()

        for u in urlList:
            yield Request(url=u, callback=self.parse)
    def parse(self, response):
        res = Selector(response)
        self.url = response.url
        print '**************************response.url:', self.url
        urlList = res.xpath('//div[@class="nav-drop nav-drop-index"]/ul/li/p[@class="drop-title"]/a/@href').extract()

        for u in urlList:
            yield Request(url=u, callback=self.parse_detail)

    def parse_detail(self, response):
        res = Selector(response)
        item = SchoolItem()
        self.nameList = self.nameList + res.xpath('//div[@class="list-xx clearfix"]/dl[@class="left"]/dd/p/a/text()').extract()
        self.addressList = self.addressList + \
            [res.xpath('//div[@class="list-xx clearfix"]/dl[@class="right"]/dd/ul/li/span/text()').extract()[0]]
        pageUrl = res.xpath('//div[@class="list-pages-c"]/ul/a[@class="next"]/@href').extract()

        if pageUrl:
            url = self.url + pageUrl[0]
            print '************************url:', url
            yield Request(url=url, callback=self.parse_detail)  #pageUrl需要拼接

        for i in range(len(self.nameList)):
            item['url'] = response.url
            item['name'] = self.nameList[i]
            item['address'] = self.addressList[i]
            yield item



