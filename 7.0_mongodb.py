# 一、mongo安装


# 二、客户端 mongo shell
# 1. 服务端的启动
#    - sudo mongod --dbpath=数据库路径
# 2. 进入mongo shell客户端
#    - mongo
# 3. mongodb的数据库和集合命令
#    - show dbs
#    - use db_name
#    - show collections
#    - db
#    - db.集合名.drop()
#    - db.dropDatabase()
#    - exit
# 4. 了解文档中的_id字段


# 创建集合
# db.createCollection(name,options)
# 检查集合是否设定上限: db.集合名.isCapped()


# 三、mongo数据类型


# 四、CRUD操作
# 1. mongo shell中的增
#    db.集合名.insert({数据})
#    db.集合名.save({包含_id的完整数据}) # 根据指定的_id进行保存，存在则更新，不存在则插入
# 2. mongo shell中的删
#    db.集合名.remove({条件}, {justOne: true/false})
# 3. mongo shell中的改
#    db.集合名.update({条件}, {$set:{完整数据/部分字段}}, {multi: true/false})
# 4. mongo shell中的查
#    db.集合名.find({条件}, {字段投影})


# 五、聚合操作(常用管道和表达式)
# 常用管道命令如下：
#  - `$group`： 将集合中的⽂档分组， 可⽤于统计结果
#            `_id` 表示分组的依据(不能取其他名)，按照哪个字段进行分组，需要使用`$gender`表示选择这个字段进行分组,为null表示不分组
#            数据透视：分组后显示不可聚合字段的分组列表，如按性别分组时，姓名(不可聚合计算)可以按分组组成一起显示 name:{$push: "$name"}
#  - `$match`： 过滤数据， 只输出符合条件的⽂档,  和`find`区别在于`$match` 操作可以把结果交给下一个管道处理，而`find`不行
#  - `$project`： 修改输⼊⽂档的结构， 如重命名、 增加、 删除字段、 创建计算结果
#  - `$sort`： 将输⼊⽂档排序后输出
#  - `$limit`： 限制聚合管道返回的⽂档数
#  - `$skip`： 跳过指定数量的⽂档， 并返回余下的⽂档
#             $limit与$skip顺序有区别，在管道中永远是下一个管道对上一个管道的结果继续操作
#  - `$unwind`： 拆分值为列表的字段
# 常⽤表达式:
#  - `$sum`： 计算总和， $sum:1 表示以⼀倍计数
#  - `$avg`： 计算平均值
#  - `$min`： 获取最⼩值
#  - `$max`： 获取最⼤值
#  - `$push`： 在结果⽂档中插⼊值到⼀个数组中


# 六、索引
# js语法插入：   for (i=0;i < 100000;i++){db.t1.insert({name: 'test' + i, age: i})}
# 创建索引：db.t1.ensureIndex({name:1})
# 显示查询操作的详细信息 db.t1.find({name:'test10000'}).explain('executionStats')
# 查看索引：db.集合名.getIndexes()






