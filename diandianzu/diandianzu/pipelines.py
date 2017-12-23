# -*- coding: utf-8 -*-

import pymongo
from items import *
client = pymongo.MongoClient('192.168.10.31', 27017)
class HousePipeline(object):
    def __init__(self):
        db=client['diandianzu']
        self.hotelDetail = db['houseDetail']
    def process_item(self,item,spider):
        if isinstance(item, HouseItem):
            self.hotelDetail.insert(dict(item))
