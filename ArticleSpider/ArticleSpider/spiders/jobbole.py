# -*- coding: utf-8 -*-
import re

import scrapy
import re
from scrapy.http import Request
class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112170/']

    def parse(self, response):
        articleurl_list=response.css('#archive .post-meta a.archive-title::attr(href)').extract()
        for url_item in articleurl_list:
            Request(url=url_item,callback=self.detail_parse)
            
        pass
        # re_selector=response.xpath('//*[@id="post-112170"]/div[1]/h1')
        # articleTitle=response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        # publishDate = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace(' ·', '')
        # voteNumber = int(response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0])
        # collectNumber = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
        # collectRe=re.match('.*(\d+).*', collectNumber)
        # if collectRe:
        #     collectNumber=collectRe.group(1)
    def detail_parse(self,response):
        # 文章标题
        article_title = response.css('.entry-header h1::text').extract_first()
        #发布时间
        publish_time = response.css('.entry-meta-hide-on-mobile::text').extract_first().strip().replace('·', '').strip()
        #文章标签
        tag_names = ','.join(response.css('.entry-meta-hide-on-mobile a::text').extract())
        #点赞数
        vote_number=response.css('.vote-post-up h10::text').extract_first()
        if not vote_number:
            vote_number=0
         # 收藏数
        origin_collect=response.css('.href-style.bookmark-btn::text').extract_first()
        collect_re=re.search('\d+',origin_collect)
        if  collect_re:
            collect=collect_re
        else:
            collect=0
        pass
#         内容
        article_contnet=response.css('.entry').extract_first()


