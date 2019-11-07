#  第一段 字符串和list（列表）
#  list1 = ['you are python','good']
# print ( len(list1))
# print( list1[0] )
# list2 = ('you are python')
# print(len(list2))
# print(list2[0])
# list3 = 'you are python'
# print (len(list3))
# print (list3[0])

#  第二段  关于读取文件 和 写入文件
a = open(r'C:\Users\Administrator\Desktop\test\110.txt') #打开文件
data = a.read()     #读取文件中的内容
print(data)         #输出文件中的内容
b = open(r'C:\Users\Administrator\Desktop\test\120.txt','w')  # ’w‘写入模式打开
b.write(data)
a.close()
b.close()
c=open(r'C:\Users\Administrator\Desktop\test\120.txt')
data2 = c.read()
print(data2)

#
 