# -*- coding: utf-8 -*-
#author ： waterspr
#单层目录分享

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import re 

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Firefox()   #驱动放在python.exe目录下
wd.maximize_window()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://pan.baidu.com/')
wd.implicitly_wait(8)  #最长等待时间，每半秒请求一次

time.sleep(2)
#等待三秒钟定位到账号密码登陆这个地方，进行点击，切换为账号登录
wd.find_element_by_id('TANGRAM__PSP_4__footerULoginBtn').click()
time.sleep(2)
#等待三秒钟定位到账号输入框这个地方，输入账号
username_input=wd.find_element_by_id("TANGRAM__PSP_4__userName").send_keys('18700037548')
time.sleep(1)
#等待三秒钟定位到密码输入框这个地方，输入密码
password_input=wd.find_element_by_id("TANGRAM__PSP_4__password").send_keys("liwei1992")
time.sleep(1)
#确认登陆
login_input=wd.find_element_by_id("TANGRAM__PSP_4__submit").click()
time.sleep(3)
print('请到页面滑动验证')

time.sleep(5)
#知道弹窗界面
elements = wd.find_elements_by_xpath('//div[@class="tip-body"]/div[@class="know-button"]')
if elements :
    elements[0].click()

#定位需要分享的目录
wd.find_elements_by_xpath('//div[@class="text"]/a[@title="八大员"]')[0].click()  #选择八大员
time.sleep(1)
wd.find_elements_by_xpath('//div[@class="text"]/a[@title="资料员"]')[0].click()  #选择资料员
time.sleep(1)
wd.find_elements_by_xpath('//div[@class="text"]/a[@title="02.测量书籍"]')[0].click()  #选择测量书籍
time.sleep(1)

#判断文件的个数
n = len(wd.find_elements_by_xpath('//div[@class="vdAfKMb"]/dd') ) 
print(n)

#遍历该目录下所有文件
for i in range(n):
    # 向下滚动200个像素
    # # js = "var q=document.body.scrollTop=" +(n+1)*400
    # js = "var q=document.documentElement.scrollTop="+str((n+1)*400 )
    # wd.execute_script(js)
   

    time.sleep(1)

    #鼠标悬停才能出现选择分享按钮
    ac = ActionChains(wd)   #实例化
    ac.move_to_element(
       wd.find_elements_by_xpath(f'//div[@class="vdAfKMb"]/dd[{i}+1]')[0]    
        ).perform()                      #xpath 是从第一个元素是1，循环第一个是0
    time.sleep(3)
    #获取文件名   
    #注意 字符串中间加变量，可以使用格式化字符串
    filename = wd.find_elements_by_xpath(f'//div[@class="vdAfKMb"]/dd[{i}+1]/div[@class="file-name"]/div/a')[0].text
    # print(filename)
    
    #选择分享
    #直接悬停选择
    # wd.find_elements_by_xpath(f'//div[@class="vdAfKMb"]/dd[{i}+1]//div[@class="operate"]//a[@class="g-button"]/span[@class="g-button-right"]/em')[0].click() 
    
    el = wd.find_elements_by_xpath(f'//div[@class="vdAfKMb"]/dd[{i}+1]')[0]   
    ac.context_click(el).perform()  #右击
    time.sleep(1)
    wd.find_elements_by_xpath('//div[@class="context-menu"]/ul[@class="list"]/li[10]')[0].click()

    
    
    #选择期限  通过js显示隐藏内容
    js = 'document.querySelectorAll("td ul")[0].style.display="block" '   #document.querySelectorAll用法
    wd.execute_script(js) #执行JS
    #显示之后在选择元素
    wd.find_elements_by_xpath('//div[@id="share"]//td[@class="choose-panel"]/ul/li')[0].click() 
    time.sleep(2)

    # #创建链接
    wd.find_elements_by_xpath('//div[@id="share"]//div[@class="footer"]//a[@class="g-button g-button-large g-button-blue-large sbtn create"]/span')[0].click() 
    time.sleep(3)

    #复制链接
    wd.find_elements_by_xpath('//div[@id="share"]//div[@class="link-info"]/div[@class="copy-button-section"]/a/span')[0].click()

    text = pyperclip.paste()
    print(f'第{i}个文件：' + text)
    if '复制' in text :   #判断字符是否在字符串中
        pat2 ="(.*) 复制"
        rst2 = re.compile(pat2).findall(text) 
        text = rst2[0]
    

    with open(r'f:\1\12345.txt', 'a+',encoding='utf-8') as f:
        f.write(filename  +  '       '   +text + '\n')

    #关闭分享界面
    wd.find_elements_by_xpath('//div[@id="share"]//div[@class="dialog-control"]/span')[0].click()

    target = wd.find_elements_by_xpath(f'//div[@class="vdAfKMb"]/dd[{i}+2]')[0] 
    if target :
        wd.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
    else:
        target = wd.find_elements_by_xpath(f'//div[@class="vdAfKMb"]/dd[last()]')[0] 
        wd.execute_script("arguments[0].scrollIntoView();", target) 

    # #向下滚动200个像素
    # js = "var q=document.body.scrollTop=" + str((i+1)*200)
    # wd.execute_script(js)
print('done-----------------------------')




