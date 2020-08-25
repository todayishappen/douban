# -*-coding:utf-8-*-
# 解决乱码问题
# 2020.08.08
# 学习爬虫
# 首先加入格式语言、
import sys
from bs4 import BeautifulSoup   #网页解析
import re  #正则 表达式，文字匹配
import xlwt    #进行excel操作
import urllib.request,urllib.error  #制定url，获取网页数据
import sqlite3   #进行sqlite3操作
'''
P爬虫的思路：
1、获取url路径
2、逐一爬取数据
3、保存到本地文件
'''
def main():
    baseurl="https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    savePath = ".//豆瓣数据.xls"
    # saveData(savePath)
    askURL("https://movie.douban.com/top250?start=")

#进入网页后把网页中的想要爬取的内容参数放入到集合中
def getData(baseurl):
    datalist=[]
    for i in range(0,10):
        # 1、获取网页内容
        url=baseurl+str(i*25)
        html=askURL(url)  # 保存获取到的网页源码

        #2、逐一解析

    return datalist

## 之所以写成一个函数是因为要爬取25个页面，所以要爬25次
#得到一个指定的url的网页内容
def askURL(url):
    # 首先要指定一个头部信息,可以为字典，可以为列表
    #head表示告诉服务器可以接受什么水平的数据
    head ={
        "User-Agent":"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.130Safari / 537.36"
    }
    request = urllib.request.Request(url,headers=head)

    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html



#吧爬取的内容放入到本地指定文件
def saveData(savePath):
    pass


if __name__=="__main__":
    #print('测试')
    main()
