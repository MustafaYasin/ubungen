import re
import scrapy
from scrapy.loader import ItemLoader
from ubungen.items import UbungenItem
from ubungen.utils.contentpath import name_to_xpath_mapper


class UbungenSpider(scrapy.Spider):
    name = "ubungen"
    start_urls = ["https://www.uebungen.ws/"]

    def __init__(self, min_votes = 1000, *args, **kwargs):
        super(UbungenSpider, self).__init__(*args, **kwargs)
        self.min_votes = int(min_votes)

    def parse(self, response):
        for muscle in response.xpath('//a[@class="auswahlboxlink"]/@href').extract():
            yield scrapy.Request(muscle, callback=self.parse_auswahlbox)

    def parse_auswahlbox(self, response):
        for katauswahlbox in response.xpath('//a[@class="katauswahlboxlink"]/@href').extract():
            yield scrapy.Request(katauswahlbox, callback=self.parse_list_of_exercises)

    def parse_list_of_exercises(self, response):
        for exercise in response.xpath('//h3[@class="content-list-title"]/a/@href').extract():
            yield scrapy.Request(exercise, callback=self.call_exercises)

    '''
    def fetch_movie(self, response):
        item_loader = ItemLoader(item=UbugenItem(), response=response)

        for name, xpath in name_to_xpath_mapper.items():
            item_loader.add_xpath(name, xpath)

        yield item_loader.load_item()
        next_page = response.xpath('//div[@class = "nav"]/div[@class = "desc"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback= self.fetch_movie)
    '''
        
    
    def call_exercises(self, response):
        muscle_group = response.xpath('//nav[@class="breadcrumb"]/a/text()').extract_first()
        subset_muscles = response.xpath('//nav[@class="breadcrumb"]/span/a/span/text()').extract()[1]
        exercise_title = response.xpath('//h1[@class="entry-title"]/text()').extract_first()
        muscle_description_title = response.xpath('//div[@class="entry-content clearfix"]/h2/text()').extract_first()
        TAG_RE = re.compile(r'<[^>]+>')
        muscle_description = response.xpath('//div[@class="entry-content clearfix"]/p').extract_first()
        muscle_description = TAG_RE.sub('', muscle_description)
        exercise_execution_title = response.xpath('//div[@class="entry-content clearfix"]/h2/text()').extract()[1]
        #exercise_execution = 


