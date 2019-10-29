import redis
from settings import REDIS_HOST, REDIS_PORT, REDIS_DB

class RedisHelp:
	def __init__(self):
		self.conn = redis.Redis(host = REDIS_HOST, port = REDIS_PORT, db = REDIS_DB)

	#添加记录
	def add_set_data(self,  data):    
		return self.conn.sadd("restaurant_id", data)

	#判断记录是否存在
	def is_member(self, value):
		return self.conn.sismember("restaurant_id", value)

	#获取所有数据集
	def get_all_data(self):

		return self.conn.smembers("restaurant_id")