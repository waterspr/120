# -*- coding: utf-8 -*-

###pexels图片下载链接下载
import urllib.request
import requests
import re
import random
import time
from lxml import etree
'''
keyname = "连衣裙"
key = urllib.request.quote(keyname)  # 将中文转码
print(key)
'''


uapools = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
    "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

#定义用户代理函数
def ua(uapools):
    thisua = random.choice(uapools)
    headers = ("User-Agent", thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 安装为全局
    urllib.request.install_opener(opener)

keyword = "美"
key = urllib.request.quote(keyword)  # 将中文转码

urls = [ "https://www.pexels.com/zh-cn/search/" + key +'/?page={}'.format(i) for i in range(1, 3)] #pexels网站规律，从第三页开始
# url = "https://www.pexels.com/zh-cn/search/" + key
print(urls)
a = 1
for url in urls :

    ua(uapools)
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    print(len(data))
    html = etree.HTML(data)   #转化为html对象
    imglist = html.xpath('//div[@class="hide-featured-badge hide-favorite-badge"]/article/@data-photo-modal-image-download-link') #xpath使用筛选链接

#使用正则表达式
    # pat = 'data-large-src="(.*?)"'  #图片的下载链接地址的正则表达式
    # #data-photo-modal-image-download-link="(.*?)"
    # imglist = re.compile(pat,re.S).findall(data)

    # print(imglist)
    for j in range(0, len(imglist)):
        thisimgurl = imglist[j]
        print('第'+str(j)+'照片地址：'+thisimgurl)

#使用requests库 下载写入内容
        # f=requests.get(thisimgurl)
        # f_name = "D:\\2\\taobao\\2\\picture"+str(a)+str(j)+".jpg"
        # with open(f_name,"wb") as code:
        #     code.write(f.content)  ##将响应对象的内容写下来

#使用urllib.request.urlretrieve下载
        localfile = "D:\\2\\taobao\\3\\"+str(a)+str(j)+".jpg"
        urllib.request.urlretrieve(thisimgurl, filename=localfile)  #urllib.request.urlretrieve下载
    a +=1
    time.sleep(1)  # 缓冲

print('------完成-----')