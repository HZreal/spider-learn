# tieba.baidu.com
import json
import os
import requests
from lxml import etree


URL = 'https://tieba.baidu.com/f?kw=速度与激情&ie=utf-8'
HEADERS = {
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}


class BaiduTiebaSpider():
    def __init__(self, url, headers=None):
        self.url = url or URL
        self.headers = headers or HEADERS

    @staticmethod
    def get_data(url, headers):
        response = requests.get(url, headers=headers)
        # with open('content.html', 'wb') as f:
        #     f.write(response.content)
        return response.content

    def parse_data(self, content):
        html = etree.HTML(content)
        el_list = html.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a')
        data = [{'title': el.xpath('./text()')[0], 'link': 'http://tieba.baidu.com' + el.xpath('./@href')[0]} for el in el_list]

        # 获取下一页的url
        try:
            next_url = 'https:' + html.xpath('//a[contains(text(), "下一页")]/@href')[0]
            print('next_url-------', next_url)
        except:
            next_url = None

        return data, next_url

    @staticmethod
    def save_data(i, data_list):
        print('保存每一页-------->', data_list)
        file_name = 'page_%s.json' % i
        with open(f'savedata/{file_name}', 'w') as f:
            f.write(json.dumps(data_list))

    def start(self):
        next_url = self.url
        i = 1
        while True:

            content = self.get_data(next_url, self.headers)
            data, next_url = self.parse_data(content)
            self.save_data(i, data)
            i += 1
            if not next_url:
                break
        print('end------------------')




def run(name):
    url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8'.format(name)
    headers = HEADERS
    spider = BaiduTiebaSpider(url, headers=headers)
    spider.start()


if __name__ == '__main__':
    run('速度与激情')



    # 查看保存的json文件
    # with open('savedata/page_1.json', 'r') as f:
    #     data_list = json.loads(f.read())
    #     print(data_list)
