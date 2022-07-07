# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyLearnItem(scrapy.Item):
    """
    传智播客教师模型类
    """
    name = scrapy.Field()
    level = scrapy.Field()
    description = scrapy.Field()



class ScrapyWangYiItem(scrapy.Item):
    """
    网易招聘模型类(表格及详情页)
    """
    name = scrapy.Field()
    link = scrapy.Field()
    department = scrapy.Field()
    category = scrapy.Field()
    type = scrapy.Field()
    address = scrapy.Field()
    num = scrapy.Field()
    date = scrapy.Field()

    job_duty = scrapy.Field()
    job_require = scrapy.Field()

class WangYiPlusItem(scrapy.Item):
    """
    网易招聘Plus模型类(仅表格数据)
    """
    name = scrapy.Field()
    link = scrapy.Field()
    department = scrapy.Field()
    category = scrapy.Field()
    type = scrapy.Field()
    address = scrapy.Field()
    num = scrapy.Field()
    date = scrapy.Field()


class MovieDoubanItem(scrapy.Item):
    """
    豆瓣电影
    """
    name = scrapy.Field()
    info = scrapy.Field()
    score = scrapy.Field()
    desc = scrapy.Field()

class AqiStudyItem(scrapy.Item):
    pass


if __name__ == '__main__':
    item = ScrapyLearnItem()
    item['nama'] = '王'           # 会报错 提示无此字段
    item['title'] = 'title'
    item['description'] = 'description'





