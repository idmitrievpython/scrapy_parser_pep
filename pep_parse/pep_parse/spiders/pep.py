import re
import scrapy

from pep_parse.items import PepParseItem

from pep_parse.constants import DOMAIN, PATTERN, START_URL


class PepSpider(scrapy.Spider):

    name = 'pep'
    allowed_domains = DOMAIN
    start_urls = START_URL

    def parse(self, response):
        pep_common_list = response.xpath('//*[@id="numerical-index"]')
        pep_links = pep_common_list.css(
            'a.pep.reference.internal::attr(href)'
        ).getall()
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': re.search(
                PATTERN,
                response.css('h1.page-title::text').get()
            ).groups(),
            'name': response.css('h1.page-title::text').get(),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)
