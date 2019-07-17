# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


def remove_whitespaces(value):
    return value.strip()


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespaces),
        output_processor=TakeFirst()
    )

    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespaces),
        output_processor=TakeFirst()
    )
