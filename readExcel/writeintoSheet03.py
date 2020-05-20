from xlwt import *
import xlwt

book=Workbook(encoding='utf-8')
sheet=book.add_sheet('Sheet1')

#写入公式
sheet.write(0,0,5)
sheet.write(0,1,2)
sheet.write(1,0,xlwt.Formula('A1*B1')) # 输出 "10" (A1[5] * A2[2])
sheet.write(1,1,xlwt.Formula('SUM(A1,B1)')) # 输出 "7" (A1[5] + A2[2])

#保存内容
book.save('test4.xls')
