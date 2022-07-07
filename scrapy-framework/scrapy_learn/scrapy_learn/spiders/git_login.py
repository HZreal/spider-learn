import scrapy
username = ''
password = ''

class GitLoginSpider(scrapy.Spider):
    name = 'git_login'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_learn.pipelines.GitPipeline': 301,
        }
    }

    def parse(self, response):
        # 获取post body
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        # trusted_device = response.xpath('//input[@name="trusted_device"]/@value').extract_first()
        # allow_signup = response.xpath('//input[@name="allow_signup"]/@value').extract_first()
        # client_id = response.xpath('//input[@name="client_id"]/@value').extract_first()
        # integration = response.xpath('//input[@name="integration"]/@value').extract_first()
        required_field_ = response.xpath('//input[contains(@name, "required_field_")]/@name').extract_first()
        webauthn_support = response.xpath('//input[@name="webauthn-support"]/@value').extract_first()
        webauthn_iuvpaa_support = response.xpath('//input[@name="webauthn-iuvpaa-support"]/@value').extract_first()
        print('get-supported------------', webauthn_support, webauthn_iuvpaa_support)
        return_to = response.xpath('//input[@name="return_to"]/@value').extract_first()
        timestamp = response.xpath('//input[@name="timestamp"]/@value').extract_first()
        timestamp_secret = response.xpath('//input[@name="timestamp_secret"]/@value').extract_first()

        post_body = {
            'commit': 'Sign in',
            'authenticity_token': authenticity_token,
            'login': username,
            'password': password,
            'webauthn-support': 'supported',
            'webauthn-iuvpaa-support': 'supported',
            'timestamp': timestamp,
            'timestamp_secret': timestamp_secret,
            # 下面暂可不传
            'return_to': return_to,
            'trusted_device': '',              # 无值时为空串，而不能是None
            'allow_signup': '',
            'client_id': '',
            'integration': '',
            # 'required_field_44de': '',       # 键是动态变化的

        }
        # 注意：没有数据时写空串，而不能是None，否则报错TypeError: to_bytes must receive a str or bytes object, got NoneType
        post_body.update({required_field_: ''})
        print('post_body------------->', post_body)

        # 方法一：构造FormRequest对象，需要详细写表单body信息
        # yield scrapy.FormRequest(
        #     # 提交地址
        #     url='https://github.com/session',
        #     # 提交的数据
        #     formdata=post_body,
        #     # 响应回调
        #     callback=self.after_login,
        #     # dont_filter=False           # 请求是否过滤，每个request对象都有dont_filter参数，用于判断此请求是否被过滤处理
        # )
        # 方法二：以表单的方式提交数据，只需用户名密码，更简洁方便
        yield scrapy.FormRequest.from_response(
            response=response,
            formdata={'login': username, 'password': password},
            callback=self.after_login,
        )

    def after_login(self, response):
        print('--------------------after_login----------------------')
        # 登录后请求profile页面，会自动携带cookies进行请求
        yield scrapy.Request(
            url='https://github.com/HZreal',
            callback=self.check_login
        )

    def check_login(self, response):
        print('--------------------check_login-----------------------')
        # 请求profile页面成功的处理
        print('title-------------->', response.xpath('/html/head/title/text()').extract_first())
