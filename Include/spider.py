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
    saveData(datalist,savePath)
    #askURL("https://movie.douban.com/top250?start=")

#获得超链接规则
findlink=re.compile(r'<a href="(.*?)">')
#获取图片的链接
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S) # S表示让换行符包含在字符中
#电影片名
findTitle=re.compile(r'<span class="title">(.*)</span>')
#电影评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq=re.compile(r'<span class="inq">(.*)</span>')
#找到电影内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)

#进入网页后把网页中的想要爬取的内容参数放入到集合中
def getData(baseurl):
    datalist=[]
    for i in range(0,10):
        # 1、获取网页内容
        url=baseurl+str(i*25)
        html=askURL(url)  # 保存获取到的网页源码
        #print('------------------************-------------')
        #2、逐一解析
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"): # 查找符合要求的字符串，列表
            #print(item)
            data=[]
            item=str(item)
            #获得电影超链接
            link=re.findall(findlink,item)[0] # findlink是一个全局变量正则
            #print(link)
            data.append(link)
            imgSrc=re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item) #添加中文名等第二个名字
            if(len(titles)==2):
                ctitle=titles[0]
                data.append(ctitle)
                otitle=titles[1].replace("/","") #替换无关的符号
                #otitle = otitle.replace(u"\xa0", u"")  # 替换无关的符号
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ') #留空
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            judge = re.findall(findJudge, item)[0]
            data.append(judge)
            inq = re.findall(findInq, item)
            if len(inq) !=0:
                inq=inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")
            bd = re.findall(findBd, item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?'," ",bd)  # \s表示空格，相当space，去掉<br>
            bd=re.sub('/'," ",bd)
            #bd = bd.replace(u"\xa0", u"")
            data.append(bd.strip()) # 去掉前后的空格

            datalist.append(data)
        #print(datalist)
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
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html



#吧爬取的内容放入到本地指定文件
def saveData(datalist,savePath):
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True) #可以覆盖
    col=('电影详情链接',"图片链接","电影中文名","电影外文名","评分","评价数","概况","相关信息") #设置列
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%(i+1))
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savePath)
    print("爬取完毕")




if __name__=="__main__":
    #print('测试')
    main()
