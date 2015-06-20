# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from fosshackers.items import FosshackersItemLoader


class DjangopatcherscrawlSpider(CrawlSpider):
    name = 'djangopatcherscrawl'
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy.pipelines.files.FilesPipeline': 1
        },
        'FILES_STORE': '/tmp/djangopatches/'
    }
    allowed_domains = ['code.djangoproject.com',
                       'api.github.com']
    start_urls = [
        'https://code.djangoproject.com/query'
        '?status=assigned&status=closed&status=new'
        '&has_patch=1&desc=1&order=id',
    ]
    pr_url = ('https://api.github.com/search/issues'
              '?q=repo:django/django+in:title+type:pr'
              '+%23{issue_id}%20+%23{issue_id}%2C+%23{issue_id}%3A+%23{issue_id}%29')

    rules = (
        Rule(LinkExtractor(restrict_css='.paging a'),
             follow=True),
        Rule(LinkExtractor(restrict_css='.tickets.listing tbody .id a'),
             callback='parse_issue', follow=False),
    )

    def parse_issue(self, response):
        loader = FosshackersItemLoader(response=response)
        loader.add_css('id_', 'h2 > a::text')
        loader.add_css('type_', '.trac-type a::text')
        item = loader.load_item()

        return scrapy.Request(
            self.pr_url.format(issue_id=item['id_'][1:]),
            callback=self.parse_pr,
            meta={'item': item}
        )

    def parse_pr(self, response):
        prdata = json.loads(response.body)
        item = response.meta['item']
        item['file_urls'] = [pr['pull_request']['patch_url'] for pr in prdata['items']]
        return item
