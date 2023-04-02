import pymysql
# 创建连接
conn = pymysql.connect(host="localhost", port=3306, user='root',passwd='Skills39!', db='word', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()
# 存在sql注入情况(不要用格式化字符串的方式拼接SQL)
sql = "insert into USER (NAME) values(%s)"
value = ('root',)
effect_row = cursor.execute(sql, value)

# 正确方式一
# execute函数接受一个元组/列表作为SQL参数,元素个数只能有1个
sql = "insert into USER (NAME) values(%s)"
effect_row1 = cursor.execute(sql, ['value1'])
effect_row2 = cursor.execute(sql, ('value2',))
# 正确方式二
sql = "insert into USER (NAME) values(%(name)s)"
effect_row1 = cursor.execute(sql, {'name': 'value3'})
# 写入插入多行数据
effect_row2 = cursor.executemany("insert into USER (NAME) values(%s)",
[('value4'), ('value5')])
# 提交
conn.commit()
# 关闭游标
cursor.close()