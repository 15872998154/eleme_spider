import requests
import json

headers = {
	"Host": "www.ele.me",
	"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
	"Accept": "application/json, text/plain, */*",
	"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	"Accept-Encoding": "gzip, deflate, br",
	"x-shard": "loc=114.397851,30.507612",
	"Connection": "keep-alive",
	"Referer": "https://www.ele.me/place/wt3me1tzxph6?latitude=30.507612&longitude=114.397851",		
	"Cookie": "ubt_ssid=9iojnt64586grmdmmid6u14xz8uha0y6_2019-10-28; perf_ssid=ukns9lpxpgld7e0gva9fs7jj6s7zjnn8_2019-10-28; cna=pNgpFtGYmVkCAXWINNuscU5A; isg=BPT0Jn6YFZGoHoHduXkRFygoxrumZTN8FSLjHo5WN3-t-ZJDs9x1R8v4efGEGlAP; l=dBNA1Nw7q3BNwf1iBOfNcuIRXMbt2QdVhkPzw4ZI6ICP_x5OJCROWZQrer8pCn1Vns19W3u2coLyBo8FZz1L3taNr6ZFm7KiUp8h.; _utrace=ae4192682af2b15d9220c8adcc16388e_2019-10-28; ut_ubt_ssid=pff7h1w3prevpufv4t7zxc6xq5byeq8k_2019-10-28; UTUSER=143389539; track_id=1572249249|386106bf620a320bb1fecbbf6e4f072903fc2dcedcf2f262c8|06c6292029cdb83978690e08436ba108; USERID=143389539; SID=c1Mkb0wH3jyP7pcqCHFuY05GVVlyhwSbVjkg; ZDS=1.0|1572249249|DUrRByPW7TytTSZ7SgrkVrWqxe5eUlf+neGA4T56HDLNFb/MwOu05sozg9ItWpG2; tzyy=27caefd5592bb0ca84c0c1a42b6da956; pizza73686f7070696e67=aKonJFn5Q5TBxydFSWJGpiBmhOWjFOVmBOjsZD1Vum7pYBvm9S_Rrqar8J759t3m",
	"Cache-Control": "max-age=0",
	"TE": "Trailers",
}

restaurant_url = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wt3me1tzxph6&latitude=30.507612&limit=24&longitude=114.397851&offset=0&restaurant_category_ids%5B%5D=-100&restaurant_category_ids%5B%5D=207&restaurant_category_ids%5B%5D=220&restaurant_category_ids%5B%5D=260&restaurant_category_ids%5B%5D=233&restaurant_category_ids%5B%5D=-102&restaurant_category_ids%5B%5D=-103&restaurant_category_ids%5B%5D=-104&restaurant_category_ids%5B%5D=-105&restaurant_category_ids%5B%5D=-107&restaurant_category_ids%5B%5D=-106&'
res = requests.get(restaurant_url,  headers = headers)
print(res.headers)
receive_cookie = str(res.headers['Set-Cookie'].split(";")[0])
new_cookie = ';'.join(res.request.headers['Cookie'].split(";")[:-1]) + '; ' + receive_cookie



# print()

# restaurant_url1 = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wt3me1tzxph6&latitude=30.507612&limit=24&longitude=114.397851&offset=0&restaurant_category_ids%5B%5D=-100&restaurant_category_ids%5B%5D=207&restaurant_category_ids%5B%5D=220&restaurant_category_ids%5B%5D=260&restaurant_category_ids%5B%5D=233&restaurant_category_ids%5B%5D=-102&restaurant_category_ids%5B%5D=-103&restaurant_category_ids%5B%5D=-104&restaurant_category_ids%5B%5D=-105&restaurant_category_ids%5B%5D=-107&restaurant_category_ids%5B%5D=-106&'

headers['Cookie'] = new_cookie

restaurant_url1 = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wt3me1tzxph6&latitude=30.507612&limit=24&longitude=114.397851&offset=24&restaurant_category_ids%5B%5D=-100&restaurant_category_ids%5B%5D=207&restaurant_category_ids%5B%5D=220&restaurant_category_ids%5B%5D=260&restaurant_category_ids%5B%5D=233&restaurant_category_ids%5B%5D=-102&restaurant_category_ids%5B%5D=-103&restaurant_category_ids%5B%5D=-104&restaurant_category_ids%5B%5D=-105&restaurant_category_ids%5B%5D=-107&restaurant_category_ids%5B%5D=-106&'
res = requests.get(restaurant_url1, headers = headers)
restaurant_set = json.loads(res.text)
print(restaurant_set[0]['name'])

for i in range(len(restaurant_set)): 
	print(restaurant_set[i]['name'])
# res = s.get(restaurant_url1)
# print(res.request.headers)








# ubt_ssid=9iojnt64586grmdmmid6u14xz8uha0y6_2019-10-28; 
# perf_ssid=ukns9lpxpgld7e0gva9fs7jj6s7zjnn8_2019-10-28; 
# cna=pNgpFtGYmVkCAXWINNuscU5A; 
# isg=BHd3GRVs5vY0ZWJ0PmiijgdpBWIBlGBVasOA98kk-saseJa60Q2C7kUeWhiDiyMW; 
# l=dBNA1Nw7q3BNw-18BOCZmuIRXMbTGIObYuPRwkZki_5w46Yiez7OkNB1XFv6csWAGo8B4q-bDUyt4eXzP12VhP7lOkS0wrM2B; 
# _utrace=ae4192682af2b15d9220c8adcc16388e_2019-10-28; 
# ut_ubt_ssid=pff7h1w3prevpufv4t7zxc6xq5byeq8k_2019-10-28; 
# UTUSER=143389539; 
# track_id=1572249249|386106bf620a320bb1fecbbf6e4f072903fc2dcedcf2f262c8|06c6292029cdb83978690e08436ba108; 
# USERID=143389539; 
# SID=c1Mkb0wH3jyP7pcqCHFuY05GVVlyhwSbVjkg; 
# ZDS=1.0|1572249249|DUrRByPW7TytTSZ7SgrkVrWqxe5eUlf+neGA4T56HDLNFb/MwOu05sozg9ItWpG2; 
# dBNA1Nw7q3BNw-18BOCZmuIRXMbTGIObYuPRwkZki_5w46Yiez7OkNB1XFv6csWAGo8B4q-bDUyt4eXzP12VhP7lOkS0wrM2B
# tzyy=27caefd5592bb0ca84c0c1a42b6da956; 
# pizza73686f7070696e67=CPuz42fVoxnRVcVQ1x33fXWEt-wpJWmRyNXYD1JXbl8QLbJyC5mt2L6fBaNO0Wzj
