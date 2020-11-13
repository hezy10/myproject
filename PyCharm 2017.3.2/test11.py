import unittest
from testtest import TestAdd
from cal import TestSub


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        print('测试开始')

    def tearDown(self) -> None:
        print('测试结束')


class TestTestAdd(MyTest):

    def test_add1(self):
        add = TestAdd(1,2,3)
        self.assertEqual(add.add(),6)

    def test_add2(self):
        add = TestAdd(1,3,3)
        self.assertEqual(add.add(),7)


class TestTestSub(MyTest):

    def test_sub1(self):
        sub = TestSub(2,1)
        self.assertEqual(sub.sub(),1)

    def test_sub2(self):
        sub = TestSub(5,3)
        self.assertEqual(sub.sub(),2)

# 组织测试用例
if __name__ == '__main__':
    # todo 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestTestAdd('test_add1'))
    suite.addTest(TestTestAdd('test_add2'))
    suite.addTest(TestTestSub('test_sub1'))
    suite.addTest(TestTestSub('test_sub2'))
    # todo 执行测试用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.main()