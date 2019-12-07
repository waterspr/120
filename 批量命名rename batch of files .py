a = 1
print('we %s china'% a)  #格式化字符串


###批量重命名
import shutil
import os
os.chdir(r'C:\Users\pc\Desktop\1234')  # 这里是文件所在目录，必须切换到文件目录中才可以使用rename方法
i = 1
for filename in os.listdir(r'C:\Users\pc\Desktop\1234'):
    portion = os.path.splitext(filename)
    print(i)
    j=str(i)
    new_filename ='【' + j +'】'+portion[0] + portion[1]
    os.rename(filename,new_filename)
    i = i+1