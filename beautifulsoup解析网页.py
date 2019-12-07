
'''
#coding=utf-8
from bs4 import BeautifulSoup
import requests
#使用requests抓取页面内容，并将响应赋值给page变量
html = requests.get('http://www.duanziwang.com/')
print(html.status_code)  #判断是否get成功
 
#使用content属性获取页面的源页面
#使用BeautifulSoap解析，把内容传递到BeautifulSoap类
soup = BeautifulSoup(html.content,'lxml')
 
title_links = soup.find_all('h1')   #通过查标签的方式，类似xpath
content_links = soup.find_all('p')
# print(title_links)
# print(content_links)
 
#link的内容就是div，我们取它的span内容就是我们需要段子的内容
# for link in links:
#     print (link.span.get_text())
#我们取它的 内容就是我们需要段子的内容
for x, y in zip(title_links,content_links):  #同时对两个list列表历遍
    print(x.get_text())
    print(y.get_text())
    print('\n')
print('-----done------')
'''
'''
select()方法
'''
#coding=utf-8
from bs4 import BeautifulSoup
import requests
 
#使用requests抓取页面内容，并将响应赋值给page变量
html = requests.get('http://www.duanziwang.com/')
 
#使用content属性获取页面的源页面
#使用BeautifulSoap解析，吧内容传递到BeautifulSoap类
soup = BeautifulSoup(html.content,'lxml')
#我是分隔符，下面就是select（）方法咯~
content_links = soup.select('article > div > p')  #> 前后一定要有空格，不然会报错的)
for link in content_links :
    print(link.get_text()
    print('\n')

print('-----done------')    