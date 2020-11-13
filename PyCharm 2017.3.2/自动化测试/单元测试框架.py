import unittest
from test1 import Count


# class TestCount(unittest.TestCase):
#     def setUp(self):
#         print('测试开始')
#
#     def test_add(self):
#         count = Count(1,2)
#         self.assertEqual(count.add(),2)
#
#     def test_add1(self):
#         count = Count(2,2)
#         self.assertEqual(count.add(),4)
#
#     def tearDown(self):
#         print('测试结束')
#
# if __name__ == '__main__':
#     # unittest.main()
#     # todo 构造测试集
#     suite = unittest.TestSuite()
#     suite.addTest(TestCount('test_add'))
#
#     # todo 执行测试
#     runner = unittest.TextTestRunner()
#     runner.run(suite)


class TestCount(unittest.TestCase):
    def setUp(self) -> None:
        print('测试开始')

    def test_add(self):
        count = Count(3,4)
        self.assertEqual(count.add(),7)

    def test_add1(self):
        count = Count(4,5)
        self.assertEqual(count.add(),9)

    def tearDown(self) -> None:
        print('测试结束')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCount('test_add'))
    runner = unittest.TextTestRunner()
    runner.run(suite)