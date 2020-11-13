# import unittest
# from testadd import TestTestAdd
# from testsub import TestTestSub
#
#
# suite = unittest.TestSuite()
# suite.addTest(TestTestAdd('test_add1'))
# suite.addTest(TestTestAdd('test_add2'))
# suite.addTest(TestTestSub('test_sub1'))
# suite.addTest(TestTestSub('test_sub2'))
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite)


# import unittest
# # 自动寻找
# ret = unittest.defaultTestLoader.discover('./')
# print(ret)
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(ret)


# # unittest执行策略
# import unittest
#
#
#
# class TestB(unittest.TestCase):
#     def setUp(self) -> None:
#         print('开始测试testb')
#
#     def tearDown(self) -> None:
#         print('结束测试testb')
#
#     def test_c(self):
#         print('cc')
#
#     def test_a(self):
#         print('aa')
#
#
# class TestA(unittest.TestCase):
#     def setUp(self) -> None:
#         print('开始测试testa')
#
#     def tearDown(self) -> None:
#         print('结束测试testa')
#
#     def test_b(self):
#         print('bb')
#
# if __name__ == '__main__':
#     unittest.main()


# # 跳过测试和预期失败
# import unittest
#
#
# # unittest.skip()
# # unittest.skipIf()
# # unittest.skipUnless()
# # unittest.expectedFailure()
#
#
# class MyTest(unittest.TestCase):
#     def setUp(self) -> None:
#         pass
#
#     def tearDown(self) -> None:
#         pass
#
#     @unittest.skip('跳过测试')
#     def test_skip(self):
#         print('test skip')
#
#     @unittest.skipIf(1,'条件成立跳过测试')
#     def test_skip_if(self):
#         print('test skipif')
#
#     @unittest.skipUnless(1 < 0,'条件成立执行测试')
#     def test_skip_unless(self):
#         print('test skipunless')
#
#     @unittest.expectedFailure
#     def test_skip_expect(self):
#         print('失败')
#
# if __name__ == '__main__':
#     unittest.main()


# 更大范围fixture
import unittest


def setUpModule():
    print('test setup>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def tearDownModule():
    print('test teardown>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('test setup class================>')

    @classmethod
    def tearDownClass(cls) -> None:
        print('test teardown class==============>')

    def setUp(self) -> None:
        print('test setup----------------->')

    def tearDown(self) -> None:
        print('test teardown------------------->')

    def test_skip(self):
        print('test skip')

if __name__ == '__main__':
    unittest.main()


