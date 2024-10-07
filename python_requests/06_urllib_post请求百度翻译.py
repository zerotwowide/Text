
import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
}

data = {
    'kw':'love'
}

# post请求的参数 必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# 定制请求对象
request = urllib.request.Request(url=url, data=data, headers=headers)

# 发送请求
response = urllib.request.urlopen(request)

# 获取信息
content = response.read().decode('utf-8')

# 转译
obj = json.loads(content)
print(obj)