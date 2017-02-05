# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector

from anjuke.items import AnjukeItem

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class AnjukeSpider(CrawlSpider):

    name = "Anjuke"
    start_urls = ['http://sh.zu.anjuke.com/fangyuan/huacao/fx3//']

    def parse(self, response):

        item = AnjukeItem()
        selector = Selector(response)

        infos = selector.xpath('//div[@class="zu-itemmod  "]')

        for info in infos:
            url = info.xpath('a/@href').extract()
            item['url'] = url

            price = info.xpath('div[2]/p/strong/text()').extract()
            item['price']= price

            roomType = info.xpath('div[1]/p[1]/text()[1]').extract()
            item['roomType']= roomType

            rentType = info.xpath('div[1]/p[1]/text()[2]').extract()
            item['rentType']= rentType

            decoration = info.xpath('div[1]/p[1]/text()[3]').extract()
            item['decoration']= decoration

            floor = info.xpath('div[1]/p[1]/text()[4]').extract()
            item['floor']= floor

            area = info.xpath('div[1]/address/a/text()').extract()
            if len(area):
                item['area']= area[0].strip()

            address = info.xpath('div[1]/address/text()').extract()
            if len(address) > 1:
                item['address']= address[1].strip()

            title = info.xpath('div[1]/h3/a/text()').extract()
            item['title']= title

            yield item

        for i in range(2,14):
            nexturl = 'http://sh.zu.anjuke.com/fangyuan/huacao/fx3-p%s/'%i

            yield Request(nexturl,callback=self.parse)