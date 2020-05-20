from xlwt import *
import xlwt
book =Workbook(encoding='utf-8')
sheet =book.add_sheet('Sheet1')

#写入链接 #输出 "Google"链接到http://www.google.com
sheet.write(0, 0, xlwt.Formula('HYPERLINK("http://www.google.com";"Google")'))

#保存内容
book.save('test5.xls')