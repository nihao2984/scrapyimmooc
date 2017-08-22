# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	pass


class JobBoleArticleItem(scrapy.Item):
	article_title = scrapy.Field()
	publish_time = scrapy.Field()
	url = scrapy.Field()
	url_md5 = scrapy.Field()
	tag_names = scrapy.Field()
	vote_number = scrapy.Field()
	collect = scrapy.Field()
	article_content = scrapy.Field()
	vote_number = scrapy.Field()
	front_url = scrapy.Field()
	front_image_path = scrapy.Field()
