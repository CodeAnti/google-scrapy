# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.headless = True


class SearchSpider(scrapy.Spider):
    name = 'searchSpider'

    allowed_domains = ['google.com']
    start_urls = ['https://www.google.com/search?q=datong+machinery',
                  'https://www.google.com/search?q=Automatic+Orange+Juice+Hot+Filling+Machine']

    def __init__(self, **kwargs):
        self.browser = webdriver.Firefox(options=firefox_options)
        super().__init__(**kwargs)

    def start_requests(self):
        url = 'https://www.google.com/search?q=datong+machinery'
        response = scrapy.Request(url, callback=self.parse)
        yield response

    def parse(self, response):
        # 置顶广告
        # content_list = response.xpath("//div[@id='tvcap']").extract()

        # 正常排序
        count = 1
        content_list = response.xpath("//div[@id='search']//div[@class='g']//div[@class='rc']//div[@class='r']/a//cite/text()").extract()
        print("=========")
        for content in content_list:
            print("网址地址:" + str(content) + ", 排名：" + str(count))
            count = count + 1
        print("=========")
        yield response

    def close(self, spider, reason):
        self.browser.quit()
