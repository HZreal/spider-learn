import requests
from requests.utils import dict_from_cookiejar

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
kw = {

}
response = requests.get(url='', params=kw, headers=header)


# cookie
cookies = {

}
res = requests.get(url='', cookies=cookies, timeout=3)
cookieJar_obj = response.cookies
cookie_dict = dict_from_cookiejar(cookieJar_obj)    # return dict

# proxy
proxies = {
    "http": "http://12.34.56.79:9527",
    "https": "https://12.34.56.79:9527"
}
resp = requests.get(url='', proxies=proxies, verify=False)



# session:
# 自动处理cookie，即 **下一次请求会带上前一次的cookie**
# 自动处理连续的多次请求过程中产生的cookie
session = requests.session()
session.get(url='')
session.post(url='')