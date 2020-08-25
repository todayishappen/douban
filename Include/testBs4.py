'''
beatifulSoup4:将html文档转化为一个复杂的属性结构，每个节点为python对象，分为四种：【解析网页】
    Tag
    NavigableString
    BeatifulSoup
    Coment
'''

from bs4 import BeautifulSoup
file=open('./baidu.html','rb')
html=file.read().decode('utf-8')
bs=BeautifulSoup(html,"html.parser") # parser为解析器，解析
print(bs.title)  # 找到第一个对应的标签内容    type为bs4.elemnet.tag

print(bs.title.string)   # 直接打印标签内的内容， type为bs4.element.NavigableString

print(bs.a.attrs) # 获取标签中的所有属性值，返回字典【属性】

print(type(bs)) # type为bs4.BeautifulSoup

print(bs)  # 整个文档的内容

print(bs.a.string)   # type为bs4.element.conment，如果标签内的为注释，则去掉注释符号，类型为这个

#---------------------------------
# 文档的遍历，然后文档的搜索

print(bs.head.contents) #获得head的内容放入到列表中，包括换行符
#['\n', <meta charset="utf-8"/>, '\n', <link href="css/base.css" rel="stylesheet" type="text/css"/>, '\n', <link href="css/index.css" rel="stylesheet" type="text/css"/>, '\n', <title>百度一下，你就知道</title>, '\n']
print(bs.head.contents[1])

#文档的搜索
#find_all
#1、
t_list=bs.find_all('a')  # find_all表示查找所有匹配的字符串‘a’，返回列表【只有字符串a】
#2、平时使用正则表达式的search()匹配内容
import re
t_list = bs.find_all(re.compile('a')) # 比如meta也找到了，按照标签来找的
print(t_list)
#3、传入一个函数（方法），根据函数要求搜索
def name_is_exists(tag):
    return tag.has_attr('name')

#使用for循环查看list
for item in t_list:
    print(item)

print('------------------------------------------')
#kwargs 参数
t_list=bs.find_all(id='head')
for item in t_list:
    print(item)
t_list=bs.find_all(class_=True) # 表示包含class及其子内容
t_list=bs.find_all(href='www.baidu.com')
print('------------------------------------------')
#text 参数
t_list=bs.find_all(text='hao123')
#可以写列表
t_list=bs.find_all(text=['hao123','百度',''])
t_list=bs.find_all(text=re.compile('\d')) #正则表达式数字

print('------------------------------------------')
#limit 参数
t_list=bs.find_all('a',limit=3) # 限定范围

print('------------------------------------------')
#css选择器
t_list=bs.select('title')  #标签
t_list=bs.select('.nav')  #选择器，.表示class
t_list=bs.select('#nav-b')  #选择器，#表示id
t_list=bs.select('a[class="nav-a"]')  # 表示在a标签中选择特定的属性
t_list=bs.select('head > title') #找子内容
t_list=bs.select('.nav-a ~ .shezhi') #找兄弟的标签内容，print(t_list[0].get_text()),第一个的内容
for item in t_list:
    print(item)