# coding:utf-8
# 要使返回值为中文，需要设置请求头信息
import requests
import json
import Consts
import pymongo
import time


headers = Consts.headers
myKey = Consts.AmapSearchKey
corpKey = Consts.AmapCorpKey

def setConn():
    #获取数据库的连接
    mongoClient = pymongo.MongoClient('192.168.10.31', 27017)
    db = mongoClient['huhhte'] #数据库
    collection = db['huhhte_info']#数据表
    return collection

# 批量插入mongodb
def insertMongoDb(MongoCollection, insertMapList):
    '''
    :param MongoCollection: 目标集合名
    :param insertMapList: 待插入的文档List，以dict为元素
    :return:
    '''
    MongoCollection.insert_many(insertMapList)

def getInfo(key,pageNum):
    #访问高德API
    #通过关键字keywords进行搜索 返回json数据
    url = 'http://restapi.amap.com/v3/config/district?key=2cb3455eaee1a9d0032879ca752d13a3' \
          '&keywords=呼和浩特&subdistrict=3&extensions=base'
    print 'url:',url
    r = requests.get(url, headers=headers).content
    j = json.loads(r.decode('utf8'))
    if j['count'] != 0:
        rstList=j['districts']

        collection = setConn()
        insertMongoDb(collection, rstList)
        time.sleep(5)

        # 判断是否可递归
        if pageNum * 20 < float(j['count']):
            pageNum += 1
            getInfo(key,pageNum)
if  __name__=='__main__':
    #通过改变关键字，就可以实现对关键字的相应查询
    getInfo(myKey, 1)