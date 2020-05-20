import pymysql

#创建数据库连接
db =pymysql.connect(host="localhost",port=3306,user="root",password="root",db="test",charset='utf8')
#创建指针
cursor =db.cursor()

#构造删除sql语句
sql ="""delete from employee where first_name='lisi'"""
try:
    #执行sql语句进行删除
    cursor.execute(sql)

    #提交到数据库执行
    db.commit()

except:
    #若是出错，则回滚
    db.rollback()

#关闭数据库连接
db.close()