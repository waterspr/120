from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import re 
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Firefox()   #驱动放在python.exe目录下
wd.maximize_window()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://news.baidu.com/')
wd.implicitly_wait(8)  #最长等待时间，每半秒请求一次
for i in range(4):
    js = "var q=document.documentElement.scrollTop=" + str((i+1)*200)
    wd.execute_script(js)