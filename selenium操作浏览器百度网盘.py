# -*- coding: utf-8 -*-


from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Firefox()   #驱动放在python.exe目录下
wd.maximize_window()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://pan.baidu.com/')
wd.implicitly_wait(5)

time.sleep(3)
#等待三秒钟定位到账号密码登陆这个地方，进行点击
wd.find_element_by_id('TANGRAM__PSP_4__footerULoginBtn').click()
time.sleep(2)
#等待三秒钟定位到账号输入框这个地方，输入账号
username_input=wd.find_element_by_id("TANGRAM__PSP_4__userName").send_keys('18700037548')
time.sleep(2)
#等待三秒钟定位到密码输入框这个地方，输入密码
password_input=wd.find_element_by_id("TANGRAM__PSP_4__password").send_keys("liwei1992")
time.sleep(1)
login_input=wd.find_element_by_id("TANGRAM__PSP_4__submit").click()
time.sleep(3)
print('请到页面滑动验证')
#百度改为滑动验证
# code=input("请输入验证码:")
# code_input=wd.find_element_by_id("TANGRAM__PSP_4__verifyCode").send_keys(code)
# login_input=wd.find_element_by_id("TANGRAM__PSP_4__submit").click()
#登陆成功
time.sleep(5)
#知道弹窗界面
elements = wd.find_elements_by_xpath('//div[@class="tip-body"]/div[@class="know-button"]')
if elements :
    elements[0].click()
wd.find_elements_by_xpath('//div[@class="text"]/a[@title="八大员"]')[0].click()  #选择八大员
time.sleep(1)
wd.find_elements_by_xpath('//div[@class="text"]/a[@title="资料员"]')[0].click()  #选择资料员
time.sleep(1)
wd.find_elements_by_xpath('//div[@class="text"]/a[@title="02.测量书籍"]')[0].click()  #选择测量书籍
time.sleep(1)

#鼠标悬停才能出现选择分享按钮
ac = ActionChains(wd)   #实例化
ac.move_to_element(
    wd.find_elements_by_xpath('//dd[@_position="2"]')[0]
).perform()

#获取文件名
filename = wd.find_elements_by_xpath('//dd[@_position="2"]/div[@class="file-name"]/div/a')[0].text
print(filename)
#选择分享
wd.find_elements_by_xpath('//dd[@_position="2"]//div[@class="operate"]//span[@class="g-button-right"]')[0].click() 
#选择期限  通过js显示隐藏内容
js = 'document.querySelectorAll("td ul")[0].style.display="block" '   #document.querySelectorAll用法
wd.execute_script(js) #执行JS
#显示之后在选择元素
wd.find_elements_by_xpath('//div[@id="share"]//td[@class="choose-panel"]/ul/li')[0].click() 
time.sleep(1)

# #创建链接
wd.find_elements_by_xpath('//div[@id="share"]//div[@class="footer"]//a[@class="g-button g-button-large g-button-blue-large sbtn create"]/span')[0].click() 
time.sleep(1)

#复制链接
wd.find_elements_by_xpath('//div[@id="share"]//div[@class="link-info"]/div[@class="copy-button-section"]/a/span')[0].click()

text = pyperclip.paste()
print(text)
#关闭分享界面
wd.find_elements_by_xpath('//div[@id="share"]//div[@class="dialog-control"]/span')[0].click()
print('done---------------------------------')

