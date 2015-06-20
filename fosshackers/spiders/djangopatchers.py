# -*- coding: utf-8 -*-
import scrapy


class DjangopatchersSpider(scrapy.Spider):
    name = "djangopatchers"
    allowed_domains = ["code.djangoproject.com"]
    start_urls = (
        'https://code.djangoproject.com/query'
        '?status=assigned&status=closed&status=new'
        '&has_patch=1&desc=1&order=id',
    )

    def parse(self, response):
        pass
