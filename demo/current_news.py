# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import csv
import datetime
#得到当前的时间
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
#创建列表储存新闻标题
new_title = []
#创建列表储存新闻跳转的百度界面
urls = []
#创建csv文件 操作方式为写入, 文件名为时间
csv_file = open(nowTime+".csv","w")
# 创建writer对象，指定文件与分隔符
csv_writer = csv.writer(csv_file, delimiter=',')
#s = requests.Session()
#百度风云榜的url
url = "http://top.baidu.com/buzz?b=1&fr=tph_right"
#设置请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
#通过一个get请求获取网页信息
req = requests.get(url,headers = headers)
#处理乱码问题
req.encoding=('gb2312')
#用Beautiful soup 解析网页
soup = BeautifulSoup(req.text,"html.parser")
#用select选择出所有新闻的超链接,储存在url列表中
all_url = soup.select('a.list-title')
print(nowTime)
for i in all_url:
    url = i["href"]
    urls.append(url)
#获取新闻题目
    new_title.append(i.string)
    # print(str(a)+i.string)
for i in range(len(urls)):
#print(urls[i])
    req = requests.get(urls[i],headers= headers)
    soup = BeautifulSoup(req.text,"html.parser")
    reall_all_url = soup.select('div > a')
    for m in range(24,200):
        try:
            if 'http://www.baidu.com/link?url=' in reall_all_url[m]["href"] :
                print(m)
                print(i + 1, new_title[i], reall_all_url[m+6]["href"])
                csv_writer.writerow([i + 1, new_title[i], reall_all_url[m+6]["href"]])
                break
        except:
            continue
    time.sleep(1)
csv_file.close()