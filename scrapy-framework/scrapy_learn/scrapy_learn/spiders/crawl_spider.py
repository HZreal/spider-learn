import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# CrawlSpider应用于数据在一个页面上的采集情况，性能更高，但无法传递meta参数，因为他是根据规则提取器自动发送请求，
# 如果数据在多个页面上且有关联，需要把多个页面上的数据拼全，通常使用原来的spider类

# 创建命令  scrapy genspider - t crawl crawl_spider tencent.com

class CrawlSpiderSpider(CrawlSpider):
    name = 'crawl_spider'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do']
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_learn.pipelines.CrawlSpiderLearnPipeline': 301,
        }
    }

    # 定义规则(每个规则即一个Rule类)
    rules = (
        # 使用Rule类生成链接提取规则对象,从response中提取符合规则的链接
        # 参数LinkExtractor 链接提取器，使用allow参数，接收正则url
        # le = LinkExtractor(allow='jobdesc.html\?postId=\d+')
        # le.extract_links(response) 返回Link对象列表
        # 参数follow 决定是否在链接提取器的链接对应的响应中继续应用链接提取器提取链接

        # 设置详情页面链接提取规则, follow为False即详情页中不再应用链接提取规则
        Rule(LinkExtractor(allow=r'/position/detail.do\?id=\d+'), callback='parse_item', follow=False),
        # 设置翻页链接提取规则, follow为True即翻页后继续应用链接提取规则
        Rule(LinkExtractor(allow=r'\?currentPage=\d+'), callback='parse_page_item', follow=True),
    )

    def parse_item(self, response):
        print('detail--------', response.url)
        item = {
            'job_duty': response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/text()').extract(),
            'job_require': response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/text()').extract()
        }

        yield item

    def parse_page_item(self, response):
        """
        翻页不需要此callback函数，仅为了查看url
        """
        print('page--------', response.url)
