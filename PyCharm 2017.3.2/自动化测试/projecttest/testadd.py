from testtest import TestAdd
from test11 import MyTest
import unittest


class TestTestAdd(MyTest):

    def test_add1(self):
        add = TestAdd(1,2,3)
        self.assertEqual(add.add(),6)

    def test_add2(self):
        add = TestAdd(1,3,3)
        self.assertEqual(add.add(),7)

if __name__ == '__main__':
    unittest.main()