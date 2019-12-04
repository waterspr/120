print('hello visual code')
import requests
import time
import re
from lxml import etree

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

for i in range(10):
    url=f"https://movie.douban.com/top250?start={i*25}"  #豆瓣网页分析
    response=requests.get(url,headers=headers,verify=False)  #requests.get获取网页信息
    # print(response.status_code)
    # print(response.text)
    data = response.text  #网页文本对象
    html = etree.HTML(data)   #转化为html对象
    # result = etree.tostring(html)   #etree不仅将节点闭合了还添加了其他需要的标签。
    rst1 = html.xpath('//div[@class="info"]//span[@class="title"][1]/text()') #xpath使用筛选出电影名称，返回列表
    rst2 = html.xpath('//div[@class="bd"]/p[@class=""]/text()') #xpath使用筛选出电影导演演员
    rst3 = html.xpath('//div[@class="star"]/span[contains(@class,"rating_num")]/text()') #xpath使用筛选评分
    # print(rst2[0])  #测试输出列表内容
    i = 0
    for name in  rst2:     #去除导演演员列表字符串中的空白字符
        name = "".join(name.split())
        rst2[i] = name
        i += 1
    director = []   #存放导演名列表
    actor = []      #存放主演名列表
    other = []     #存放其他列表
    for j in range(0,len(rst2),2) :      #把列表偶数元素导演和主演分开
        pat = "导演:(.*)主演"      #正则表达式匹配
        pat2 = "主演:(.*)"         #正则表达式匹配
        r11 = re.compile(pat).findall(rst2[j])
        r22 = re.compile(pat2).findall(rst2[j])
        director.append(r11)
        actor.append(r22)
    for k in range(1,len(rst2),2) :    #把列表奇数元素信息提取出来
        r33 = rst2[k]
        other.append(r33)
    # print(director)
    # print(actor)
    # print(other)
    for l in range(len(rst1)) :
        try:   #解决IndexError: list index out of range
            print(rst1[l],'    ',director[l][0],'     ',actor[l][0],'     ',other[l],'      ',rst3[l] )   # director和actor列表是嵌套的
            with open(r'D:\1\12345.txt', 'a+',encoding='utf-8') as f:
                f.write('\n')  #空行
                f.write(rst1[l] + '    '  + director[l][0] + '   ' + actor[l][0]+ '    '+ other[l] + '    '  + rst3[l] +"\n")  #换行写入txt文件
        except :
            continue 
time.sleep(3)
print('done!')
    


