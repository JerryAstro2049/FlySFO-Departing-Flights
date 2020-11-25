import scrapy


class FlySFOSpider(scrapy.Spider):
    name = 'FlySFOSpider'
    allowed_domains = ['www.flysfo.com']
    start_urls = ['https://www.flysfo.com/flight-info/flight-status/']

    def request(self):
        url = "https://www.flysfo.com/flight-info/flight-status"
        response = scrapy.Request(url, callback=self.parse)
        yield response

    def parse(self, response):
        filename = "SFO today departs.html"
        with open(filename, "wb") as f:
            f.write(response.body)
