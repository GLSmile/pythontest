import requests
from bs4 import BeautifulSoup
import xlrd
import json

def readExcel(rowx,filePath='data.xls'):
    '''
      读取excel中数据并且返回
    :param rowx: 在excel中的行数
    :param filePath: xlsx文件名称
    :return:
    '''

    book = xlrd.open_workbook(filePath)
    sheet =book.sheet_by_index(0)
    return sheet.row_values(rowx)

#提取第一个测试用例数据
print("第一行数据内容：",readExcel(2))

#查看数据的类型
print("数据类型：{0}：".format(type(readExcel(2))))

#从列表中提取url
url =readExcel(2)[3]
print(url)

#从列表中提取data参数
#JSON中，标准语法中，不支持单引号，属性或者属性值，都必须是双引号括起来,用字符串方法replace("'",'\"')进行处理
#data1 =readExcel(2)[3].replace("",'\"')
data1 =readExcel(2)[3]

#因为请求参数数据类型是字典，所以进行了反序列化的处理。
#从Excel表提取的行数据，是一个列表，列表的元素是字符串，
# 如果接口参数类型如果是字典类型，需要反序列化的处理（json.loads()）
data=json.loads(data1)
print(data)
print(type(data))

print("---------------------------------------------------")
#招生系统接口例子

header={
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/67.0.3396.99 Safari/537.36",
    "Referer":" http://127.0.0.1:8080/recruit.students/login/view",

}

#URL参数
payload =data

#发送get请求
response =requests.get(url,headers=header,params=payload)

#打印请求response后的URL
print(response.url)

#查看响应内容，response.text返回的是Unicode格式的数据
print(response.text)

#查看响应码
print(response.status_code)

