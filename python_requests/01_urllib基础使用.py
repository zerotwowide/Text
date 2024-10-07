# 使用urllib获取网站首页的源码
import urllib.request

# first 定义一个url   就是要访问的网址
url = 'https://www.cbjq.com'

# two 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# third 获取响应中的源码
content = response.read().decode("utf-8")

# four 打印数据
print(content)