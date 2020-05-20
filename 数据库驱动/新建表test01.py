import pymysql
import random

#创建链接
db =pymysql.connect(host="localhost",port=3306,user="root",password="root",db="test",charset='utf8')
#创建游标
cursor =db.cursor()

#编写创建表的sql语句
sql1 ="""create table test01(
     id char(20) not null,
     t_name char(20))"""


try:
    #执行创建sql语句
    cursor.execute(sql1)
    #提交到数据库
    db.commit()

except:
    #回滚
    db.rollback()


#关闭数据库连接
db.close()