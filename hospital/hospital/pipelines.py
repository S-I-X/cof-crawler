# -*- coding: utf-8 -*-
'''
Created on 2017��10��19��

@author: sangfor
'''
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from items import *
import pymongo



class DB_conn(object):
     dbpool = adbapi.ConnectionPool('MySQLdb',
                                    host='192.168.10.31',
                                    port=3306,
                                    db='liugm_amap_api',
                                    user='dingsa',
                                    passwd='123456',
                                    cursorclass=MySQLdb.cursors.DictCursor,
                                    charset='utf8',
                                    use_unicode=True)
                                    
class HospitalPipeline(object):
     def process_item(self,item,spider):
         if  isinstance(item,hospitalItem):
             DB_conn.dbpool.runInteraction(self._hospital_insert,item)
         elif  isinstance(item,hospitalDetailItem):
             DB_conn.dbpool.runInteraction(self._detail_insert,item)
         return item
        
     def _hospital_insert(self,tx,item):
         sql='insert ignore into hospital (name,url) value (%s,%s)'
         print len(item['name'])
         if len(item['name']):
             for i in range(len(item['name'])):
                 tx.execute(sql,(item['name'][i],item['url'][i]))
     def _detail_insert(self,tx,item):
         
         print item['nickname'][0],item['property'][0],item['rank'][0],item['tel'][0],item['address'][0]
         sql='insert ignore into detailHospital (nickname,property,rank,tel,address,url) value (%s,%s,%s,%s,%s,%s)'
         tx.execute(sql,(item['nickname'][0],item['property'][0],item['rank'][0],item['tel'][0],item['address'][0],item['url'][0]))
                 
                 
                 
                 