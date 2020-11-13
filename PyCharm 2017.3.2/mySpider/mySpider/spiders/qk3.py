import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mySpider.items import MyspiderItem

class Qk3Spider(CrawlSpider):
    name = 'qk3'
    allowed_domains = ['https://www.qk365.com/list']
    start_urls = ['https://www.qk365.com/list/']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.qk365.com/list/p\d+'), callback='parse_item', follow=True),
    )
    # allow = (),
    # deny = (),
    # allow_domains = (),
    # deny_domains = (),
    # restrict_xpaths = (),

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        node_list = response.xpath("//p[@class='easyPage']/a/@href")
        for node in node_list:
            item = MyspiderItem()
            cprice = ''.join(node.xpath(".//span/i/text()").extract())
            print(cprice)
            position = '-'.join(node.xpath(".//p/span/a/text()").extract())
            print(position)
            href = ''.join(node.xpath("./a/@href").extract())
            print(href)
            item['cprice'] = cprice
            item['position'] = position
            item['href'] = href

        return item
# url,  需要构造请求的URL地址
# callback=None, 指定当前请求返回的response，由那一方法进行处理
# method='GET', post put head
# headers=None, 请求头
# body=None,
# cookies=None,
# meta=None, 在不同的请求中进行数据的传递
# encoding='utf-8',
# priority=0,
# dont_filter=False, 构造的请求不经过调度器过滤，如果需要多次执行相同的请求，忽略过滤
# errback=None,
# flags=None,
# cb_kwargs=None