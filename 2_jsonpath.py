import json

import requests
from jsonpath import jsonpath

"""
语法：
$             根节点位置
.             下一个位置
..            跨过层级的某个位置
"""
# data_dict= {'key1': {'key2': {'key3': {'key3': {'key3': {'key4': 'hello'}}}}}}
# value1 = jsonpath(data_dict, '$..key4')        # 返回列表
# print(value1)
# value2 = jsonpath(data_dict, '$..key3')       # 多个
# print(value2)


book_dict = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             },
            {"category": "fiction",
             "author": "Herman Melville",
             "title": "Moby Dick",
             "isbn": "0-553-21311-3",
             "price": 8.99
             },
            {"category": "fiction",
             "author": "J. R. R. Tolkien",
             "title": "The Lord of the Rings",
             "isbn": "0-395-19395-8",
             "price": 22.99
             }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}

print(jsonpath(book_dict, '$..color'))  # 车颜色
print(jsonpath(book_dict, '$..price'))  # 所有书的价格

with open('json_data.json', 'r') as f:
    dict_data = json.loads(f.read())
print(jsonpath(dict_data, '$..A..name'))
# ['安庆', '安阳', '鞍山', '安顺', '安康', '澳门', '阿克苏', '阿勒泰', '阿坝藏族羌族自治州', '阿拉善盟']


url = ' http://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
res = requests.get(url=url, headers=headers)
data_dict = res.json()
print(data_dict)
print(jsonpath(data_dict, '$..A..name'))
# ['安庆', '安阳', '鞍山', '安顺', '安康', '澳门', '阿克苏', '阿勒泰', '阿坝藏族羌族自治州', '阿拉善盟']
