from xlwt import *

book = Workbook(encoding='utf-8')
sheet =book.add_sheet('Sheet1')

#在sheet1中简单插入内容
sheet.write(0,0,label='Row 0,Column 0 Value')

#保存内容
book.save('test1.xls')