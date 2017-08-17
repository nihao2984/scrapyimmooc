# -*- coding: utf-8 -*-
import re

import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112170/']

    def parse(self, response):
        # re_selector=response.xpath('//*[@id="post-112170"]/div[1]/h1')
        articleTitle=response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        publishDate = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace(' ·', '')
        voteNumber = int(response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0])
        collectNumber = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
        collectRe=re.match('.*(\d+).*', collectNumber)
        if collectRe:
            collectNumber=collectRe.group(1)


        pass

