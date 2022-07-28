import scrapy

from stackOverflowCrowler.items import StackoverflowcrowlerItem


class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['dominio.exemplo.com']
    start_urls = ['https://dominio.exemplo.com/']

    def start_requests(self):
        yield scrapy.Request('https://dominio.exemplo.com/questions/11827176/', self.parse)
        yield scrapy.Request('https://dominio.exemplo.com/questions/11827175/', self.parse)
        yield scrapy.Request('https://dominio.exemplo.com/questions/11827174/', self.parse)
#        return super().start_requests()

    def parse(self, response):

        for h1 in response.xpath('//*[@id="question-header"]/h1/a').getall():
            yield StackoverflowcrowlerItem(titulo=h1)

        for href in response.xpath('//*[@id="question-header"]/h1/a').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)
