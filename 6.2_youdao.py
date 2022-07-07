import hashlib
import json
import time
import requests
import random

URL = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'


class YouDao():

    def __init__(self, word):
        self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Cookie': 'DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=1061302298@139.226.50.240; JSESSIONID=abcEiTl00YsJKcCmYoO4x; OUTFOX_SEARCH_USER_ID_NCOO=824763397.0793219; _ntes_nnid=0c76f82b69a994be2740ce3672ea321a,1641352563950; ___rl__test__cookies=1641366596119',
            'Referer': 'https://fanyi.youdao.com/?keyfrom=dict2.index',
        }
        self.word = word
        self.formdata = None

    def generate_formdata(self):
        ts = str(int(time.time() * 1000))
        # a = random.randint(0, 9)
        salt = ts + str(random.randint(0, 9))
        print(salt)

        # 会变动，根据fanyi.min.js中generateSaltSign定义
        end_str = 'Y2FYu%TNSbMCxc3t2u^XT'
        tempstr = 'fanyideskweb' + self.word + salt + end_str
        MD5 = hashlib.md5()
        MD5.update(tempstr.encode())
        sign = MD5.hexdigest()

        self.formdata = {
            'i': self.word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'lts': ts,
            'bv': 'a9c06578fcaa460614d7467f0dcef37a',
            'doctype': 'json',
            'version': 2.1,
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }

    def getdata(self):
        response = requests.post(self.url, headers=self.headers, data=self.formdata)
        # 示例响应
        demo_response_text = {
            "translateResult": [
                [
                    {
                        "tgt": "happy",
                        "src": "开心"
                    }
                ]
            ],
            "errorCode": 0,
            "type": "zh-CHS2en",
            "smartResult": {
                "entries": [
                    "",
                    "feel happy\r\n",
                    "be delighted\r\n",
                    "have a grand time\r\n"
                ],
                "type": 1
            }
        }
        return response.text

    def parsedata(self, text):
        text = json.loads(text)
        if text.get('errorCode') == 0:
            translateResult = text.get('translateResult')
            print(translateResult[0][0]['tgt'])
            print(translateResult[0][0]['src'])

            type = text.get('type')
            smartResult = text.get('smartResult')
            print(smartResult['entries'])

    def start(self):
        # url
        # headers
        # formdata
        self.generate_formdata()
        # 发送数据
        text = self.getdata()
        print(text)
        # 解析数据
        self.parsedata(text)


def run():
    youdao = YouDao('无聊')
    youdao.start()


if __name__ == '__main__':
    run()