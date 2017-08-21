# -*- coding: utf-8 -*-
import re

import scrapy
import re
from urllib.parse import urljoin
from scrapy.http import Request

from ArticleSpider.items import JobBoleArticleItem
from ArticleSpider.utils.common import getmd5

class JobboleSpider(scrapy.Spider):
	name = 'jobbole'

	allowed_domains = ['blog.jobbole.com']
	start_urls = ['http://blog.jobbole.com/all-posts/']

	def parse(self, response):
		articleurl_list = response.css('#archive .post-thumb')   #提取包含图片和链接的模块
		for url_item in articleurl_list:
			# 提取每个pages的url
			post_url = url_item.css('a::attr(href)').extract_first('')
			# 提取图片的URL
			image_url = url_item.css('img::attr(src)').extract_first('')
			#将每个URL交给detail解析，同时meta中放置每个图片的URL
			yield Request(url=post_url, callback=self.detail_parse,
			              meta={'front_img_url': urljoin(response.url, image_url)})
		# 提取下一页的URL
		next_pageurl = response.css('.next.page-numbers::attr(href)').extract_first()
		# 交给parse进行解析
		yield Request(url=next_pageurl, callback=self.parse)
		pass
		# re_selector=response.xpath('//*[@id="post-112170"]/div[1]/h1')
		# articleTitle=response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
		# publishDate = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace(' ·', '')
		# voteNumber = int(response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0])
		# collectNumber = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
		# collectRe=re.match('.*(\d+).*', collectNumber)
		# if collectRe:
		#     collectNumber=collectRe.group(1)

	def detail_parse(self, response):
		article_item = JobBoleArticleItem()

		# 文章标题
		article_title = response.css('.entry-header h1::text').extract_first()

		# 发布时间
		publish_time = response.css('.entry-meta-hide-on-mobile::text').extract_first().strip().replace('·', '').strip()
		# 文章标签
		tag_names = ','.join(response.css('.entry-meta-hide-on-mobile a::text').extract())
		# 点赞数
		vote_number = response.css('.vote-post-up h10::text').extract_first()
		if not vote_number:
			vote_number = 0
			# 收藏数
		origin_collect = response.css('.href-style.bookmark-btn::text').extract_first()
		collect_re = re.search('\d+', origin_collect)
		if collect_re:
			collect = collect_re.group()
		else:
			collect = 0
		#         内容
		article_contnet = response.css('.entry').extract_first()
		# 图片的URL
		front_url = response.meta.get('front_img_url')



		# 从引用的items中为定义好的字段填充相应的内容
		article_item['article_title']=article_title
		article_item['publish_time']=publish_time
		article_item['url']=response.url
		article_item['tag_names']=tag_names
		article_item['vote_number']=vote_number
		article_item['front_url']=front_url
		article_item['collect']=collect
		article_item['vote_number']=vote_number
		article_item['front_url']=[front_url] #这里必须设置为数组
		article_item['article_contnet']=article_contnet
		article_item['url_md5']=getmd5(response.url)


		# yield 填充好的类
		yield article_item

		pass
