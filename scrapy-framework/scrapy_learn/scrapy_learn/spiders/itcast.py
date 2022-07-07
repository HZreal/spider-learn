import json
import scrapy
from scrapy_learn.items import ScrapyLearnItem

# 命令创建爬虫--->  scrapy genspider itcast itcast.cn
# 运行爬虫     scrapy crawl itcast


class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = 'itcast'
    # 允许的域
    allowed_domains = ['itcast.cn']
    # 初始url
    start_urls = [
        'http://www.itcast.cn/channel/teacher.shtml']  # 由于继承了Spider, 会自动读取start_urls, 生成request, 发送给调度器Schedule
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_learn.pipelines.ScrapyLearnPipeline': 300,
        }
    }

    def parse(self, response):
        """
        爬虫类必须有此parse函数  定义对网站的相关操作
        :param response: 下载器请求目标网站后，返回的scrapy响应类
        :return: 只能返回BaseItem, Request, dict, None
        """

        # print('scrapy响应类response------------>', response)
        # print(response.url)
        # print(response.request.url)
        # print(response.headers)
        # print(response.requests.headers)
        # print(response.requests.headers)
        # print(response.body)   # 响应体，也就是html代码，byte类型
        # print(response.status)

        teachers = response.xpath("//div[@class='li_txt']")
        print('教师数量------------', len(teachers))


        # 在scrapy中使用xpath语法得到的是一个Selector对象列表
        # 例如 teacher.xpath('./h3/text()') 返回的是 [<Selector xpath='./h3/text()' data=''韩老师>]
        # xpath确认取到的是多值列表时用extract；取不到值时为空列表，会报索引错误，此时使用extract_first不报错设置值为空；
        # teacher_list = [{
        #     'name': teacher.xpath('./h3/text()')[0].extract(),
        #     # {'name': teacher.xpath('./h3/text()').extract_first(),
        #     'level': teacher.xpath('./h4/text()').extract_first(),
        #     'description': teacher.xpath('./p/text()').extract_first()
        # } for teacher in teachers]
        # print(teacher_list[0])
        # with open('itcast_teacher.json', 'w') as f:
        #     f.write(json.dumps(teacher_list))
        # return teacher_list

        for teacher in teachers:
            # item = {}
            item = ScrapyLearnItem()

            item['name'] = teacher.xpath('./h3/text()')[0].extract(),
            item['level'] = teacher.xpath('./h4/text()').extract_first(),
            item['description'] = teacher.xpath('./p/text()').extract_first(),
            yield item

