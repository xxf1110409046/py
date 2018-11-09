#coding=utf-8
from projects.testdemo import registTest
import unittest
#传入了一个对象
class reset(unittest.TestCase):
    def setUp(self):
        print('setUp')
    def demo001(self):
        # print('demo001')
        # self.test001()
        # self.test002()
        # self.test003()
        a = 1
        b = 1
        c = 'false'
        d = 'ture'
        self.assertEquals(a,b)
        print('执行了：' + "equals")
        # self.assertFalse(a,b)
    def demo002(self):
        print('demo002')


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite.addTest(reset.demo002()))
    #  unittest.main()
    # print('xiong')




