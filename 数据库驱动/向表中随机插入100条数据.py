import pymysql
import random

'''
Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。
对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。
commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。
'''


#创建链接
db =pymysql.connect(host="localhost",port=3306,user="root",password="root",db="test",charset='utf8')
#创建游标
cursor =db.cursor()

#try:
# 循环插入100条数据到刚创建的表中
for i in range(1,100):
    id =random.randint(100,10000)
    t_name = "IEX" + str(id)

    sql2 = 'insert into test01(ID,T_NAME) values(%d,"%s")' % (id, t_name)
    cursor.execute(sql2)
    # 再次提交
    db.commit()
cursor.execute('select * from test01')
results =cursor.fetchall() #获取所有信息
for x in results:
    print(x)
#except:
    #回滚
   # db.rollback()

#关闭数据库连接
db.close()