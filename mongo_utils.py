from pymongo import MongoClient
from settings import MONGO_HOST,MONGO_PORT, MONGO_DB_NAME, MONGO_COLLECTION_NAME

class MongoHelp(object):
    """
    mongodb增删改查的操作
    """
    client = MongoClient(host = MONGO_HOST, port = 27017)
    col = client[MONGO_DB_NAME][MONGO_COLLECTION_NAME]

    @classmethod
    def insert(cls, data,flg=True):
        """添加数据"""
        if flg:
            if isinstance(data, dict):  # 插入一条数据
                ret = cls.col.insert_one(data)
                
                return ret

        elif isinstance(data, list):  # 插入多条数据
            for i in data:
                if not isinstance(i, dict):
                    return "数据格式有误"
            ret = cls.col.insert_many(data)
            return ret
        else:
            return "数据格式为dict或者[{},{}]形式的列表但你传入的是%s," % type(data)

    @classmethod
    def find(cls, data, flg=True):
        """查找数据"""
        try:
            if flg:
                rt = cls.col.find_one(data)  # 查一条数
                return rt
            else:
                rt = cls.col.find(data)  # 查多条数据
                result = []
                for i in rt:
                    result.append(i)
                return result
        except Exception:
            return "查询数据格式有误"

    @classmethod
    def update(cls, org_data, new_data, flg=True): # flg = True  只更新一条
        """更新数据"""
        if flg:
            ret = cls.col.update_one(org_data, {"$set": new_data})  # 之更细一条
            return ret

        else:
            ret = cls.col.update_many(org_data, {"$set": new_data})  # 更新全部数据
            return ret

    @classmethod
    def delete(cls, data, flg=True):
        """删除数据"""
        if flg:
            ret = cls.col.delete_one(data)  # 删除一条
            return ret
        else:
            ret = cls.col.delete_many(data)  # 删除全部
            return ret

# db.getCollection('wuhan').aggregate([
#     { $group: { _id : '$restaurant_name', count: { $sum : 1 } } },
#     { $match: { count: { $gt : 1} } }
# ])

