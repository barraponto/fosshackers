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
        for issue_url in response.css('.tickets.listing tbody .id a::attr("href")').extract():
            yield scrapy.Request(response.urljoin(issue_url),
                                 callback=self.parse_issue)

        # Get the other pages
        for page_url in response.css('.paging a::attr("href")').extract():
            yield scrapy.Request(response.urljoin(page_url))

    def parse_issue(self, response):
        return {'id': response.css('h2 > a::text').extract_first(),
                'type': response.css('.trac-type a::text').extract_first()}
