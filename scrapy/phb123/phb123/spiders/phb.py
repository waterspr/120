# -*- coding: utf-8 -*-
import scrapy
from phb123.items import Phb123Item


class PhbSpider(scrapy.Spider):
    name = 'phb'
    allowed_domains = ['phb123.com']
    start_urls = ['https://www.phb123.com/hangye/qiche/']

    def parse(self, response):

        # 测试输出
        # print(type(response))
        # print(response.body)
        item = Phb123Item()  #实例化对象

        # 网页解析函数
        carlists = response.xpath('//div[@class="mar1"]//tbody/tr')
        print(type(carlists))
        for carlist in carlists:
            print('-'*50)
            item['rank'] = carlist.xpath('./td[1]/text()').extract_first()
            item['carmodel'] = carlist.xpath('./td/a/p/text()').extract_first()
            item['octsale'] = carlist.xpath('./td[3]/text()').extract_first()
            item['yearsale'] = carlist.xpath('./td[4]/text()').extract_first()

            print(item['carmodel'])
            yield item
        #构造下一页url
        next_text=response.xpath('//div[@class="page mt10"]/a[last()-1]/text()').extract_first()
        if next_text == '下一页':
            next_page = response.xpath('//div[@class="page mt10"]/a[last()-1]/@href').extract_first()
            print(next_page)
            next_page = response.urljoin(next_page)        # 将相对地址转换为绝对地址
 
            yield scrapy.Request(next_page, callback=self.parse)    # next_page继续进行spider解析
