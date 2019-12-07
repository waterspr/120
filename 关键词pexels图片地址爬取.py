# -*- coding: utf-8 -*-
import urllib.request
import re
import random
import time
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

keyword = "美女"
key = urllib.request.quote(keyword)  # 将中文转码

urls = [ "https://www.pexels.com/zh-cn/search/" + key +'/?page={}'.format(i) for i in range(1, 4)] #pexels网站规律，从第三页开始
# url = "https://www.pexels.com/zh-cn/search/" + key
print(urls)
for url in urls :

    ua(uapools)
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat = 'data-large-src="(.*?)"'   #图片的地址的正则表达式
    imglist = re.compile(pat).findall(data)
    # print(imglist)
    for j in range(0, len(imglist)):
        thisimgurl = imglist[j]
        print('第'+str(j)+'照片地址：'+thisimgurl)
        localfile = "D:\\2\\taobao\\2\\"+str(j)+".jpg"
        urllib.request.urlretrieve(thisimgurl, filename=localfile)
    time.sleep(1)  # 缓冲

print('------完成-----')
'''
keyword = "地球"
for i in range(1, 10):
    url = "https://www.pexels.com/zh-cn/search/" + keyword
    ua(uapools)
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat = '"pic_url":"//(.*?)"'     #data-large-src="https://images.pexels.com/photos/301614/pexels-photo-301614.jpeg?auto=compress&cs=tinysrgb&h=650&w=940"
    imglist = re.compile(pat).findall(data)
    print(imglist)
    for j in range(0, len(imglist)):
        thisimg = imglist[j]
        thisimgurl = "http://"+thisimg
        localfile = "D\\2\\taobao\\"+str(i)+str(j)+".jpg"
        urllib.request.urlretrieve(thisimgurl, filename=localfile)
'''
