# -*- coding: utf-8 -*-
import pymongo
from items import *
client = pymongo.MongoClient('192.168.10.31', 27017)
class HotelPipeline(object):
    def __init__(self):
        db=client['hotel']
        self.hotelDetail = db['hotelDetail']
    def process_item(self,item,spider):
        if isinstance(item,hotelItem):
            self.hotelDetail.insert(dict(item))
