from lxml import etree


# 利用etree.HTML，将html字符串（bytes类型或str类型）转化为Element对象，Element对象具有xpath的方法，返回结果的列表
text = ''' 
        <div> 
          <ul> 
            <li class="item-1">
              <a href="link1.html">first item</a>
            </li> 
            <li class="item-1">
              <a href="link2.html">second item</a>
            </li> 
            <li class="item-inactive">
              <a href="link3.html">third item</a>
            </li> 
            <li class="item-1">
              <a href="link4.html">fourth item</a>
            </li> 
            <li class="item-0">
              a href="link5.html">fifth item</a>
          </ul> 
        </div>
'''
html_obj = etree.HTML(text=text)        # 实际过程中 传响应的解析html数据response.text
print(html_obj)
# print(dir(html_obj))
ret_list = html_obj.xpath('//a[@href="link1.html"]/text()')
# print(ret_list[0])            # first item

text_list = html_obj.xpath('//a/@href')
# print(text_list)
link_list = html_obj.xpath('//a/text()')
# print(link_list)

# zip 函数返回(两个迭代器对应位置的元祖的)迭代器
# print(zip(text_list, link_list))             # <zip object at 0x101122b00>
# for text, link in zip(text_list, link_list):
#     print(text, link)


el_list = html_obj.xpath('//a')
for el in el_list:
    # print(el)                    # el 为 Element对象， 故亦可用xpath()方法
    print(el.xpath('./text()')[0], el.xpath('./@href')[0])
    # print(el.xpath('.//text()'))
    # print(el.xpath('text()'))



# etree.HTML() 会自动补全html中缺失的标签
# tostring将el对象转回html字符串
html_str = etree.tostring(html_obj).decode()
print(html_str)





