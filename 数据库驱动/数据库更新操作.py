import pymysql

#创建数据库连接
db = pymysql.connect(host="localhost",port=3306,user="root",password="root",db="test",charset='utf8')
#创建指针
cursor =db.cursor()

#构造更新用的sql语句
sql ="""update employee set age=50 where last_name='xiaosi'"""

try:
    #执行更新操作
    cursor.execute(sql)
    #交给数据库执行
    db.commit()
except:
    #出错后，回滚
    db.rollback()

#关闭数据库连接
db.close()
