from xlwt import *
from xlrd import open_workbook
from xlutils.copy import copy

#新建一个test1.xls的文件，并在新建的文件里写
book = Workbook(encoding='utf-8')
sheet =book.add_sheet('Sheet1')

sheet.write(0,0,label='name')
sheet.write(0,1,label='age')
sheet.write(1,0,label='xiao')
sheet.write(1,1,label='18')

book.save('test6.xls')

#修改test6.xls中的文件内容
book2 =open_workbook('test6.xls')
wb = copy(book2)#wb即为xlwt.WorkBook对象
ws =wb.get_sheet(0) #通过get_sheet()获取的sheet有write()方法
ws.write(1,0,'张三')
ws.write(1,1,'28')
wb.save('test7.xls')