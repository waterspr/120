ph = "abc"
print('excel文件名%s' % ph)

from openpyxl import load_workbook
import os
from openpyxl import Workbook

wb = load_workbook('d:\\1\\1.xlsx')
wb.guess_types = True   #猜测格式类型
sheet = wb.active
# sheet.append(['1','2'])
# wb.save('d:\\1\\1.xlsx')


for index, row in enumerate(sheet.rows):
    if index > 0:  # 因为 index = 0时，获取到的为表格的值。
         print(row)
         print("\n")
         for item in row:   #  这个迭代无特殊情况 可简化一下
            print(item.value)






# for row in sheet.rows:
#     for cell in row:   #  这个迭代无特殊情况 可简化一下
#         print(cell.value)