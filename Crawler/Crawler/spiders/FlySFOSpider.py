import scrapy


class FlySFOSpider(scrapy.Spider):
    name = 'FlySFO'
    allowed_domains = ['www.flysfo.com']
    start_urls = ['https://www.flysfo.com/flight-info/flight-status/']

    def request(self):
        url = "https://www.flysfo.com/flight-info/flight-status"
        response = scrapy.Request(url, callback=self.parse)
        yield response

    def parse(self, response):
        flights = response.xpath('//*[@id="flight_results"]/tbody').get()

        try:
            filename = 'SFO today departs.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(flights)
        except TypeError:
            print('didn\'t get the flights')
