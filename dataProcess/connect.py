# coding:utf-8

import MySQLdb

class ConnSettings:
        def __init__(self):
                self.host='192.168.10.31'
                self.db='baidu_api'
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