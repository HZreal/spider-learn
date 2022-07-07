# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from pymongo import MongoClient
from itemadapter import ItemAdapter

# 不同的pipeline可以处理不同爬虫的数据
# 不同的pipeline能够对一个或多个爬虫进行不同的数据处理的操作，比如一个进行数据清洗，一个进行数据的保存
# 同一个管道类也可以处理不同爬虫的数据，通过spider.name属性来区分
# pipeline在setting中键表示位置(即pipeline在项目中的位置可以自定义)，值表示距离引擎的远近，越近数据会越先经过：**权重值小的优先执行**


# 定义数据处理的管道类，需要在settings.py中配置启用
class ScrapyLearnPipeline:
    """
    管道类
    """
    def __init__(self):
        self.file = open('_item.json', 'w')

    def process_item(self, item, spider):
        """
        数据操作,重写方法
        :param item: 爬取的数据
        :param spider: 爬虫实例对象
        :return: 将数据返回给引擎
        """
        # print(item, spider)
        if spider.name == 'itcast':
            # 传过来的item为ScrapyLearnItem模型类，不能JSON序列号，需强转成字典
            # item = item.__dict__
            print('item------->', item, '\ndict------->', item.__dict__)
            item = dict(item)

            # 写入文件
            self.file.write(json.dumps(item, ensure_ascii=False) + ',\n')


        # 默认调用管道结束，将数据返给下一个管道(若有)或引擎
        return item

    def __del__(self):
        self.file.close()


class WangYiPipeline:
    """
    网易招聘管道
    """
    def __init__(self):
        self.file = open('_wangyi.json', 'w')

    def process_item(self, item, spider):
        """
        网易招聘数据操作
        :param item:
        :param spider:
        :return:
        """
        if spider.name == 'wangyi':
            item = dict(item)
            print('item---------', item)
            self.file.write(json.dumps(item, ensure_ascii=False) + ',\n')

        return item

    def __del__(self):
        self.file.close()


class GitPipeline:
    """
    Git login
    """
    def process_item(self, item, spider):
        return item


class WangYiPlusPipeline:
    """
    网易Plus
    """
    def open_spider(self, spider):
        # 在爬虫开启的时候仅执行一次
        if spider.name == 'wangyi_plus':
            self.file = open('_wangyi_plus.json', 'w')

    def process_item(self, item, spider):
        if spider.name == 'wangyi_plus':
            item = dict(item)
            print('item---------', item)
            self.file.write(json.dumps(item, ensure_ascii=False) + ',\n')

        # 返给下一个管道(若有)或引擎
        return item

    def close_spider(self, spider):
        # 在爬虫关闭的时候仅执行一次
        if spider.name == 'wangyi_plus':
            self.file.close()


class MongoPipeline:
    """
    MongoDB
    """
    def __init__(self):
        self.mongo_client = MongoClient()

    def open_spider(self, spider):
        if spider.name == 'wangyi_plus':
            self.db = self.mongo_client.get_database('test')
            self.collection = self.db.get_collection('wangyi')

    def process_item(self, item, spider):
        if spider.name == 'wangyi_plus':
            print('item----mongo----------', item)
            # 经过上一个管道已经转成字典，此处无需再转
            # item = dict(item)
            self.collection.insert_one(item)

        return item

    def close_spider(self, spider):
        if spider.name == 'wangyi_plus':
            self.mongo_client.close()


class CrawlSpiderLearnPipeline:
    """
    CrawlSpider爬虫类
    """
    def __init__(self):
        self.file = open('_wangyi.json', 'w')

    def process_item(self, item, spider):
        self.file.write(json.dumps(item, ensure_ascii=False) + ',\n')
        return item

    def __del__(self):
        self.file.close()


class MovieDoubanPipeline:
    """
    豆瓣电影
    """
    def open_spider(self, spider):
        if spider.name == 'movie_douban':
            self.file = open('movie_douban.json', 'w')

    def process_item(self, item, spider):
        if spider.name == 'movie_douban':
            # ScrapyLearnItem模型类强转字典
            item = dict(item)
            self.file.write(json.dumps(item, ensure_ascii=False) + ',\n')
        return item

    def close_spider(self, spider):
        if spider.name == 'movie_douban':
            self.file.close()


class AqiStudyPipeline:
    def process_item(self, item, spider):
        print('-----------')
        return item



