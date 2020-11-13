import scrapy
from mySpider.items import MyspiderItem



class QkSpider(scrapy.Spider):
    name = 'qk'
    allowed_domains = ['www.qk365.com']
    start_urls = ['https://www.qk365.com/list']

    def parse(self, response):
        print('####################################')
        # print(response.text)
        # print(response.xpath("//span/i/text()"))
        # list_itme = []
        node_list = response.xpath("//ul[@class='easyList']/li")
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
            yield scrapy.Request(url=href, callback=self.href_secondpage, meta={'item': item})
            # list_itme.append(item)
            # yield item

        # return list_itme

    def href_secondpage(self, response):
        item = response.meta['item']
        print('*****************************')
        price = ''.join(response.xpath("//div[@class='survey-left fL']/dd[1]/text()").extract())
        print(price)
        roomnum = ''.join(response.xpath("//div[@class='survey-right fR']/dd[1]/text()").extract())
        print(roomnum)
        item['price'] = price
        item['roomnum'] = roomnum
        yield item