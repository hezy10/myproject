from test1 import Count


class TestCount:
    def test_add(self):
        try:
            count = Count(1,2)
            sum_val = count.add()
            # 断言
            assert sum_val == 3,'func error'
        except AssertionError as e:
            print(e)
        else:
            print('通过测试')
        finally:
            print('测试程序')
if __name__ == '__main__':
    test = TestCount()
    test.test_add()