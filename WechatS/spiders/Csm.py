# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from WechatS.items import WechatsItem

class CsmSpider(scrapy.Spider):
    name = 'Csm'
    allowed_domains = ['chuansongme.com']
    make = input("请输入公众号(非公众号名称):\n")
    start_urls = ['https://chuansongme.com/account/' + str(make) + '/hot']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.set_page_load_timeout(30)


    def closed(self, spider):
        print("spider closed")
        self.browser.close()

    def parse(self, response):
        item = WechatsItem()
        for li in response.xpath('//div[@class="pagedlist_item"]'):
            item['title'] = li.xpath('.//h2/span/a/text()').extract()[0].replace('\n','')
            item['link'] = 'https://chuansongme.com' + li.xpath('.//h2/span/a/@href').extract()[0]
            item['date'] = li.xpath('.//h2/span/span/text()').extract()
            print (item)
            yield item

# if __name__ == "__main__":
#     print("\n说明：若程序很快退出，可能是输入的信息有错\n"
#           "\nAuthor:Ctipsy\n")
#     name = input("请输入公众号名称：")
#     CsmSpider(name)
#     pages = input("\n请输入需要抓取的文章页数(<N):")
#     for i in range(int(pages)):
#         main(name, i)


