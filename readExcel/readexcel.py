import requests
import xlrd

def readExcel(rowx,filePath='data.xls'):
    '''
    读取excel中数据并且返回
    :param rowx: 在excel中的行数
    :param filePath: xlsx文件名称
    :return:
    '''
    book =xlrd.open_workbook(filePath)
    sheet=book.sheet_by_index(0)
    return sheet.row_values(rowx)

#提取第一个测试用例数据
print("数据类型：{0}：".format(type(readExcel(2))))
#从列表中提取url
url =readExcel(2)[1]
print(url)

#从列表中提取data参数
data =readExcel(2)[3]
print(data)