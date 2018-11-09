# import unittest
# from test_case import HTMLTestReportCN
# class Mydemo(unittest.TestCase):
#     def setUp(self):
#         self.a=1
#     def test_1(self):
#         print("执行了test1")
#         self.assertEqual(1,1,"eerorcode")
#     def test_2(self):
#         print("执行了test2")
#         # self.assertEqual(2,3,"errorcode")
#         self.assertTrue(loginTure())
#         print(loginTure())
#
#
# def loginTure():
#     a = 1
#     b = 2
#     if(a != b):
#         return False
#     else:
#         return True
#
# if __name__=='__main__':
#     print("执行了main方法")
#     # unittest.main()
#     suite = unittest.TestSuite()
#     #获取某个文件下的所有test_*的测试用例
#     # suite.addTest(Mydemo('test_1'))
#     # suite.addTest(Mydemo('test_2'))
#     all_suite = unittest.defaultTestLoader.discover('H:\\PycharmProjects\\demo\\test_case','test*.py')
#     print(all_suite)
#     # # #循环将所有测试用例放入集合中
#     # for case in all_suite:
#     #
#     #     suite.addTest(case)
#     #生成测试报告
#     #文件路径
#     fileName = "H:\\xiaofeng.html"
#     # 文件操作权限
#     op = open(fileName,"wb")
#     # Html报文
#     runner = HTMLTestReportCN.HTMLTestRunner(stream = op,title="xiong",tester='熊')
#     print(suite)
#     runner.run(suite)
#     op.close()
#
i=0
list = [1,2,3,"12",5]
# i=list.count()
#
del list[3]
# list.remove("234")
# print(list)
print("max(list)" + str(max(list)))
for i in range(0,len(list)):
    print(list[i])

s=0
listdate = (1,233,4,34,23,"12")
# list1=listdate[5]
# print(list1)
del listdate[len(listdate)]
print(str(max(listdate)))
for s in range(0,len(listdate)):
    print(listdate[s])
# for s in listdate:
#     print(listdate[s])