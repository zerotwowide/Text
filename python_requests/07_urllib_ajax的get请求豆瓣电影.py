
# get 请求
# 获得豆瓣第一页数据

import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
}

# 定制请求对象
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器发送请求
response = urllib.request.urlopen(request)

# 接收数据
content = response.read().decode('utf-8')
# print(content)

# 下载数据到本地
file = open('douban.json','w',encoding='utf-8')
file.write(content)