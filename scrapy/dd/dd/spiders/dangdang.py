# -*- coding: utf-8 -*-
import scrapy


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://dangdang.com/']

    def parse(self, response):
        title = response.xpath("//p[@class="name"]/a/text()").get()  # get()/getall()/extract_first()
        print(title)