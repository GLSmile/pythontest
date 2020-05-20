import unittest
import requests
from test01.readExcl01 import read_Excel


class test_TQ(unittest.TestCase):
    def setUp(self):
        print("开始")

    def tearDown(self):
        print("结束")

    def test002(self):
        #创建对象
        t = read_Excel()
        #调用方法
        data2 = t.red_exc()
        #遍历数据
        for i in data2:
            url ="http://v.juhe.cn/weather/index" #查询天气的接口请求地址
            #构建请求参数
            para = {"cityname":i["cityname"],"key":i["key"]}
            #发送请求
            res = requests.post(url,params=para)
            re =res.json()
            self.assertEqual(re["reason", i["查询成功！"]])
            self.assertEqual(re["error_code",int(i["exp"])])


if __name__ == "__main__":
    unittest.main()