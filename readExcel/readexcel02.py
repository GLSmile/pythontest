import xlwt
import requests
import xlrd
import json
import unittest

#接口数据驱动之Excel 单个文件

#定义一个读取excel表的readExcel（）方法，参数rowx.
def readExcel(rowx):
    '''
       读取excel中数据并且返回

       :parameter filePath:xlsx文件名称

       :parameter rowx:在excel中的行数

     '''

    book =xlrd.open_workbook('data.xls')
    sheet =book.sheet_by_index(0)

    return sheet.row_values(rowx)

#第二步：定义一个获取请求URL的方法geturl()，参数：rowx.
def getUrl(rowx):
    '''
    获取请求URL
    :param rowx:在excel中的行数
    :return:
    '''
    return readExcel(rowx)[3]


#第三步：定义一个获取请求参数的方法getDat(),参数：rowx.
def getData(rowx):
    '''
     获取请求参数
    :param rowx:在excel中的行数
    :return:
    '''
    # 由于JSON中，标准语法中，不支持单引号，属性或者属性值，
    # 都必须是双引号括起来,用字符串方法replace("'",'\"')进行处理
    data1 = readExcel(rowx)[4].replace("'", '\"')
    # 因为请求参数数据类型是字典，所以进行了反序列化的处理
    data = json.loads(data1)
    return data

#第四步：用unittest 单元测试框架编写测试用例
class Test(unittest.TestCase):
    def setUp(self):
        print("---------开始执行用例----------")

    def tearDown(self):
        print("----------用例执行结束---------")

    def test_case1(self):
        url =getUrl(2)
        payload =getData(2)
        headers={
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Referer": "http://127.0.0.1:8090/recruit.students/login/view",
        }

        #发送get请求
        response =requests.get(url,headers,params=payload)

        #打印请求response后的URL
        print(response.url)

        #查看响应内容，response.text返回的是Unicode格式的数据
        print(response.text)

        #查看响应码
        print(response.status_code)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    '''
    这里的verbosity是一个选项,表示测试结果的信息复杂度，有三个值
    0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
    1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
    2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
    并且 你在命令行里加入不同的参数可以起到一样的效果
    加入 --quiet 参数 等效于 verbosity=0
    加入--verbose参数等效于 verbosity=2
    什么都不加就是 verbosity=1
    '''