# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random, base64
import time
from scrapy.http import HtmlResponse
from scrapy import signals
from scrapy_learn.settings import USER_AGENTS_LIST, PROXY_LIST

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium import webdriver

# 爬虫中间件
class ScrapyLearnSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 下载器中间件(常用)
class ScrapyLearnDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # 引擎将请求传给下载器之间调用

        # Must either:
        # - return None: continue processing this request       该request对象传给下载器，或传给下一个中间件(若有)
        # - or return a Response object         将response对象由引擎传给spider解析，不再发送请求即下载器的操作被截断
        # - or return a Request object          将request对象传给调度器，不再经过其他中间件
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        # 下载器完成网络请求将响应传给引擎之间调用

        # Must either;
        # - return a Response object                 通过引擎交给spider处理，或传给下一个中间件(若有)
        # - return a Request object                  通过引擎交给调取器
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 定义随机请求头用户代理中间件
class RandomUserAgentMiddleware:

    def process_request(self, request, spider):
        if spider.name == 'movie_douban':
            user_agent = random.choice(USER_AGENTS_LIST)
            request.headers['User-Agent'] = user_agent


# 随机代理ip中间件
class RandomProxyMiddleware:

    def process_request(self, request, spider):
        if spider.name == 'movie_douban':
            proxy_server = random.choice(PROXY_LIST)
            print('随机到的代理ip-----', proxy_server)
            if 'user_passwd' in proxy_server:
                # 收费代理需http基本认证
                # 账号密码进行编码
                b64_user_passwd_str = base64.b64encode(proxy_server['user_passwd'].encode()).decode()
                # 设置认证：Basic类型，空格不能少
                request.headers['Proxy-Authorization'] = 'Basic %s' % b64_user_passwd_str       #
                # 设置代理
                request.meta['proxy'] = proxy_server['ip_port']
            else:
                # 免费代理
                # 直接设置代理
                request.meta['proxy'] = proxy_server['ip_port']

        return None


class SeleniumMiddleware:
    """
    Selenium操作中间件
    """
    def process_request(self, request, spider):
        url = request.url
        if 'daydata' in url:    # 调用Selenium的条件，根据实际而定
            driver = webdriver.Chrome()     # 可采用无头模式
            driver.get(url)
            time.sleep(3)
            # driver中取渲染后的源码
            data = driver.page_source
            driver.close()

            # 创建响应对象并返回----不经过下载器直接响应
            return HtmlResponse(url=url, body=data, encoding='utf8', request=request)









