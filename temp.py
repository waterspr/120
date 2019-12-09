import re
str1 = "123332323" 
pat = '(23)+'
rst = re.compile(pat).findall(str1) 
print (rst)
