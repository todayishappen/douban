# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse   # 解析器
'''
# get方式获得网页请求
# 用response接收获得的request请求
response = urllib.request.urlopen("http://www.baidu.com")
print(response)  # 获得是一个请求到的对象
print(response.read())      # 获得response的具体内容，但存在包含\n在内的转义字符等编码
print(response.read().decode('utf-8')),   # 将获得到的页面内容进行解码，这样会获得和页面源代码相同的内容
'''
'''
# 获得一个post请求
# 单独的post是无法直接进行访问请求的，必须将post请求进行封装，变成表单信息才能进行访问。
# 封装：使用一个列表等等，此时例如放着是二进制信息包
data = bytes(urllib.parse.urlencode({'hello': 'world'}), encoding='utf-8')  # 键值对
response = urllib.request.urlopen('http://httpbin.org/post', data=data) # 传递的参数为字节文件
print(response.read().decode('utf-8'))
'''

'''
# 超时timeout,常用于在爬取页面时防止一直等待，必要
# 利用get请求
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)  # timeout键显示超时。1代表一秒，这里保证健壮性用try,except
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print('time out!')
'''

'''
response = urllib.request.urlopen('http://httpbin.org/get')
print(response.status)  # 200状态码  ，  418 ：对方发现为爬虫
print(response.getheaders())  # 可以获得响应头，
print(response.getheader("Server"))  # 可以加单独的参数获取单独的内容,但header就为单数，即getheader（）
'''

'''
# 在页面中正式爬取内容时网站可能会识破爬虫程序报418错误
# 所以需要进行伪装，urlopen（）方法已经无法进行，这里利用Request对象封装，对象首字母为大写。
url = "http://httpbin.org/post"
headers={   #利用在页面上network到的user-agent将其封装到字典中成为键值对
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}
data= bytes(urllib.parse.urlencode({'name':'xiaowang'}),encoding='utf-8')
req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')  # 严格区分大小写
#上述是完成了req对象的创建，还需要reponse进行接收响应
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
'''


# 最后伪装测试豆瓣网站，不显示418
url='http://douban.com'
headers={   #利用在页面上network到的user-agent将其封装到字典中成为键值对
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}
req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode('utf-8'))