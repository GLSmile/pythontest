from xlwt import *
import xlwt

book = Workbook(encoding='utf-8')
sheet =book.add_sheet('Sheet1')

#设置格式
font =xlwt.Font()#字体
font.name ='Times New Roman'
font.bold =True
font.underline =True
font.italic =True

style =xlwt.XFStyle() #创建一个格式
style.font=font #设置格式字体
#在sheet1中插入格式化的内容
sheet.write(1,0,label='Formatted value',style) #Apply the Style to the Cell

#保存内容
book.save('test2.xls')