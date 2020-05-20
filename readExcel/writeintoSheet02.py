from xlwt import *
import xlwt
import time

book = Workbook(encoding='utf-8')
sheet = book.add_sheet('Sheet1')
style =xlwt.XFStyle()
#写入当前时间
time = time.strftime("%Y%m%d%H%M%S",time.localtime())
style.num_format_str ='M/D/YY'
sheet.write(0,0,time,style)

#保存内容
book.save('test3.xls')