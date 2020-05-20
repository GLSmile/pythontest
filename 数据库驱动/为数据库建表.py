import pymysql

#创建链接
db = pymysql.connect(host="localhost",port=3306,user="root", password="root",db= "test",charset='utf8')
#创建游标
cursor =db.cursor()
#利用游标执行sql语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
try:
    #执行
    cursor.execute(sql)
    #提交到数据库
    db.commit()
except:
    #如果发生异常则回滚
    db.rollback()


#关闭数据库连接
db.close()