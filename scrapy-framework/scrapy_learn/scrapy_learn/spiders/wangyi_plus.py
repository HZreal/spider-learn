import scrapy

from scrapy_learn.items import WangYiPlusItem


class WangyiPlusSpider(scrapy.Spider):
    name = 'wangyi_plus'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do']
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_learn.pipelines.WangYiPlusPipeline': 302,
            'scrapy_learn.pipelines.MongoPipeline': 303,
        }
    }

    def parse(self, response):
        # 提取数据
        table_list = response.xpath('//*[@class="position-tb"]/tbody/tr')

        for index, table in enumerate(table_list):
            if index % 2 == 0:
                item = WangYiPlusItem()
                item['name'] = table.xpath('./td[1]/a/text()').extract_first()
                item['link'] = response.urljoin(table.xpath('./td[1]/a/@href').extract_first())
                item['department'] = table.xpath('./td[2]/text()').extract_first()
                item['category'] = table.xpath('./td[3]/text()').extract_first()
                item['type'] = table.xpath('./td[4]/text()').extract_first()
                item['address'] = table.xpath('./td[5]/text()').extract_first()
                item['num'] = table.xpath('./td[6]/text()').extract_first().strip()
                item['date'] = table.xpath('./td[7]/text()').extract_first()
                yield item


        # 翻页
        part_url = response.xpath('/html/body/div[2]/div[2]/div[2]/div/a[last()]/@href').extract_first()

        # 判断终止条件
        if part_url != 'javascript:void(0)':
            next_url = response.urljoin(part_url)
            yield scrapy.Request(url=next_url, callback=self.parse)

