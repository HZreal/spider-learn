import scrapy

from scrapy_learn.items import ScrapyWangYiItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do']
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_learn.pipelines.WangYiPipeline': 301,
        }
    }

    def parse(self, response):
        # 提取数据
        # table_list = response.xpath('//*[@id="position-table-35477"]/tbody/tr')    # 反爬id动态变化，不可取
        table_list = response.xpath('//*[@class="position-tb"]/tbody/tr')

        for index, table in enumerate(table_list):
            # 过滤，只有索引为偶数的tr标签才有数据
            if index % 2 == 0:
                item = ScrapyWangYiItem()
                item['name'] = table.xpath('./td[1]/a/text()').extract_first()
                # item['link'] = 'https://hr.163.com' + table.xpath('./td[1]/a/@href').extract_first()
                # response.urljoin 用于拼接相对路径为绝对路径
                item['link'] = response.urljoin(table.xpath('./td[1]/a/@href').extract_first())
                item['department'] = table.xpath('./td[2]/text()').extract_first()
                item['category'] = table.xpath('./td[3]/text()').extract_first()
                item['type'] = table.xpath('./td[4]/text()').extract_first()
                item['address'] = table.xpath('./td[5]/text()').extract_first()
                item['num'] = table.xpath('./td[6]/text()').extract_first().strip()
                item['date'] = table.xpath('./td[7]/text()').extract_first()
                # print(item)
                # yield item     # 此操作将数据返给了管道则无法做继续解析，所以此处不yield返回
                # 构造Request对象可调用callback函数对数据中的链接(即link字段)进一步解析
                # 向parse_detail方法中传递item，解析完成后返回item给引擎
                yield scrapy.Request(
                    url=item['link'],
                    callback=self.parse_detail,
                    meta={'item': item}
                )


        # 翻页url(不完整)
        part_url = response.xpath('/html/body/div[2]/div[2]/div[2]/div/a[last()]/@href').extract_first()

        # 判断终止条件
        if part_url != 'javascript:void(0)':
            # 拼接翻页完整url
            next_url = response.urljoin(part_url)

            # 构建请求对象，并返回给引擎
            # 参数callback：表示当前的url的响应交给哪个函数去处理
            # 参数meta：实现数据在不同的解析函数中传递，常用在一条数据不在同一个页面中，meta默认带有部分数据，比如下载延迟，请求深度等
            yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        """
        解析爬取表格中的链接，进行招聘详情页爬取
        :param response: 请求详情页的响应
        :return:
        """
        item = response.meta.get('item')
        print('获取parse解析中传递过来的数据--------->', item)

        # 增添详情页的数据
        item['job_duty'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/text()').extract()
        item['job_require'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/text()').extract()

        yield item




