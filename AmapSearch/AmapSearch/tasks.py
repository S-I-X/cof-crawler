# -*- coding:utf-8 -*-
from celery import task
import time
from views import dmapSearch
import requests
import json
import pymongo
from django.http import HttpResponse
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive"}


AmapSearchKey='1072a343e59f3ef2ddf864e0f2562359'

AmapCorpKey='2cb3455eaee1a9d0032879ca752d13a3'

headers = headers
myKey = AmapSearchKey
corpKey = AmapCorpKey
MONGO_HOST='192.168.10.31'
MONGO_PORT=27017

def insertMongoDb(MongoCollection, insertMapList):
    '''
    :param MongoCollection: 目标集合名
    :param insertMapList: 待插入的文档List，以dict为元素
    :return:
    '''
    MongoCollection.insert_many(insertMapList)

#通过调用高德API进行关键字搜索服务
@task
def build_job(request):
    keywords = request.GET.get('keywords')
    print("********keywords:", keywords)
    mongoClient = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
    db = mongoClient['amapSearch']
    collection = db['keySearch']
    url = ''.join(['http://restapi.amap.com/v3/place/text?key=', str(corpKey), '&keywords=', keywords,
                   '&types=&city=&children=&offset=&page=&extensions=all'])
    r = requests.get(url, headers=headers).content
    j = json.loads(r.decode('utf8'))

    print(j['pois'])

    insertMongoDb(collection, j['pois'])

    #return HttpResponse("<h1>successful</h1>")
