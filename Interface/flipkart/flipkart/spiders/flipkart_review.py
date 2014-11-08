from scrapy.spider import Spider
from scrapy.item import Item, Field
from scrapy.selector import Selector
from link import *

class FeatureItem(Item):
   # title = Field()
   # link = Field()
   reviews = Field()

class FeatureSpider(Spider):
   name = "flipkart_review"
   allowed_domains = ["www.flipkart.com"]
   start_urls = [input_link]
   # "http://www.flipkart.com/nikon-d5100-dslr-camera/product-reviews/ITMDUZHMEYJH2ZEC",


   def parse(self, response):
       sel = Selector(response)
       item = FeatureItem()
       # item['title'] = sel.css('.title::text').extract()
       # item['link'] = response.url
       item['reviews'] = sel.css('.review-text::text').extract()
       return item
