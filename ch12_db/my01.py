#coding=utf-8
'''
1 .导入sqlite3模块
2. 创建连接 sqlite3.connect()
3.创建游标对象
4.编写创建表的sql语句
5.执行sql
6.关闭连接
'''

import sqlite3
# 创建连接
con = sqlite3.connect('d:/sqlite3Demo/demo.db')
#print(con)
# 创建游标对象
cur = con.cursor()
# 编写创建表的sql语句
sql = '''create table t_person(
             pno INTEGER PRIMARY KEY autoincrement,
             pname VARCHAR NOT NULL,
             age INTEGER)
'''
try:
    # 执行sql
    cur.execute(sql)
    print('创建表成功')
except Exception as e:
    print(e)
    print('创建表失败')
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()





