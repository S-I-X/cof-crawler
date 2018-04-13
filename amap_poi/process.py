import json
import time

import pymongo
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive"}

# 个人用户key
AmapSearchKey = '1072a343e59f3ef2ddf864e0f2562359'
# 企业用户key,元力云公司企业开发者
AmapCorpKey = '2cb3455eaee1a9d0032879ca752d13a3'

BaiduKey = 'MNpMOzQYiGntOT7ppYsrvGFm9YG0eNHv'

MONGO_HOST = '192.168.10.31'
MONGO_PORT = 27017


def setConn(db_name, table_name, host=MONGO_HOST, port=MONGO_PORT):
    # 获取数据库的连接
    mongoClient = pymongo.MongoClient(host, port)
    db = mongoClient[db_name]  # 数据库
    collection = db[table_name]  # 数据表
    print(f"{time_now(1)}\t\tConnect Successful: Database:{db_name},  Table:{collection_name}")
    # time.sleep(5)
    return collection


def getInfo(id):
    # 访问高德API
    # 通过关键字keywords进行搜索 返回json数据
    url = 'https://ditu.amap.com/detail/get/detail?id=' + id
    # print('url:', url)
    r = requests.get(url, headers=headers).content
    j = json.loads(r.decode('utf8'))
    # print(json.dumps(j, sort_keys=True, indent=2))
    try:
        shape = j['data']['spec']['mining_shape']['shape']
    except:
        shape = ''
    # print(shape)
    return shape


def time_now(type_int=0):
    """
    函数功能：匹配时间段重叠情况。
    时间格式统一为‘1995-4-16’。
    :param type_int: 时间类型，0：'1995-4-16'，1：'Sun Apr 16 6:6:6 1995'
    :return: 请求的格式化时间
    """
    if type_int == 0:
        return str(time.localtime(time.time()).tm_year) + '-' + str(time.localtime(time.time()).tm_mon) + '-' \
               + str(time.localtime(time.time()).tm_mday)
    if type_int == 1:
        return time.asctime(time.localtime(time.time()))
