
# 获取明星（name）的网页源码

# https://cn.bing.com/search?pglt=131&q=周星驰

import urllib.request
import urllib.parse


url = 'https://cn.bing.com/search?pglt=131&q='

name = urllib.parse.quote('周杰伦')

url = url + name

headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
}


request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
