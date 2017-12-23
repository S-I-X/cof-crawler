# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
import requests, json
from scrapy.http import Request
import re
from lxml import etree
from hotel.items import *
from hotel.middlewares import *

class hotelSpider(CrawlSpider):
    name='HotelSpider'
    download_delay=5
    custom_settings={'ITEM_PIPELINES':{'hotel.pipelines.HotelPipeline':200}}
    mainUrl='http://hotels.ctrip.com'
    start_url='http://hotels.ctrip.com/domestic-city-hotel.html'
    nameList=[]
    addressList=[]
    priceList=[]
    t=0
    def start_requests(self):
        url=self.start_url
        yield Request(url=url,callback=self.parse)
    def parse(self,response):
        res=Selector(response)
        item=hotelItem()
        urlList=res.xpath('//dl[@class="pinyin_filter_detail layoutfix"]/dd/a/@href').extract()
        for u in urlList:
            self.nameList=[]
            self.addressList=[]
            self.priceList=[]
            self.t=0
            l=u.split('/')
            cityPY=re.sub('\d','',l[len(l)-1])
            cityId=re.sub('\D','',l[len(l)-1])
            page=1
            url="http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx?cityId=%s&cityPY=%s&page=%d" %(cityId,cityPY,page)
            print ('****************************************************url:',url)
            r = requests.get(url).content
            print type(r)
            j = json.loads(r.decode('utf8'))
            total=j['hotelAmount']
            print ('****************************************************total:',total)
            if total%25==0:
                self.t=total/25
            else:
                self.t=total/25+1
            while page<=self.t:
                if (cityId=='1'  and cityPY=='beijing' and (page == 8 or page == 43)) or (cityPY='baishan'):
                    page +=1
                url="http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx?cityId=%s&cityPY=%s&page=%d" %(cityId,cityPY,page)
                #url="http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx?cityId=3886&cityPY=baishan&page=1"
                r = requests.get(url=url).content
                j = json.loads(r.decode('utf8'))
                total=j['hotelAmount']
                pageContent=etree.HTML(j['hotelList'])
                name_List=pageContent.xpath('//li[@class="hotel_item_name"]/h2[@class="hotel_name"]/a/@title')
                for j in range(len(name_List)):
                    self.nameList +=[re.sub('<[\s\S]+?>','',name_List[j])]
                    print ('***************************************************name_List[%d]' %(j),name_List[j])
                address_List=pageContent.xpath('//li[@class="hotel_item_name"]/p[@class="hotel_item_htladdress"]')
                for j in range(len(address_List)):
                    self.addressList +=[address_List[j].xpath("string(.)").replace("/&nbsp;/&nbsp","")]
                    print ('***************************************************address_List[%d]' %(j),address_List[j])
                price_List=pageContent.xpath('//span[@class="J_price_lowList"]/text()')
                for j in range(len(price_List)):
                    self.priceList +=[re.sub('<[\s\S]+?>','',price_List[j])]
                    print ('***************************************************price_List[%d]' %(j),price_List[j])
                page +=1
            for k in range(len(self.nameList)):
                print ("*****************************len(nameList):",len(self.nameList))
                item['name']=self.nameList[k]
                print ("*********************************************name:",k,self.nameList[k])
                item['address']=self.addressList[k]
                print ("*********************************************address:",k,self.addressList[k])
                item['price']=self.priceList[k]
                print ("*********************************************price:",k,self.priceList[k])
                yield item


