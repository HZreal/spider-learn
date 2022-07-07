import requests
import json
import js2py

# - 实现思路:
#   - 使用session发送rKey获取登录需要信息
#     - url: http://activity.renren.com/livecell/rKey
#     - 方法: get
#  获取session对象
session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/x-www-form-urlencoded"
}
# 设置session的请求头信息
session.headers = headers

response = session.get("http://activity.renren.com/livecell/rKey")
# print(response.content.decode())
n = json.loads(response.content)['data']

#   - 根据获取信息对密码进行加密
#     - 准备用户名和密码
phoneNum = "131..."
password = "****"
#     - 使用js2py生成js的执行环境:context
context = js2py.EvalJs()
#     - 拷贝使用到js文件的内容到本项目中
#     - 读取js文件的内容,使用context来执行它们
with open("BigInt.js", 'r', encoding='utf8') as f:
    context.execute(f.read())

with open("RSA.js", 'r', encoding='utf8') as f:
    context.execute(f.read())
with open("Barrett.js", 'r', encoding='utf8') as f:
    context.execute(f.read())

# - 向context环境中添加需要数据
context.t = {'password': password}
context.n = n
#     - 执行加密密码的js字符
js = '''
       t.password = t.password.split("").reverse().join(""),
       setMaxDigits(130);
       var o = new RSAKeyPair(n.e,"",n.n)
        , r = encryptedString(o, t.password);
      '''
context.execute(js)
# - 通过context获取加密后密码信息
# print(context.r)
password = context.r
#   - 使用session发送登录请求
#     - URL: http://activity.renren.com/livecell/ajax/clog
#     - 请求方法: POST
#     - 数据:
#       - phoneNum: 15565280933
#       - password: (加密后生产的)
#       - c1: 0
#       - rKey: rkey请求获取的
data = {
    'phoneNum': '131....',
    'password': password,
    'c1': 0,
    'rKey': n['rkey']
}

# print(session.headers)
response = session.post("http://activity.renren.com/livecell/ajax/clog", data=data)
print(response.content.decode())

# 访问登录的资源
response = session.get("http://activity.renren.com/home#profile")
print(response.content.decode())
