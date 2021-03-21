import pymysql
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlDarkSpider(CrawlSpider):
    name = 'crawl_dark'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )

    def __init__(self, name=None, **kwargs):
        super(CrawlDarkSpider, self).__init__()
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
                               password="wuhao123", database="dark_web", charset="utf8")
        cursor = conn.cursor()
        select_sql = 'select  url from test'
        cursor.execute(select_sql)
        urls = cursor.fetchall()
        for url in urls:
            print(url)
            self.start_urls.append(url[0])

    def parse_item(self, response):
        print(response)
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
