# -*- coding: utf-8 -*-
import pymongo
from items import *
client = pymongo.MongoClient('192.168.10.31', 27017)
class SchoolPipeline(object):
    def __init__(self):
        db=client['school']
        self.hotelDetail = db['schoolDetail']
    def process_item(self, item, spider):
        if isinstance(item, SchoolItem):
            self.hotelDetail.insert(dict(item))
