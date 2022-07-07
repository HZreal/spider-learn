# pymongo tutorial  and   API document


import bson
import pymongo
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from pymongo import InsertOne, DeleteOne, ReplaceOne
from pymongo import IndexModel

# 一、连接器
# client = MongoClient()
# client = MongoClient('mongodb://192.168.197.129:27017')
client = MongoClient('mongodb://192.168.197.129:27017', username='hz', password='root123456')    # 根据mongo服务器的配置，需认证
# 选择数据库
# db1 = client['python']
db = client.get_database('test')

# 二、数据库  https://pymongo.readthedocs.io/en/stable/api/pymongo/database.html
# 查看数据库的集合
# coll_obj = db.list_collections()  # 返回游标对象CommandCursor
# coll_list = db.list_collection_names()  # 返回集合名列表
# print(coll_obj, coll_list)
# 选择集合
# collection1 = db1['collec']
# collection = db.get_collection('collec')
collection = db.get_collection('col_1')
# 创建集合
# db.create_collection(name='col_1')
# db.create_collection(name='wangyi')
# 删除集合
# db.drop_collection(name_or_collection='')
# 在数据库监听更改
# db.watch()  # 返回DatabaseChangeStream cursor，可迭代数据库中集合的改变
# with db.watch() as stream:
#     for change in stream:
#         print(change)
# 例如监听插入改变
# try:
#     with db.watch([{'$age': {'operationType': 'insert'}}]) as stream:
#         for insert_change in stream:
#             print(insert_change)
# except PyMongoError:
#     logging.error('insert change error--------')


# 三、集合
# 获取集合名
# collection_name = collection.name      # collec
# collection_full_name = collection.full_name    # test.collec
# 集合所在数据库
# belong_db = collection.database
# 执行多个写操作
# collection.bulk_write(requests=[])
# multi_requests = [InsertOne({'x': 1, 'y': 2}), DeleteOne({'x': 1}), ReplaceOne({'z': 1}, {'z': 4}, upsert=True)]
# result_1 = collection.bulk_write(multi_requests)
# print(result_1)
# inserted_count_1 = result_1.inserted_count
# deleted_count_1 = result_1.deleted_count
# modified_count_1 = result_1.modified_count
# upserted_count_1 = result_1.upserted_count
# upserted_ids_1 = result_1.upserted_ids

# 插入单个文档
inserted_id = collection.insert_one({'name': 'huang', 'hometown': 'hubei', 'age': 24, 'gender': True}).inserted_id
# 插入批量文档
# inserted_ids = collection.insert_many([{'name': 'fff', 'age': 25},
#                                        {'name': 'ggg', 'age': 22},
#                                        {'name': 'hhh', 'age': 29},
#                                        ]).inserted_ids
# 替换单个文档(upsert=True表示不存在则创建)
# result_2 = collection.replace_one({'age': 22}, {'age': 26}, upsert=True)
# matched_count_2 = result_2.matched_count
# modified_count_2 = result_1.modified_count
# 更新单个文档
# result_3 = collection.update_one({'age': 21}, {'$inc': {'age': 25}})
# matched_count_3 = result_2.matched_count
# modified_count_3 = result_1.modified_count
# 更新多个文档
# collection.update_many({})
# 删除单个文档
# collection.delete_one()
# 删除多个文档
# collection.delete_many()

# 在集合中监听更改
# with collection.watch() as stream:
#     for change in stream:
#         print(change)
# 例如监听插入改变
# try:
#     with db.watch([{'$age': {'operationType': 'insert'}}]) as stream:
#         for insert_change in stream:
#             print(insert_change)
# except PyMongoError:
#     logging.error('insert change error--------')


# 查询文档
# res_Cursor = collection.find()  # 返回游标对象(可迭代)
# print(res_Cursor)
# for doc in res_Cursor:
#     print(doc)
# batch_cursor = collection.find_raw_batches()   # 类似于find() 但返回RawBatchCursor
# print(batch_cursor)
# for batch in batch_cursor:
#     print(bson.decode_all(batch))
# 查询一条
# res_one = collection.find_one()
# print(res_one)
# 查询一条并替换/更新/删除
# collection.find_one_and_replace()
# collection.find_one_and_update()
# collection.find_one_and_delete()
# 去重
# collection.distinct(key='', filter=None)

# 文档数量(可条件过滤)
# count = collection.count_documents({})
# print(count)
# count2 = collection.count_documents({'name': 'huang'})
# print(count2)

# 排序
# ree = collection.find({'age': {'$gt': 18}}).sort('age')
# for r in ree:
#     print(r)

# 索引
# 创建索引
# collection.create_index(keys=['age', pymongo.ASCENDING], unique=True)
# 为多个字段创建索引
# collection.create_index([
#     ('age', pymongo.DESCENDING),
#     ('hometown', pymongo.TEXT),
# ])
# 通过索引模型类创建一个或多个索引
# index1 = IndexModel([('hello', pymongo.ASCENDING), ('world', pymongo.DESCENDING)], name='hello_world')
# index2 = IndexModel([('goodbye', pymongo.DESCENDING)])
# index_list = collection.create_indexes([index1, index2])
# 删除索引
# collection.drop_index(index_or_name='')
# collection.drop_indexes()
# 索引信息
# collection.index_information()
# collection.list_indexes()


# 集合重命名
# collection.rename(new_name='')
# 删除集合
# collection.drop()



