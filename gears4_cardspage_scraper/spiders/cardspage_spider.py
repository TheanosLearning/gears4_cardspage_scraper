import scrapy
import json


class CardsPageSpider(scrapy.Spider):
    name = "cardspage"

    def start_requests(self):
        urls = [
            'https://gearsofwar.com/en-us/cards'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filenames = ['initialState', 'text']
        for filename in filenames:
            with open('data/' + filename + '.json' , 'w') as f:
                payload = response.xpath('//*[@id="' + filename + '"]/text()').extract_first()
                f.write(json.dumps(json.loads(payload), indent=4))
            self.log('Saved file %s' % filename)