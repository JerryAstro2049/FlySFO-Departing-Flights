# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FlightItem(scrapy.Item):
    Airline = scrapy.Field()
    DepartingTo = scrapy.Field()
    Flight = scrapy.Field()
    Scheduled = scrapy.Field()
    Estimated = scrapy.Field()
    Remarks = scrapy.Field()
    Terminal = scrapy.Field()
    Gate = scrapy.Field()
