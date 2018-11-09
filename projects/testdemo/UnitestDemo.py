#coding = utf-8
#为什么要选择unitest做单元测试，unitest提供了一些校验的方法，为什么我不选择自己写校验的方法，而是使用unitest提供的呢？

import unittest

class FuctionUnittest(unittest.TestCase):
    #初始化
    def setUp(self):
        print("setUp")
    #测试内容1
    def test_1(self):
        print("this is first demo")
    #测试内容2
    def test_2(self):
        a = '10000'
        b = '10000'
        # self.assertEquals(a,b)
        print("this is seconds demo")
    #清理
    def tearDown(self):
        print("tearDown")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(FuctionUnittest.test_2())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    print('i am not runner')
    runner.run(suite())
    #可以生成HTML测试报告
    print('生成测试报告')
    #将邮件发送到邮箱中
    print('将测试报告发送至邮箱')




