# -*- coding: utf-8 -*-
import MySQLdb

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive"}

# 个人用户key
AmapSearchKey='1072a343e59f3ef2ddf864e0f2562359'
# 企业用户key,元力云公司企业开发者
AmapCorpKey='2cb3455eaee1a9d0032879ca752d13a3'

BaiduKey='MNpMOzQYiGntOT7ppYsrvGFm9YG0eNHv'

MONGO_HOST='192.168.10.31'
MONGO_PORT=27017

#数据库得连接配置
class ConnSettings:
        def __init__(self):
                self.host='192.168.10.31'
                self.db='liugm_amap_api'
                self.port=3306
                self.username='dingsa'
                self.password='123456'


        # @property.setter
        def setHost(self,serverIP):
                self.host=serverIP

        # @property.setter
        def setPort(self,portNum):
                self.port=portNum

        # @property.setter
        def setUserName(self,username):
                self.username=username

        # @property.setter
        def setPassword(self,passwd):
                self.password=passwd

        # @property.setter
        def setDB(self,DBname):
                self.db=DBname

        def getConn(self):
                return MySQLdb.connect(host=self.host,db=self.db,port=self.port,
                                    user=self.username,passwd=self.password,charset='utf8')


