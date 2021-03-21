import scrapy
import pymysql


class DarkSpider(scrapy.Spider):
    name = 'dark'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://httpbin.org/get']

    # def __init__(self, name=None, **kwargs):
    #     super(DarkSpider, self).__init__()
    #     conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
    #                            password="wuhao123", database="dark_web", charset="utf8")
    #     cursor = conn.cursor()
    #     select_sql = 'select  url from test'
    #     cursor.execute(select_sql)
    #     urls = cursor.fetchall()
    #     for url in urls:
    #         print(url)
    #         self.start_urls.append(url[0])

    def parse(self, response):
        print(response.text)

