# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapylib.processors import default_input_processor, default_output_processor


class FosshackersItem(scrapy.Item):
    id_ = scrapy.Field()
    type_ = scrapy.Field()
    file_urls = scrapy.Field()


class FosshackersItemLoader(ItemLoader):
    default_item_class = FosshackersItem
    default_input_processor = default_input_processor
    default_output_processor = default_output_processor
