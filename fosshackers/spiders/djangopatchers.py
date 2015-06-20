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
        # Get issue data from the main table
        for issue in response.css('.tickets.listing tbody tr'):
            yield {'id': issue.css('.id a::text').extract_first(),
                   'type': issue.css('.type::text').extract_first().strip()}

        # Get the other pages
        for page_url in response.css('.paging a::attr("href")').extract():
            yield scrapy.Request(response.urljoin(page_url))
