#coding=utf-8
import unittest
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.a = 1000000
        self.b = 1000000
        self.assertEquals(self.a,self.b)
    @classmethod
    def setUpClass(self):
        print('setUpClass')

    def test_1(self):
        # self.assertFalse('false','true')
        print('213')
    def tearDown(self):
        print('123')

def suite():
    suite = unittest.TestSuite()
    suite = suite.addTest(LoginTest('test_1'))
    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    # print('xiaohai')
    runner.run(suite())
    # unittest.main()

