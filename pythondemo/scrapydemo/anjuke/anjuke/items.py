# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class AnjukeItem(Item):
    # define the fields for your item here like:
    url = Field()
    title = Field()
    price = Field()
    roomType = Field()
    rentType = Field()
    decoration = Field()
    floor = Field()
    area = Field()
    address = Field()
