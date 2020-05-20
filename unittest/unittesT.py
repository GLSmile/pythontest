import unittest
from test01 import readExcl


class Test_Add(unittest.TestCase):
    def setUp(self):
        print("开始执行")
    def tearDown(self):
        print("执行结束")

    def test01(self):

        r =readExcl()
        data =r.red_exc()

        for i in data:
            self.assertEqual(int(['a'])+int(i['b']),int(i['c']))


if __name__=="__main__":
    unittest.main()