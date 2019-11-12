import redis
from settings import REDIS_HOST, REDIS_PORT, REDIS_DB
import hashlib

class RedisHelp:
	def __init__(self):
		self.conn = redis.Redis(host = REDIS_HOST, port = REDIS_PORT, db = REDIS_DB)

	#添加记录
	def add_set_data(self, value):
		m = hashlib.md5()
		m.update(value.encode(encoding = 'utf-8'))   
		return self.conn.sadd("restaurant_id", m.hexdigest())

	#判断记录是否存在
	def is_member(self, value):
		m = hashlib.md5()
		m.update(value.encode(encoding='utf-8'))   
		return self.conn.sismember("restaurant_id", m.hexdigest())

	#获取所有数据集
	def get_all_data(self):

		return self.conn.smembers("restaurant_id")