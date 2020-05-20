import pymysql

#Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。
#创建链接
db =pymysql.connect(host="localhost",port=3306,user="root",password="root",db= "test",charset='utf8')

#创建指针
cursor =db.cursor()

#执行sql语句，插入操作


sql1 ="""INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('lisi', 'xiaosi', 22, 'M', 150000)"""

try:
    #执行插入操作
    cursor.execute(sql1)
    # 提交到数据库执行
    db.commit()
except:
    #出现问题，回滚
    db.rollback()

#关闭数据库连接
db.close()