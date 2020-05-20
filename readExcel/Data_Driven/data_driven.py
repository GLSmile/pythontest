import xlrd
import json

class Data_Excel(object):
    def __init__(self):
        pass
    def readExcel(self,rowx):
       '''
       读取excel中数据并且返回
       :param rowx: 在excel中的行数
       :return:
       '''
       book =xlrd.open_workbook('data.xls')
       sheet =book.sheet_by_index(0)
       return sheet.row_values(rowx)

    def getUrl(self,rowx):
        '''
         获取请求URL
        :param rowx:在excel中的行数
        :return:
        '''
        return self.getUrl(rowx)[3]

    def getData(self,rowx):
        '''
         获取请求参数
        :param rowx:在excel中的行数
        :return:
        '''
        #由于Json中，标准语法中，不支持单引号，属性或者属性值，都必须是双引号括起来,用字符串方法replace("'",'\"')进行处理
        data1 =self.readExcel(rowx)[4].replace("'",'\"')

        #因为请求参数数据类型是字典，所以进行了反序列化的处理
        data =json.loads(data1)

        return data

if __name__ == '__main__':
    #定义一个类对象
    t =Data_Excel()
    url =t.getUrl(2)
    print(url)
    payload =t.getData(2)
    print(payload)

