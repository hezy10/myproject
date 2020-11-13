# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    position = scrapy.Field()
    cprice = scrapy.Field()
    href = scrapy.Field()
    price = scrapy.Field()
    roomnum = scrapy.Field()
    # config = scrapy.Field()

