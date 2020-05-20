import pymysql

#打开数据库连接（ip/端口/数据库用户名/登录密码/数据库名/编码）
db = pymysql.connect(host="localhost",port=3306,user="root", password="root",db="test",charset='utf8')
#使用cursor()方法创建一个游标对象cursor
cursor =db.cursor()

#使用execute()方法执行Sql查询（查询mysql的版本）
cursor.execute("select version()")

#使用fetchone()方法获取单条数据
data =cursor.fetchone()
print("Database version:%s" %data)

#关闭数据库
db.close()