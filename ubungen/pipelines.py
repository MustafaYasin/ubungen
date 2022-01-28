# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter

from ubungen.utils.contentpath import export_order


class UbungenPipeline(object):
    def open_spider(self, spider):
        self.file = open("data.csv", 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = export_order
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
