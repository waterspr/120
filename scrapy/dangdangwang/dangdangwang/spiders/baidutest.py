# -*- coding: utf-8 -*-
import scrapy


class BaidutestSpider(scrapy.Spider):
    name = 'baidutest'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print("----------")
        print (type(response))
        
        print(response.text)
        print('-'*25)
