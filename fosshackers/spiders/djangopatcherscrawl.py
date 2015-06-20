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
        return {'id': response.css('h2 > a::text').extract_first(),
                'type': response.css('.trac-type a::text').extract_first()}

    # def parse_item(self, response):
    #     i = FosshackersItem()
    #     #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
    #     #i['name'] = response.xpath('//div[@id="name"]').extract()
    #     #i['description'] = response.xpath('//div[@id="description"]').extract()
    #     return i
