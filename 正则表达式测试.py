import re
str1 = "123332323" 
pat = '(23)+'
rst = re.compile(pat).findall(str1) 
print (rst)

str2 = '链接: https://pan.baidu.com/s/14t3dZ-fO4D1_iHpc0XQghw 提取码: gims 复制这段内容后打开百度网盘手机App，操作更方便哦'
str3 = '链接: https://pan.baidu.com/s/14t3dZ-fO4D1_iHpc0XQghw 提取码: gims '
pat2 ="(.*) 复制"
if '复制' in str2 :
    rst2 = re.compile(pat2).findall(str2) 
    print(rst2)

if '复制' in str3 :
    rst3 = re.compile(pat2).findall(str3) 
    print(rst3)
else:
    print(str3)

print('1')


# import  re


# a= '导演:弗兰克·德拉邦特FrankDarabont主演:蒂姆·罗宾斯TimRobbins/...'
# b = "主演: 罗宾斯 Tim Robbins /..."
# # pat = "导演:([\u4e00-\u9fa5]+[·| /s][\u4e00-\u9fa5]+)"

# # pat = "导演:([^\x00-\xff]+)"
# pat = "导演:(.*)主演"

# rst1 = re.compile(pat).findall(a)
# rst2 = re.compile(pat).findall(b)
# print(rst1)
# print(rst2)

