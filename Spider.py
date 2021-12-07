import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
import hashlib
import requests
class MySpider(CrawlSpider):
    name = "reanes-student"
    start_urls = [
        'https://en.wikipedia.org/wiki/Computer_science'
    ]
    rules = [
        Rule(LinkExtractor(allow_domains =['en.wikipedia.org'], unique=True), callback = 'parse_items', follow = True)
    ]
    def parse_items(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        entry = dict.fromkeys(['pageid', 'url', 'title', 'body'])
        entry['pageid'] = hashlib.md5(response.request.url.encode()).hexdigest()
        entry['url'] = response.request.url
        entry['title'] = response.css('title::text').get()
        entry['body'] = soup.get_text()
        yield entry
    