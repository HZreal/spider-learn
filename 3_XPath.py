# XPath (XML Path Language) 是一门在 HTML\XML 文档中查找信息的语言，可用来在 HTML\XML 文档中对元素和属性进行遍历
# 即快速定位XML/HTML中某个元素或标签


# XPath语法--路径表达式
# -----------------基础节点选择语法-----------------------
#       /              连续的层级查找
#       //             跨层级的查找     默认相对html标签向下查找
#       .              当前标签
#       ..             上一级标签
#       @              取标签的属性值   放在表达式结尾提取数据
#       text            取标签的文本    放在表达式结尾提取数据

#       `//h2/text()`                           - 选择所有的h2下的文本
#       `//a/@href`                             - 获取所有的a标签的href
#       `/html/head/title/text()`               - 获取html下的head下的title的文本
#       `/html/head/link/@href`                 - 获取html下的head下的link标签的href


# --------------------节点修饰语法-----------------------
# []               修饰路径表达式中的标签

# 多个标签时，根据索引筛选
# !!!!!!注意索引是从1开始的!!!!!!
#       `//div[3]`                              - 通过索引查找某个div
#       `//div[last()]`                         - 取最后一个索引的div
#       `//div[last()-1]`                       - 取倒数第二个索引的div
#       `//div[position()>10]`                  - 索引的区间选择的div  默认所有

# 根据标签的属性筛选(属性名前加@)
#       `//div[@id='app']/div/@label`           - @ 在 [] 中是修饰标签的属性，在路径表达式最后/@是取标签属性值

# 通过子节点的值修饰当前节点
#       `//span[i>20]`                          - 取span 其子节点i的值大于20
#       `//div[span[2]>=9.4]`                   - 取div 其子节点中的第二个span大于等于9.4

# 通过包含修饰
#       `//div[contains(@id, 'tag_')]`          - 取div 其属性id包含'tag_'
#       `//span[contains(text(), '下一页')]`     - 取span 其文本中含有'下一页'


# -------------------其他常用节点选择语法------------------
#       *            通配任意一个节点
#       node()       所有节点

#       `//*[@id='tag_']/div`                   - 取所有标签中id='tag_'的那个下的div


# ------------------复合语法----------------------
#      |            或者，即多个xpath语法逻辑或
# `//span[i>20]|//div[span[2]>=9.4]`            - 两者均可匹配









