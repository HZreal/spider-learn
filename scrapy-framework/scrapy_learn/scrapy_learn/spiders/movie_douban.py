import scrapy

from scrapy_learn.items import MovieDoubanItem


class MovieDoubanSpider(scrapy.Spider):
    name = 'movie_douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_learn.pipelines.MovieDoubanPipeline': 305,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_learn.middlewares.RandomUserAgentMiddleware': 544,
            'scrapy_learn.middlewares.RandomProxyMiddleware': 545,
        }
    }

    def parse(self, response):
        # print('请求头user-agent', response.request.headers.get('User-Agent'))
        movie_list = response.xpath('//*[@class="info"]')
        print(len(movie_list))

        for movie in movie_list:
            item = MovieDoubanItem()
            item['name'] = movie.xpath('./div[1]/a/span[1]/text()').extract_first()
            item['info'] = movie.xpath('./div[2]/p[1]/text()').extract_first().strip()
            item['score'] = movie.xpath('./div[2]/div/span[2]/text()').extract_first()
            item['desc'] = movie.xpath('./div[2]/p[2]/span/text()').extract_first()

            yield item

        # 下一页
        url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if url != None:
            next_url = response.urljoin(url)
            yield scrapy.Request(
                url=next_url,
                callback=self.parse
            )


