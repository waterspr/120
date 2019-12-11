# -*- coding: utf-8 -*-
import pandas as pd
import csv

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangwangPipeline(object):
    def process_item(self, item, spider):
        print(item['name'])
        # 1. 创建文件对象
        f = open(r'D:\2\test.csv','a+',encoding='gb18030',newline='' ) 
        #2. 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f) 
       # 3. 构建列表头
        # csv_writer.writerow(["书名","价格"]) 
        # 4. 写入csv文件内容
        csv_writer.writerow([item['name'],item['price']])
        # 5. 关闭文件
        f.close()

        #字典中的key值即为csv中列名
        # dataframe = pd.DataFrame({'a_name':item['name'],'b_name':item['price']})
        # #将DataFrame存储为csv,index表示是否显示行名，default=True
        # dataframe.to_csv(r"D:\2\test.csv",encoding="utf-8-sig", mode="a", header=False, index=False)

        # print(item['name'])
        return item


        '''
        直接将爬取的数据存入csv文件中，
        直接在cmd终端运行，即可在爬虫项目文件夹生成csv文件
        scrapy crawl dangdang -o dangdang.csv -t csv

        可在settings.py中设置输出编码

        '''

