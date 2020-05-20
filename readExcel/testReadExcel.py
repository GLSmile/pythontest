import os,sys,requests,unittest
sys.path.append("./Data_Driven")
#from Data_Driven.data_driven import Data_Excel 这个总是出错
from Data_Driven import *


#接口数据驱动之Excel 多个文件
class Test(unittest.TestCase,Data_Excel):
    def setUp(self):
        print("--------用例开始执行-----------")

    def tearDown(self):
        print("--------用例执行完毕-----------")

    def test_case1(self):
        t =Data_Excel()
        url =t.getUrl(2)
        payload =t.getData(2)
        headers ={
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Referer": "http://127.0.0.1:8090/recruit.students/login/view",
        }

        #发送get请求
        response =requests.get(url,headers=headers,params=payload)

        #打印请求response后的Url
        print(response.url)

        #查看响应内容，response.text返回的是Unicode格式的数据
        print(response.text)

        #查看响应码
        print(response.status_code)

if __name__ == '__main__':
    unittest.main(verbosity=2)