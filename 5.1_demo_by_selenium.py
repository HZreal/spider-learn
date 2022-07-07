# 斗鱼直播demo       to use selenium
import json
import time

from selenium import webdriver

URL = 'https://www.douyu.com/directory/all'


class DouYuSpider():
    def __init__(self, url):
        self.url = url or URL
        self.driver = webdriver.Chrome()

    def parse_data(self):
        room_list = self.driver.find_elements(by='xpath', value='//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        print(len(room_list))

        data_list = []
        i = 1
        for room in room_list:
            temp = {}
            link = room.find_element(by='xpath', value='./a/div[1]/div[1]/picture/img').get_attribute('src'),
            print(f'---------第{i}个----------', link)
            temp['cover_picture_link'] = link
            data_list.append(temp)
            print(data_list)
            i += 1

        # data_list = [{
        #     'title': room.find_element(by='xpath', value='./a/div[2]/div[1]/h3').text,
        #     'type': room.find_element(by='xpath', value='./a/div[2]/div[1]/span').text,
        #     'owner': room.find_element(by='xpath', value='./a/div[2]/div[2]/h2/div').text,
        #     'hot': room.find_element(by='xpath', value='./a/div[2]/div[2]/span').text,
        #     'cover_picture_link': room.find_element(by='xpath', value='./a/div[1]/div[1]/picture/img').get_attribute('src'),
        # } for room in room_list]

        print('data_list------------------', data_list)
        print('data_list.length-----------', len(data_list))
        return data_list

    @staticmethod
    def save_data(data_list):
        print('save_data-------------------')
        with open('douyu.json', 'w') as f:
            f.write(json.dumps(data_list))

    def start(self):
        self.driver.get(self.url)
        time.sleep(5)
        # self.driver.execute_script('scrollTo(0, 1000000)')
        # time.sleep(5)
        data_list = self.parse_data()
        # self.save_data(data_list)

        print('end-----------------------------------------------')


def run():
    douyu = DouYuSpider(url=URL)
    douyu.start()
    time.sleep(10)


if __name__ == '__main__':
    run()






















