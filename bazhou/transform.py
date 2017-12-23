# conding:utf-8
from Consts import ConnSettings as settings
from AmapSearch import setConn
sets = settings()
conn = sets.getConn()
con = setConn()

#将mongodb中的数据转存于mysql中
def insertInfo(d):
    print 'd:', d
    insertSql = 'insert into huhhte (name,level,adcode,citycode,center) value (%s,%s,%s,%s,%s)'
    cursor = conn.cursor()
    name = d['name']
    level = d['level']
    adcode = d['adcode']
    citycode = d['citycode']
    center = d['center']
    cursor.execute(insertSql, (name, level, adcode, citycode, center))
    conn.commit()
    if d['districts']:
        print 'd[\'districts\']:', d['districts']
        for k in d['districts']:
            insertInfo(k)

#从mongodb中获取数据
def getInfo_fromMongo():
    data = con.find({})
    for r in data:
        print r['districts']
        for dt in r['districts']:
            print 'dt:', dt
            if dt['districts']:
                insertInfo(dt)


if __name__ == '__main__':
    getInfo_fromMongo()






