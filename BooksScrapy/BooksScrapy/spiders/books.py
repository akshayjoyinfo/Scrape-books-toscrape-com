import scrapy
from BooksScrapy.items import BookItem
from scrapy.loader import ItemLoader


class BooksSpider(scrapy.Spider):
    name = 'books'

    start_urls = [
        'http://books.toscrape.com/'
    ]

    def parse(self, response):
        for book in response.xpath("//section/div/ol[@class='row']/li"):
            l = ItemLoader(item=BookItem(), selector=book)
            l.add_xpath('book', ".//article[@class='product_pod']/h3/a/@title")
            l.add_xpath('price', ".//article[@class='product_pod']/div[@class='product_price']/p["
                                 "@class='price_color']/text()")
            yield l.load_item()

        next_page = response.xpath("//section/div/div//ul[@class='pager']/li[@class='next']/a/@href").extract_first()

        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
