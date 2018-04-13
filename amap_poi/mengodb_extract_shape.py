import csv

from amap_crawler_shape import aggregate_MongoDb
from process import *


def extract_shape():
    tabels = ['bazhoupois_admin', 'bazhoupois_hospital', 'bazhoupois_hotel', 'bazhoupois_life',
              'bazhoupois_officeBuild', 'bazhoupois_park', 'bazhoupois_recreations',
              'bazhoupois_research', 'bazhoupois_resident', 'bazhoupois_school']
    all_count = 0
    with open('amap_pois_shape.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 写入columns_name
        writer.writerow(['index', 'collection', 'collection_count', 'id', 'name', 'shape'])
        queryArgs = {'shape': {'$nin': ['']}}
        groupArgs = {'_id': {'id': '$id', 'name': "$name", 'shape': '$shape'}}
        for collection_name in tabels:
            conn = setConn('amap_pois', collection_name)
            results = aggregate_MongoDb(conn, queryArgs, groupArgs)
            count = 0
            for result in results:
                result = result['_id']
                count += 1
                all_count += 1
                writer.writerow([all_count, collection_name, count, result['id'], result['name'], result['shape']])
                # print(collection_name, count, result['id'], result['name'], result['shape'])
            print(f"{time_now(1)}\tTable:{collection_name}  Shape:{count}")
        print(f"\n{time_now(1)}\t\tAll Shape:{all_count}")
    return all_count


if __name__ == '__main__':
    extract_shape()
