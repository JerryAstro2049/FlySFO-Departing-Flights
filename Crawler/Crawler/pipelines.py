# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json


class CrawlerPipeline:
    def __init__(self):
        self.file = open('SFO today departs.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = "\n" + json.dumps(dict(item), ensure_ascii=False) + ","
        self.file.write(line)
        return item

    def open_spider(self, spider):
        self.file.write('{"SFO today departs":[')

    def close_spider(self, spider):
        self.file.write('\n]}')
