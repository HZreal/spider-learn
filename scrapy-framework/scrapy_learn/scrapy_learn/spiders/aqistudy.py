import time

import scrapy


class AqistudySpider(scrapy.Spider):
    name = 'aqistudy'
    allowed_domains = ['aqistudy.cn']
    start_urls = ['https://aqistudy.cn/historydata']
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_learn.pipelines.AqiStudyPipeline': 306,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_learn.middlewares.SeleniumMiddleware': 546,
        }
    }

    def parse(self, response):
        """
        解析响应，进入某个城市页面
        :param response:
        :return:
        """
        url_list = response.xpath('').extract()

        for url in url_list[20: 23]:
            city_url = response.urljoin(url)
            yield scrapy.Request(url=city_url, callback=self.parse_month)

    def parse_month(self, response):
        """
        解析某个城市的某月数据，并进入月份中的某天
        :param response:
        :return:
        """
        url_list = response.xpath('').exract()

        for url in url_list[12: 15]:
            month_url = response.urljoin(url)
            yield scrapy.Request(url=month_url, callback=self.parse_day)

    def parse_day(self, response):
        """
        解析某个城市某月的某天数据，但是发现数据是经过js渲染的
        故需要借助Selenium打开该城市此月此天的页面，待数据加载完成后获取源码数据再进行解析，即使用中间件对此url进行特别处理
        :param response:
        :return:
        """
        node_list = response.xpath('')
        city = response.xpath().extract_first().split()  # 城市名

        for node in node_list:
            item = {}
            item['city'] = city
            item['url'] = response.url
            item['timestamp'] = time.time()
            item['date'] = node.xpath().extract_first()
            item['AQI'] = node.xpath().extract_first()
            item['LEVEL'] = node.xpath().extract_first()
            item['PM2.5'] = node.xpath().extract_first()


            yield item
