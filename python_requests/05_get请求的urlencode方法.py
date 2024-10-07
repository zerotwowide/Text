# urlencode的应用场景：多个参数

# https://cn.bing.com/search?pglt=131&q=周杰伦&sex=男

import urllib.request
import urllib.parse

# 初始url
url = 'https://cn.bing.com/search?pglt=131&'

# url路径处理
data = {
    'q':'周杰伦',
    'sex':'男'
}
a = urllib.parse.urlencode(data)
url = url + a

# 请求对象的定制
headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
}
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器发送请求
response = urllib.request.urlopen(request)

# 获取数据
content = response.read().decode('utf-8')

# 打印数据
print(content)
