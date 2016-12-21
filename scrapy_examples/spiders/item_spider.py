# Scrap a single page and get the URL.
# The special about this example is that is using `Item` to store the data.
# Then using the `ITEM_PIPELINES` in the settings we can pipeline the data
# to the Elastic Search.

# Import scrapy library.
import scrapy
# Add extra libraries.
from scrapy import Item, Field


class PageItems(Item):
    url = Field()
    meta = Field()


class TestSpider(scrapy.Spider):
    # download_delay = 0.5
    name = 'item_spider'
    allowed_domains = [
        'example.com',
    ]

    start_urls = [
        'http://www.example.com/',
    ]

    def parse(self, response):
        item = PageItems()
        item['url'] = response.url
        item['meta'] = response.xpath('/html/head/meta[@name="viewport"]/@content').extract_first()
        return item
