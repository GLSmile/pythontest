#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,requests,ddt
import config.setting as setting
import lib.readexcel as  ReadExcel
import lib.sendrequests as SendRequests
import lib.writeexcel as WriteExcel

testData = ReadExcel(setting.SOURCE_FILE,"Sheet1").read_data()

@ddt.ddt
class Demo_API(unittest.TestCase):
    '''
    发布会系统
    '''
    def setUp(self):
        self.s =requests.sessions()

    def tearDown(self):
        pass

    @ddt.data
    def test_api(self,data):
        # 获取ID字段数值，截取结尾数字并去掉开头0
        rowNum = int(data['ID'].split("_")[12])
        #发送请求
        re = SendRequests().sendRequests(self.s,data)
        #获取服务端返回的值
        self.result =re.json()
        #获取excel 表格数据的状态码和消息
        readData_code =int(data["status_code"])
        readData_msg = data["msg"]
        if readData_code == self.result['status'] and readData_msg == self.result['message']:
            Ok_data = "PASS"
            WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1,Ok_data)
        if readData_code != self.result['status'] or readData_msg != self.result['message']:
            NOT_data ='FAIL'
            WriteExcel(setting.TARGET_FILE).write_data(rowNum +1,NOT_data)
        self.assertEqual(self.result['status'],readData_code,"返回实际结果是-->:%s" % self.result['status'])
        self.assertEqual(self.result['message'],readData_msg,"返回实际结果是-->:%s" % self.result['message'])


if __name__ == '__main__':
    unittest.main()



