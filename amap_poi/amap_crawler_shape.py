from amap_poi.process import *


def select_MongoDb(MongoCollection, queryArgs, projectionFields=None):
    results = MongoCollection.find(queryArgs, projection=projectionFields)
    return results


def aggregate_MongoDb(MongoCollection, queryArgs, groupArgs):
    results = MongoCollection.aggregate([{"$match": queryArgs}, {"$group": groupArgs}])
    return results


def update_MongoDb(MongoCollection, filterArgs, updateArgs):
    updateRes = MongoCollection.update_many(filter=filterArgs, update=updateArgs)
    return updateRes


# 批量插入mongodb
def insert_MongoDb(MongoCollection, insertMapList):
    '''
    :param MongoCollection: 目标集合名
    :param insertMapList: 待插入的文档List，以dict为元素
    :return:
    '''
    MongoCollection.insert_many(insertMapList)


def add_shape():
    collections = ['bazhoupois_admin', 'bazhoupois_hospital', 'bazhoupois_hotel', 'bazhoupois_life',
                   'bazhoupois_officeBuild', 'bazhoupois_park', 'bazhoupois_recreations',
                   'bazhoupois_research', 'bazhoupois_resident', 'bazhoupois_school']
    counts = up_nums = 0
    for collection_name in collections:
        conn = setConn('amap_pois', collection_name)
        queryArgs = {'shape': None}
        groupArgs = {"_id": "$id"}
        results = aggregate_MongoDb(conn, queryArgs, groupArgs)
        count = up_num = 0
        for result in results:
            # print(result)
            count += 1
            poi_id = result['_id']
            try:
                shape = getInfo(poi_id)
                filterArgs = {'shape': None, 'id': poi_id}
                updateArgs = {'$set': {'shape': shape}}
                update = update_MongoDb(conn, filterArgs, updateArgs)
                up_num += update.modified_count
                # print(count, up_num, update.matched_count, update.modified_count, result['_id'], shape)
            except:
                print(f"{time_now(1)}\t\t{count} {result['_id']} Update Error!")
        update = update_MongoDb(conn, {'shape': None}, {'$set': {'shape': ''}})
        print(f"{time_now(1)}\t\tFix: matched_count:{update.matched_count},  modified_count:{update.modified_count}")
        print(f"{time_now(1)}\t\tTable:{collection_name}  POI:{count}  Update:{up_num}\n\n")
        counts += count
        up_nums += up_num
    print(f"{time_now(1)}\t\tCompleted!  All POI:{counts}  All Update:{up_nums}")
    return counts, up_nums


if __name__ == '__main__':
    add_shape()
