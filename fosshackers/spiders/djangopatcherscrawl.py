# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from fosshackers.items import FosshackersItem


class DjangopatcherscrawlSpider(CrawlSpider):
    name = 'djangopatcherscrawl'
    allowed_domains = ['code.djangoproject.com']
    start_urls = [
        'https://code.djangoproject.com/query'
        '?status=assigned&status=closed&status=new'
        '&has_patch=1&desc=1&order=id',
    ]

    rules = (
        Rule(LinkExtractor(restrict_css='.paging a'),
             follow=True),
        Rule(LinkExtractor(restrict_css='.tickets.listing tbody .id a'),
             callback='parse_issue', follow=False),
    )

    def parse_issue(self, response):
        item = FosshackersItem()
        item['id_'] = response.css('h2 > a::text').extract_first()
        item['type_'] = response.css('.trac-type a::text').extract_first()
        return item
