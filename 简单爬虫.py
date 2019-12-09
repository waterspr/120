print('hello')

"""
爬取豆瓣电影TOP250,分页保存电影数据
"""
'''
import requests
import time

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

for i in range(10):
    url=f"https://movie.douban.com/top250?start={i*25}"
    response=requests.get(url,headers=headers,verify=False)
    print(response.status_code)
    if response.status_code==200:
        # 获取网页数据
        with open(f"第{i+1}页.html","w",encoding="UTF-8") as f:
            f.write(response.text)
            print(f"{url}保存成功")
    time.sleep(2)
'''

'''
爬取豆瓣250的电影名称，并写入txt文件中
'''
'''
import requests
import time
import re

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

for i in range(1):
    url=f"https://movie.douban.com/top250?start={i*25}"
    response=requests.get(url,headers=headers,verify=False)
    # print(response.status_code)
    # print(response.text)
    data = response.text
    pat = 'alt="(.*?)"'    #正则表达式匹配，研究网页从图片链接入手的
    rst = re.compile(pat).findall(data)   #这是个列表，正则匹配结果
    print(rst)
    str1 = '\n'
    rst_str = str1.join(rst)    #转化为字符串
    with open(r'F:\1\250.txt', 'a+') as f:     
        f.write(rst_str)   #list列表无法直接写入文件，需转化为字符串
f.close()
'''
import requests
import time
import re
import urllib3
urllib3.disable_warnings()

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

for i in range(1):
    url=f"https://movie.douban.com/top250?start={i*25}"
    response=requests.get(url,headers=headers,verify=False)
    # print(response.status_code)
    # print(response.text)
    data = response.text
    # pat = 'alt="(.*?)"'   
    pat = '<span class="title">(.*?)</span>'
    rst = re.compile(pat).findall(data)   #这是个列表
    print(rst)
  
