import time
from selenium import webdriver

# 原理剖析
# 浏览器的驱动程序webdriver是原生浏览器API的封装，其他浏览器也有自己的webdriver驱动
# 下载的谷歌webdriver是谷歌浏览器的驱动程序，即谷歌浏览器提供的操作命令API
# python通过调用selenium库去操作谷歌webdriver，从而操作谷歌浏览器


# 此时启动了谷歌webdriver服务器，通过调用webdriver的API来操作谷歌浏览器(如启动关闭，截屏，安装插件，配置证书，定位元素等)
driver = webdriver.Chrome()
# 指定webdriver的路径，加入系统环境变量则不需指定
# driver = webdriver.Chrome(executable_path='')



# 一、driver对象常用属性及方法：
# driver.get(url='http://www.baidu.com/')
# 当前标签页浏览器渲染之后的网页源码
# print(driver.page_source)
# 当前标签页的url(浏览器响应的url)，不一定是请求url，比如请求http://www.baidu.com，实际被重定向到https://www.baidu.com 这才是浏览器响应的url
# print(driver.current_url)
# 页面标题
# print(driver.title)
# time.sleep(3)

# driver.find_element_by_id('kw').send_keys('python')
# driver.find_element_by_id('su').click()

# driver.get('http://www.douban.com')
# time.sleep(3)

# driver.back()
# time.sleep(3)

# driver.forward()
# time.sleep(2)

# 页面截图
# driver.save_screenshot('baidu.png')



# 二、定位标签元素获取标签对象：
# driver.find_element_by_*()      返回匹配到的第一个WebElement对象，匹配不到会报错，现在被弃用但仍可使用
# driver.find_elements_by_*()     返回匹配到的第一个WebElement对象的列表，匹配不到返回空列表，现在被弃用但仍可使用

# 目前定位元素统一成find_element(s)返回元素对象(列表)
# driver.find_element(by='xpath', value='//*[@id="kw"]')           # 返回WebElement对象 匹配不到会报错
# driver.find_elements(by='xpath', value='//*[@id="kw"]')          # 返回WebElement对象的列表  匹配不到返回空列表

# 根据xpath进行定位
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
# driver.find_element(by='xpath', value='//*[@id="kw"]').send_keys('python')
# driver.find_elements(by='xpath', value='//*[@id="kw"]')[0].send_keys('python')
# 根据css选择器进行定位
# driver.find_element_by_css_selector('#kw').send_keys('python')
# driver.find_element(by='css', value='#kw').send_keys('python')
# 根据标签中name属性值进行定位
# driver.find_element_by_name('wd').send_keys('python')
# driver.find_element(by='name', value='wd').send_keys('python')
# 根据标签中class属性值进行定位
# driver.find_element_by_class_name('s_ipt').send_keys('python')
# driver.find_element(by='class name', value='s_ipt').send_keys('python')

# 点击搜索
# driver.find_element_by_id(id_='su').click()
# driver.find_element(by='id', value='su').click()

# 根据可点击的链接文本进行定位
# driver.find_element(by='link text', value='hao123').click()
# driver.find_element(by='link text', value='hao').click()                     # 报错，因为页面上没有'hao'这个链接文本
# driver.find_element(by='partial link text', value='hao').click()             # 匹配到'hao'即可


# 批量定位标签元素：
driver.get('https://tieba.baidu.com/f?kw=%E9%80%9F%E5%BA%A6%E4%B8%8E%E6%BF%80%E6%83%85&ie=utf-8&pn=0')
el_list = driver.find_elements(by='xpath', value='//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a')    # 返回元素对象列表，匹配不到则返回空列表
for el in el_list:
    print(el)
    print(el.get_attribute('href'))



# 三、标签元素操作
# for el in el_list:
#     print('获取文本---->', el.text)
#     print('获取属性值---->', el.get_attribute('href'))
#     print('---------------------------------------------------------------------------------')

# el.click()                  # 仅可点击元素才能调用，否则报错
# el.send_keys('data')        # 用于输入框输入数据，仅text input这些可输入元素才能调用
# el.clear()                  # 用于清空输入框，仅输入框调用



# 四、标签页切换
# selenium控制浏览器打开多个标签页时，控制他们的切换需要以下两步
#     获取所有标签页的句柄
#     通过窗口句柄切换到句柄指向的标签页
# driver.get('https://sh.58.com/')
# 点击之前查看url和窗口句柄
# print(driver.current_url)
# print(driver.window_handles)

# el = driver.find_element(by='partial link text', value='租房')
# el = driver.find_element(by='xpath', value='/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a')
# el.click()
# 获取当前所有的标签页的窗口句柄列表
# current_windows = driver.window_handles
# 根据标签页句柄列表索引下标进行切换
# driver.switch_to.window(current_windows[-1])

# 点击之后查看url和窗口句柄：
# print(driver.current_url)
# print(driver.window_handles)           # 结果为：没有切换窗口句柄时，url和句柄前后相同，而切换了窗口句柄时则两者不同
# el_list = driver.find_elements(by='xpath', value='/html/body/div[6]/div[2]/ul/li/div[2]/h2/a')
# print(len(el_list))                    # 结果为：没有切换窗口句柄时，列表长度为0，因为在原来标签页匹配不到元素，而切换了窗口句柄时则为实际匹配到的元素个数



# 五、切换进入iframe
# iframe是html中常用的一种技术，即一个页面中嵌套了另一个网页，selenium默认是访问不了frame中的内容的，对应的解决思路是`driver.switch_to.frame(frame_element)`

# driver.get('https://qzone.qq.com')

# 参数frame_reference接收frame对象，或id, 或name等
# driver.switch_to.frame(frame_reference='login_frame')                             # frame_reference接收id, 有时候id是动态的(如时间戳命名)，则无法定位
# el_frame = driver.find_element(by='xpath', value='//*[@id="login_frame"]')
# driver.switch_to.frame(frame_reference=el_frame)                                  # frame_reference接收frame对象
# time.sleep(3)
# driver.find_element(by='id', value='switcher_plogin').click()                     # 必须先进入iframe，否则定位不到
# time.sleep(3)
# driver.find_element(by='id', value='u').send_keys('1605255762')
# time.sleep(3)
# driver.find_element(by='id', value='p').send_keys('tianxiawude')
# driver.find_element(by='id', value='login_button').click()



# 六、处理cookie
# driver.get('https://www.baidu.com')
# cookies = driver.get_cookies()
# print(cookies)
# cookie_list = [{'name': i['name'], 'value': i['value']} for i in cookies]
# print(cookie_list)
# 删除cookie
# driver.delete_cookie(name='cookie_name')
# driver.delete_all_cookies()



# 七、执行js代码
# driver.get('https://sh.lianjia.com/')

# 滚动条拖动
# js_code = 'scrollTo(0, 500)'
# driver.execute_script(js_code)

# el_a = driver.find_element(by='xpath', value='/html/body/div[2]/div/div[1]/div[2]/div[1]/a[1]')     # 若没有进行页面滚动或者滚动量不够，会定位不到元素，则会报错
# el_a.click()



# 八、页面等待
# 分类：
#     强制等待     time.sleep  缺点时不智能，要么设置的时间太短，元素还没有加载出来；要么设置的时间太长，则会浪费时间
#     隐式等待     隐式等待针对的是元素定位，隐式等待设置了一个时间，在一段时间内判断元素是否定位成功，如果完成了，就进行下一步；  在设置的时间内没有定位成功，则会报超时加载
#     显式等待     明确等待某一元素  一般爬虫不用，测试用

# 设置隐式等待，最长等20秒  所有元素定位操作都有最大等待时间
# driver.implicitly_wait(10)

# driver.get('https://www.baidu.com')

# el_image = driver.find_element(by='xpath', value='//*[@id="lg"]/map/area')
# print(el_image)



# 九、无界面模式
# 创建一个配置对象
# options = webdriver.ChromeOptions()
# 开启无界面模式:启动程序时不会打开谷歌浏览器界面
# options.add_argument('--headless')
# 禁用GPU
# options.add_argument('--disable-gpu')
# 使用代理ip,这种方式更换代理时必须重启浏览器
# options.add_argument('--proxy-server=https://221.22694.218:110')
# 替换user-agent
# options.add_argument('--user-agent=Mozilla/5.0 HAHA--------')

# _driver = webdriver.Chrome(options=options)
# _driver.get('https://www.baidu.com')
# print(_driver.title)
# _driver.save_screenshot('_baidu.png')



time.sleep(6)
# 关闭当前句柄指向的标签页，若仅有一个标签页，则关闭浏览器
# driver.close()


# 关闭浏览器
# driver.quit()
# _driver.quit()






