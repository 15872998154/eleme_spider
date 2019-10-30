import requests
import json
from mongo_utils import MongoHelp
from redis_utils import RedisHelp
import time 
import random

class WuhanShopSpider:
	def __init__(self, latitude = "", longitude = "", cookie = ""):
		self.mongo_handle = MongoHelp()  
		self.redis_handle = RedisHelp()
		self.latitude = "30.507612"
		self.longitude = "114.397851"
		self.cookie = "ubt_ssid=9iojnt64586grmdmmid6u14xz8uha0y6_2019-10-28; perf_ssid=ukns9lpxpgld7e0gva9fs7jj6s7zjnn8_2019-10-28; cna=pNgpFtGYmVkCAXWINNuscU5A; isg=BPT0Jn6YFZGoHoHduXkRFygoxrumZTN8FSLjHo5WN3-t-ZJDs9x1R8v4efGEGlAP; l=dBNA1Nw7q3BNwf1iBOfNcuIRXMbt2QdVhkPzw4ZI6ICP_x5OJCROWZQrer8pCn1Vns19W3u2coLyBo8FZz1L3taNr6ZFm7KiUp8h.; _utrace=ae4192682af2b15d9220c8adcc16388e_2019-10-28; ut_ubt_ssid=pff7h1w3prevpufv4t7zxc6xq5byeq8k_2019-10-28; UTUSER=143389539; track_id=1572249249|386106bf620a320bb1fecbbf6e4f072903fc2dcedcf2f262c8|06c6292029cdb83978690e08436ba108; USERID=143389539; SID=c1Mkb0wH3jyP7pcqCHFuY05GVVlyhwSbVjkg; ZDS=1.0|1572249249|DUrRByPW7TytTSZ7SgrkVrWqxe5eUlf+neGA4T56HDLNFb/MwOu05sozg9ItWpG2; tzyy=27caefd5592bb0ca84c0c1a42b6da956; pizza73686f7070696e67=aKonJFn5Q5TBxydFSWJGpiBmhOWjFOVmBOjsZD1Vum7pYBvm9S_Rrqar8J759t3m"
		self.headers = {
			"Host": "www.ele.me",
			"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
			"Accept": "application/json, text/plain, */*",
			"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
			"Accept-Encoding": "gzip, deflate, br",
			"x-shard": "loc='{},{}'.format(self.longitude, self.latitude)",    #114.397851 , 30.507612
			"Connection": "keep-alive",
			"Referer": "https://www.ele.me/place/wt3me1tzxph6?latitude=30.507612&longitude=114.397851",		
			"Cookie": self.cookie,
			"Cache-Control": "max-age=0",
			"TE": "Trailers",
		} 

	def save_shop_info(self):
		"""
		请求拿到Json数据后，redis判重，存储至mongo
		"""

		offset_set = [i for i in range(0, 500, 24)]
		for offset in offset_set:
			restaurant_url = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wt3me1tzxph6&latitude={}&limit=24&longitude={}&offset={}&restaurant_category_ids%5B%5D=-100&restaurant_category_ids%5B%5D=207&restaurant_category_ids%5B%5D=220&restaurant_category_ids%5B%5D=260&restaurant_category_ids%5B%5D=233&restaurant_category_ids%5B%5D=-102&restaurant_category_ids%5B%5D=-103&restaurant_category_ids%5B%5D=-104&restaurant_category_ids%5B%5D=-105&restaurant_category_ids%5B%5D=-107&restaurant_category_ids%5B%5D=-106&'.format(self.latitude, self.longitude, offset)
			res = requests.get(url = restaurant_url, headers = self.headers)
			
			#解析出服务端设置的cookie
			receive_cookie = str(res.headers['Set-Cookie'].split(";")[0])
			#拼凑新的cookie
			new_cookie = ';'.join(res.request.headers['Cookie'].split(";")[:-1]) + '; ' + receive_cookie
			#设置头部,下一次请求带上该头部信息
			self.headers['Cookie'] = new_cookie

			restaurant_set = json.loads(res.text)
			for i in range(len(restaurant_set)): 
				restaurant_id = restaurant_set[i]['id']
				
				# 判断该店铺信息是否已经在数据库中
				if self.redis_handle.is_member(restaurant_id):
					print("continue")
					continue
				
				#从json中解析数据
				restaurant_name = restaurant_set[i]['name']
				restaurant_image_path = restaurant_set[i]['image_path'] #img path
				restaurant_business_info = restaurant_set[i]['business_info'] #img path
				restaurant_opening_hours = ','.join(restaurant_set[i]['opening_hours'])
				restaurant_flavors = ','.join( [flavor['name'] for flavor in restaurant_set[i]['flavors']] )
				restaurant_rating = restaurant_set[i]['rating'] #综合评价
				restaurant_latitude = restaurant_set[i]['latitude']
				restaurant_longitude = restaurant_set[i]['longitude']
				restaurant_recent_order_num = restaurant_set[i]['recent_order_num']
				restaurant_promotion_info = restaurant_set[i]['promotion_info']

				#存储文档至mongodb
				document = {}
				document['restaurant_id'] = restaurant_id
				document['restaurant_name'] = restaurant_name
				document['restaurant_image_path'] = restaurant_image_path
				document['restaurant_business_info'] = restaurant_business_info
				document['restaurant_opening_hours'] = restaurant_opening_hours
				document['restaurant_flavors'] = restaurant_flavors
				document['restaurant_rating'] = restaurant_rating
				document['restaurant_latitude'] = restaurant_latitude
				document['restaurant_longitude'] = restaurant_longitude
				document['restaurant_recent_order_num'] = restaurant_recent_order_num
				document['restaurant_promotion_info'] = restaurant_promotion_info
				self.mongo_handle.insert(document)

				#将该店铺ID保存至redis中，表示该店铺信息已经在Mongo中
				self.redis_handle.add_set_data(restaurant_id)

				#日志
				print(restaurant_id)
				print(restaurant_name)
				print(restaurant_image_path)
				print(restaurant_business_info)
				print(restaurant_opening_hours)
				print(restaurant_flavors)
				print(restaurant_rating)
				print(restaurant_latitude)
				print(restaurant_longitude)
				print(restaurant_recent_order_num)
				print(restaurant_promotion_info)
				print("==" * 20)
			time.sleep(random.randint(6,8))
#12123
WuhanShopSpider().save_shop_info()
