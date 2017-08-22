# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import  MySQLdb
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.images import ImagesPipeline


#
class ArticlespiderPipeline(object):
	def process_item(self, item, spider):
		return item


# 我们自己定义的pipelines 需要在seeting中与之对应
class ArticleImagePipLine(ImagesPipeline):
	def item_completed(self, results, item, info):
		for ok, value in results:
			image_file_path = value['path']

		item['front_url'] = image_file_path

		return  item
class JsonWithEncodingPipeline(object):
	def __init__(self):
		self.file=codecs.open('article.json','w',encoding='utf-8')
	def process_item(self, item, spider):
		lines=json.dumps(dict(item),ensure_ascii=False) + '\n' #如果不指定中文就会出问题
		self.file.write(lines)
		return item
	def spider_closed(self,spider):
		self.file.close()
class JsonExporterPipleline(object):
	# 调用scrapy提供的json export提供方法
	def __init__(self):
		self.file=open('articleexport.json','wb')
		self.exporter=JsonItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
		self.exporter.start_exporting()

	def close_spider(self,spider):
		self.exporter.finish_exporting()
		self.file.close()

	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item


class MysqlPipeLine(object):
	def __init__(self):
		self.conn=MySQLdb.connect('127.0.0.1','root','root','articlespider',charset='utf8',use_unicode=True)
		self.cursor=self.conn.cursor()

	def process_item(self, item, spider):
		insert_sql='''
		insert into jobbole (article_title,url,publish_time,vote_number)
		VALUES
		(%s,%s,%s,%s)
		'''

		self.cursor.execute(insert_sql,(item['article_title'],item['url'],item['publish_time'],item['vote_number']))
		self.conn.commit()

