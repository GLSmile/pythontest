import pymysql

#创建数据库连接
db =pymysql.connect(host="localhost",port=3306,user="root",password="root",db="test",charset='utf8')
#创建指针
cursor =db.cursor()


#执行sql语句查询
sql ="""select * from employee where income >1000"""

try:
    #执行查询
    cursor.execute(sql)
    #获取所有的记录列表
    results =cursor.fetchall()
    #循环操作每条记录,得到每条记录中各个字段的信息
    for row in results:
        fname =row[0]
        lname =row[1]
        age =row[2]
        sex =row[3]
        income =row[4]

        #打印结果
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" %(fname,lname,age,sex,income))

except:
    #出现错误，打印错误信息
    print("Error: unable to fecth data")

#关闭数据库
db.close()
