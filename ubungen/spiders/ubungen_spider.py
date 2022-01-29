import re
import scrapy
import pprint
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



    def call_exercises(self, response):
        name_to_xpath_mapper = {
            'muscle_group': 'response.xpath(\'//nav[@class="breadcrumb"]/a/text()\').extract_first()',
            'subset_muscles': 'response.xpath(\'//nav[@class="breadcrumb"]/span/a/span/text()\').extract()[1]',
            'exercise_title': 'response.xpath(\'//h1[@class="entry-title"]/text()\').extract_first()',
            'muscle_description_title': 'response.xpath(\'//div[@class="entry-content clearfix"]/h2/text()\').extract_first()',
            'muscle_description': 'response.xpath(\'//div[@class="entry-content clearfix"]/p\').extract_first()',
            'exercise_execution_title': 'response.xpath(\'//div[@class="entry-content clearfix"]/h2/text()\').extract()[1]',

        }


        export_order = ["movie_name", "muscle_group", "subset_muscles", "exercise_title", "muscle_description_title",
                        "muscle_description", "exercise_execution_title"]
        for xpath in name_to_xpath_mapper.values():
            yield {
                'muscle_group': xpath,
                #'subset_muscles' : response.xpath('//nav[@class="breadcrumb"]/span/a/span/text()').extract()[1]
                #name : response.xpath('//h1[@class="entry-title"]/text()').extract_first()
                #name : response.xpath('//div[@class="entry-content clearfix"]/h2/text()').extract_first()
                #name : response.xpath('//div[@class="entry-content clearfix"]/p').extract_first()

            }





