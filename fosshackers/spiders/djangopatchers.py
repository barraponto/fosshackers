# -*- coding: utf-8 -*-
import scrapy


class DjangopatchersSpider(scrapy.Spider):
    name = "djangopatchers"
    allowed_domains = ["code.djangoproject.com"]
    start_urls = (
        'http://www.code.djangoproject.com/',
    )

    def parse(self, response):
        pass
