# -*- coding: utf-8 -*-
import scrapy
from googlesearch.items import GooglesearchItem
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from urllib.parse import urlparse, parse_qs, parse_qsl
import datetime

firefox_options = Options()
firefox_options.headless = True

searchKeyWords = {
    "www.datong-machine.com": [
        "datong machinery"
    ]
}


class SearchSpider(scrapy.Spider):
    name = 'searchSpider'
    allowed_domains = ['google.com']
    start_urls = []

    def __init__(self, **kwargs):
        self.browser = webdriver.Firefox(options=firefox_options)
        super().__init__(**kwargs)

    def start_requests(self):
        # 构造start_urls
        for domain in searchKeyWords:
            for keyWord in searchKeyWords[domain]:
                start_url = 'https://www.google.com/search?q=' + keyWord.replace(" ", "+") + '&domain=' + domain
                self.start_urls.append(start_url)

        # 爬取start_urls
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        print("爬取网址:" + response.url)
        query = dict(parse_qsl(urlparse(response.url).query))
        searchDomain = query['domain']
        searchKeyWord = query['q'].replace("+", " ")

        # 广告
        # content_list = response.xpath("//div[@id='tvcap']").extract()

        # 正常排序
        rank = 0
        count = 1
        content_list = response.xpath("//div[@id='search']//div[@class='g']//div[@class='rc']//div[@class='r']/a//cite/text()").extract()
        for content in content_list:
            if rank == 0 and str(content) == searchDomain:
                rank = count
            print("网址地址:" + str(content) + ", 排名：" + str(count))
            count = count + 1

        print("=========")
        print("搜索关键字:" + searchKeyWord)
        print("匹配域名:" + searchDomain)
        print("排名:" + str(rank))
        print("=========")

        item = GooglesearchItem()
        item['keywords'] = searchKeyWord
        item['domain'] = searchDomain
        item['rank'] = rank
        item['created_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        item['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        yield item

    # def close(self, spider, reason):
    #     # self.browser.quit()
