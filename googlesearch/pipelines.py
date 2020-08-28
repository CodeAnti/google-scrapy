# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors


class GooglesearchPipeline:
    def __init__(self):
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='scrapy_search',
            user='root',
            passwd='root',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """
            insert into google (keywords,domain,rank,created_at,updated_at) values (%s, %s, %s, %s, %s)
            """,
            (item['keywords'], item['domain'], item['rank'], item['created_at'], item['updated_at'])
        )
        self.connect.commit()
        return item
