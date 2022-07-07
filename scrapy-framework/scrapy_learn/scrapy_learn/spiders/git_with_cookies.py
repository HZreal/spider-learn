import scrapy


class Git1Spider(scrapy.Spider):
    name = 'git_with_cookies'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/HZreal']
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_learn.pipelines.GitPipeline': 301,
        }
    }

    def start_requests(self):
        """
        start_requests方法默认不携带cookies
        重写用于携带cookie，请求git的profile页面
        :return:
        """
        url = self.start_urls[0]

        # 手动登录  得到的cookies
        temp = '_octo=GH1.1.1256770186.1642405527; tz=Asia%2FShanghai; _device_id=86aa549a98714e9ca1c53ef63bc6ee2a; has_recent_activity=1; user_session=cTXRCBwVyoz1LQ9NQPP-_MBMn_qjkKzqBWSOnRXNJi-hZCJz; __Host-user_session_same_site=cTXRCBwVyoz1LQ9NQPP-_MBMn_qjkKzqBWSOnRXNJi-hZCJz; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=HZreal; _gh_sess=50h1%2FEMAQ%2FVOQXtcL1YRKHXmQ0Hd%2Bl6K0trl1aPLf1BtfujNYCwCIAS7pJCwfNj9J5vmVskmDX7yE3yt3cXfiwB94Mt%2BFvgjPo6Usnw9rmZpsksmFRyWYXywzQf%2FdGtqibkOxBQs2QXPd0ZWHw4Ff08vhzZgAU%2BTPdqVKJrdOWmxl1UCvucrpPQfqxCO4wcB9KpyJnj%2BtW%2BYSjR7hxzq4t7NK7gyVaFqeu07lyqteufXyQyTmK5QP9Tcb%2BsA5vkwR5SCuq7Lm190ihWYc6mJkrTe8xvwwC7gmpePAFmVuCI4JNL%2BGAV88lM9LJahdRlXf4anGBdqrgbfMljQ8RTcx1SIQ11NQ%2Fn1S12bF%2Fz2evuXNLRCRnXwan0sFFSUl%2F86O9Kutg6uTXnSTBfdgWEgokKwuxKkHnqPTxuYP11Ww0pXi3xyDRYozF8Jv2eQfbxvXl0K%2FZiPpNqmziucyslHqlcy1Ancr%2BzuSuvouyNgmxTzk80E%2Bs%2FTiWYyM6IxcRvv5I5tIoQQKEvssidKoq3HawjvOE8Gzp%2F8ORlkuwCmABzCRy5%2BOsE7BTymdIjLKbcabxqhJEt%2F3VtxAzGIQeFvyuve7DDDIabroaWcc6aHkUHJ9DtDXMk3yuNuYF5dYmGXsiRYrWCpeX3XcJ5b6mvm9cER7XN9PtC24BcERxObbpSWJKiJkLEArQMzmLPM4qo4e9phu1NWUGzs94WdqW4KOm5oQGDLJ6%2BG3TOpFS7MADaOF6N13Kk5izSx26cfjLNCc1RuovwOgJLm3J3GFZdaf96H9jWnaDHAqMQ3iJdHr05Xgv5BuF7pFV1n%2BBTO%2F3fnHiZ1AjjC1afN7hoQOL7XeJozQ%2BS0ShefoQAsQ%2F8sTZbyLmKzBXyjRsBUIioVDsYgN%2BvlS4YdQRVV48qffmtSdonIpOzdSxpK--m1pirACcIviXPo74--Udy4U1CuBYf%2FuON3pZErug%3D%3D'

        # scrapy中cookie不能够放在headers中，在构造请求的时候有专门的cookies参数
        # 且只能够接受字典形式的coookie，故需将cookie字符串转字典
        cookies = {data.split('=')[0]: data.split('=')[-1] for data in temp.split('; ')}

        yield scrapy.Request(
            url=url,
            callback=self.parse,
            cookies=cookies
        )


    def parse(self, response):
        print('title--------------', response.xpath('/html/head/title/text()').extract_first())




















