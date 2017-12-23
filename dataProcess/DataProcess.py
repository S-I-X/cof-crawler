# coding:utf-8

import json
from connect import  ConnSettings 
from _sqlite3 import Cursor
from test.pickletester import __main__

setting=ConnSettings()
conn=setting.getConn()
cursor=conn.cursor()

def setConnParams(): 
    setting.setDB('baidu_api')
    setting.setHost('192.168.10.31')
    setting.setPassword('123456')
    setting.setPort('3306')
    setting.setUserName('dingsa')
    
def getConn(setting):
    return setting.getConn()

def getContent():
    selectSQL='select uid,enclose,shape from baidu_house'  #city,fang_id,name,address, location,geo_string,
    updateSQL='update baidu_house set shape=%s where uid=%s'
   
    cursor.execute(selectSQL)
    fangContentList=cursor.fetchall()
    encloseList=[(s[0],s[1],s[2]) for s in fangContentList]
#     print 'enclose:',encloseList
    #enclose=json.loads(encloseList)
    for t in encloseList:
       # print t[0]
        if(t[1]!='not found' and t[1]!='del' and t[2]==''):
            t_enclose=json.loads(t[1])
            l=''
            for r in t_enclose['result']:
                l =l + str(r['x']) +',' +str(r['y']) +';'
               # print l
            print l
            cursor.execute(updateSQL,(l,t[0]))
            conn.commit()
                
#     for f in fangContentList:
#         i=0
#         while(i<len(f)):
#             if(f[7]!=None):
#                 print i,f[i]
#                 i=i+1
   # print fangContentList
    
if __name__ == '__main__':
    getContent()