# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from fosshackers.items import FosshackersItem


class DjangopatcherscrawlSpider(CrawlSpider):
    name = 'djangopatcherscrawl'
    allowed_domains = ['code.djangoproject.com']
    start_urls = ['http://www.code.djangoproject.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = FosshackersItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
