from cal import TestSub
from test11 import MyTest
import unittest


class TestTestSub(MyTest):

    def test_sub1(self):
        sub = TestSub(2,1)
        self.assertEqual(sub.sub(),1)

    def test_sub2(self):
        sub = TestSub(5,3)
        self.assertEqual(sub.sub(),2)

if __name__ == '__main__':
    unittest.main()