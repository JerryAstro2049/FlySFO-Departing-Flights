import scrapy

from Crawler.items import FlightItem


class FlySFOSpider(scrapy.Spider):
    name = 'FlySFO'
    allowed_domains = ['www.flysfo.com']
    start_urls = ['https://www.flysfo.com/flight-info/flight-status/']

    def request(self):
        url = 'https://www.flysfo.com/flight-info/flight-status'
        response = scrapy.Request(url, callback=self.parse)

        yield response

    def parse(self, response):
        filename = 'SFO today departs.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        flights = response.xpath('//*[@id="flight_results"]/tbody/tr').getall()

        for flight in flights:
            flight_item = FlightItem()

            flight_obj = scrapy.Selector(text=flight)
            airline = "" if flight_obj.xpath('//td[1]/span[1]/text()').get() is None \
                else flight_obj.xpath('//td[1]/span[1]/text()').get()
            departing_to = "" if flight_obj.xpath('//td[2]/text()').get() is None \
                else flight_obj.xpath('//td[2]/text()').get()
            flight = "" if flight_obj.xpath('//td[3]/text()').get() is None \
                else flight_obj.xpath('//td[3]/text()').get()
            scheduled = "" if flight_obj.xpath('//td[4]/text()').get() is None \
                else flight_obj.xpath('//td[4]/text()').get()
            estimated = "" if flight_obj.xpath('//td[5]/text()').get() is None \
                else flight_obj.xpath('//td[5]/text()').get()
            remarks = "" if flight_obj.xpath('//td[6]/text()').get() is None \
                else flight_obj.xpath('//td[6]/text()').get()
            terminal = "" if flight_obj.xpath('//td[7]/text()').get() is None \
                else flight_obj.xpath('//td[7]/text()').get()
            gate = "" if flight_obj.xpath('//td[8]/text()').get() is None \
                else flight_obj.xpath('//td[8]/text()').get()

            flight_item['Airline'] = airline
            flight_item['DepartingTo'] = departing_to
            flight_item['Flight'] = flight
            flight_item['Scheduled'] = scheduled
            flight_item['Estimated'] = estimated
            flight_item['Remarks'] = remarks
            flight_item['Terminal'] = terminal
            flight_item['Gate'] = gate

            yield flight_item
