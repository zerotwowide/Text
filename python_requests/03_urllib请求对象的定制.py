import urllib.request

url = 'https://www.cbjq.com'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
}
# 因为urlopen不能存储字典，因此需要进行请求对象的定制
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 发送请求
response = urllib.request.urlopen(request)

# 获取源码
content = response.read().decode('utf-8')

# 打印
print(content)