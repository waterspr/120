## 写CSV 文件
# import csv

# def writecsv(path,data):
#     with open(path, "w") as f:
#         writer = csv.writer(f)
#         for rowData in data:
#             print("rowData=", rowData)
#             writer.writerow(rowData)
# path = r"d:\113.csv"
# writecsv(path ,[[1,2,3],[4,5,6],[7,8,9],[10,11,12]])


##读取csv
# import csv

# def readcev(path):
#     infolist = []
#     with open(path, "r") as f:
#         allFile = csv.reader(f)
#         for row in allFile:
#             infolist.append(row)
#     return infolist

# path = r"E:\\Python\\py17\\automatictext\\PCB3.csv"
# info = readcev(path)

##读取word
# import win32com
# import win32com.client

# def readWordFile(path):
#     # 调用系统word功能，可以处理doc和docx两种文件
#     mw = win32com.client.Dispatch("Word.Application")
#     # 打开文件
#     doc = mw.Documents.Open(path)
#     for paragraph in doc.Paragraphs:
#         line = paragraph.Range.Text
#         print(line)
#     doc.Close()
#     mw.Quit()

# path = r"d:\114.docx"
# readWordFile(path)



##读word并写入word
# import win32com
# import win32com.client


# def readWordFiletootherFile(path, topath):
#     mw = win32com.client.Dispatch("Word.Application")
#     doc = mw.Documents.Open(path)
#     # 将word的数据保存在另一个文件
#     doc.SaveAs(topath, 2)#2表示txt文件
#     doc.Close()
#     mw.Quit()

# path = r"d:\114.docx"
# topath = r"d:\115.txt"

# readWordFiletootherFile(path, topath)




###合并word文件

# # -*- encoding:utf-8 -*-
# #导入pywin32包
# import win32com.client as win32
# #打开word软件
# word = win32.gencache.EnsureDispatch('Word.Application')
# #非可视化运行
# word.Visible = False
 
# output = word.Documents.Add()#新建合并后空白文档
 
# #part1
# #需要合并的文档路径，这里有个文档1.docx，2.docx，3.docx.
# files = [r'D:\1\1.docx', r'D:\1\2.docx',r'D:\1\3.docx']
# for file in files:
# 	output.Application.Selection.Range.InsertFile(file)#拼接文档
# #endpart1
 
# #获取合并后文档的内容
# doc = output.Range(output.Content.Start, output.Content.End)
# # doc.Font.Name = "黑体"	#设置字体
 
# output.SaveAs(r'D:\meger.docx') #保存
# output.Close()



##合并另一种方法
# -*- encoding:utf-8 -*-
#导入pywin32包
import win32com.client as win32
#打开word软件
word = win32.gencache.EnsureDispatch('Word.Application')
#非可视化运行
word.Visible = False
 
output = word.Documents.Add()#新建合并后空白文档
#part1部分可以按实际使用场景替换如下：
import os
 
#声明一个待合并的列表，注意是有序的列表
files=[]
for root, dirs, filess in os.walk(r'D:\1'):  #os.walk游历D:\1目录和文件夹
	for i in filess:
		file=os.path.join(root,i)
		files.append(file)

#files.reverse() #颠倒拼接顺序，reverse()列表排序
for file in files:
	output.Application.Selection.Range.InsertFile(file)#拼接文档
#获取合并后文档的内容
doc = output.Range(output.Content.Start, output.Content.End)
# doc.Font.Name = "黑体"	#设置字体
 
output.SaveAs(r'D:\meger.docx') #保存
output.Close()
