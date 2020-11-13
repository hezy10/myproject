from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=r'E:\chromdriver\chromedriver.exe')
        self.base_url = 'https://www.baidu.com'
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').send_keys('图片')
        driver.find_element_by_id('su').click()
        print(driver.title)
        self.assertEqual(driver.title,'百度一下，你就知道')

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(MyTest('test_baidu'))
    # 自定义报告存放路径
    # filename = './'+time.strftime('%Y_%m_%d %H:%M:%S')+'report.html'
    file = open('./report.html','wb')
    runner = HTMLTestRunner(file,title='百度搜索报告',description='测试用例测试情况')
    runner.run(suite)
    file.close()