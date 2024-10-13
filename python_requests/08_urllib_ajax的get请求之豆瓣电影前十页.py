import urllib.request
import urllib.parse
from idlelib.iomenu import encoding

'''
https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&
start=0&limit=20

https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&
start=20&limit=20

https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&
start=40&limit=20

'''

def creat_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&'

    data = {
        'start':(page - 1) * 20,
        'limit':20,
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
    }

    request = urllib.request.Request(url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def download(page,content):
    # 使用 + 进行数据的拼接时，+ 两端都需要是字符串类型，因此这里 page 需要进行强制数据转换
    with open('douban_' + str(page) + '.json','w',encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    start_page = int(input("请输入开始的页码："))
    end_page = int(input("请输入结束的页码："))

    for page in range(start_page, end_page + 1):
        # 请求对象的定制
        request = creat_request(page)
        # 模拟浏览器发送请求
        content = get_content(request)
        # 下载数据
        download(page,content)