import smtplib
from email.mime.text import MIMEText
import unittest
from test_case import HTMLTestReportCN
from test_case import emails

class Mydemo(unittest.TestCase):
    def setUp(self):
        self.a=1
    def test1(self):
        #print("test1 value is {}".format(self.a))
        #self.assertEqual(2,3,"testError")
        # #验证list为空时，该用例不通过
        # a = 100
        # b = 1000
        # if(a!=b):
        #     print("错误")
        #     return False
        # else:
        #     print("OK")
        #     return True
        # print("xiongxiaofeng")
        self.assertEqual(2, 3, "testError")
    def test2(self):
        self.assertEqual(3,3,"testError")
        # print("test2 value is {}".format(self.a))
        # print(self.assertEqual(3,3,"testError"))
    def test3(self):
        print("test3 value is {}".format(self.a))

    def test9(self):
        self.assertEqual(1, 1, "testError")
    @classmethod
    def setUpClass(cls):
        cls.a=1
    @classmethod
    def tearDownClass(cls):
        print("i am tearDownClass")

def Suite():
    suitetest= unittest.TestSuite()
    suitetest.addTest(Mydemo("test1"))
    suitetest.addTest(Mydemo("test2"))
    suitetest.addTest(Mydemo("test9"))
    print(suitetest)
    return suitetest

if __name__ == '__main__':
    print("xiaoxiong")
    #unittest.main()
    # 确定生成报告的路径
    filePath = 'H:\\HTMLTestReportCN.html'
    # Mydemo().test1()
    # print(a)
    fp = open(filePath, 'wb')
    print("xiaoxiong")
    # 生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        # description='详细测试用例结果',
        tester='xiong'
    )
    # 运行测试用例
    runner.run(Suite())
    # print(runner.run(Suite()))
    # 关闭文件，否则会无法生成文件
    fp.close()
    #发送报告到邮箱
    emails.sendEmails()





