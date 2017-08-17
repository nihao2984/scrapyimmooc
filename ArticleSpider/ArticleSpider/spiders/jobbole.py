# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112170/']

    def parse(self, response):
        # re_selector=response.xpath('//*[@id="post-112170"]/div[1]/h1')
        re_selector=response.xpath('//div[@class="entry-header"]/h1/text()')
        pass

