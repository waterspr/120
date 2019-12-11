# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from dangdangwang.items import DangdangwangItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-1']

    def parse(self, response):
        print('-'*25)
        item = DangdangwangItem()  #实例化一个类
        
        booklists = response.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li')
        # print(booklists)

        for book in booklists:
            item['name'] = book.xpath('./div[@class="name"]/a/text()').extract_first()
            item['price']= book.xpath('./div[@class="price"]/p[1]/span[1]/text()').extract_first()
            # print(item['name'])
            # print(item['price'])
            
            yield item #传入pipeline
        print("------------------------")
        
        # print(items['name'] )     
        
