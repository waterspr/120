#  -*- coding :utf8 -*-

import xlrd
from  openpyxl import  Workbook    #导入库
from openpyxl  import load_workbook  #导入库
import os 

#在目标的文件夹中遍历出所有的excel文档
'''
def find_excle(path):
    

'''


#创建工作簿和工作表
wb3 = Workbook()
# 激活 worksheet
ws3 = wb3.active

for root, dirs, files in os.walk(r'd:\1'):   #os.walk()用法
    for name in files :
        # print(os.path.join(root, name))
        ph = os.path.join(root, name)
        print(ph)
        wb1 = xlrd.open_workbook(ph)   #导入工作簿
        ws1 = wb1.sheet_by_index(0)
        nrows1 = ws1.nrows
        for row1 in range(0,nrows1+1) :     #
            try :
                data1 = ws1.row_values(row1,start_colx=0, end_colx=None)  #取出每行数据 列表
                print(data1)
                ws3.append(data1)   #添加储存到工作表3
            except:
                continue
        # ws3.append(data1)       #添加储存到工作表3


wb3.save(r'D:\00.xlsx')
print('done')

