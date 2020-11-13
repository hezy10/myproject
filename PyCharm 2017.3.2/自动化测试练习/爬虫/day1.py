import unittest
import time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=r'E:\chromdriver\chromedriver.exe')
        self.driver_url = 'https://mail.163.com'
        # self.driver_url = 'https://www.baidu.com'
        self.driver.maximize_window()        # 窗口最大化
        # self.driver.implicitly_wait(5)      # 隐式等待

    def tearDown(self) -> None:
        self.driver.quit()

    def test_email(self):
        driver = self.driver
        driver.get(self.driver_url)

        # driver.find_element_by_id('kw').send_keys('图片')
        # driver.find_element_by_id('su').click()
        # print(driver.title)
        # self.assertEqual(driver.title,'百度一下，你就知道')

        # css标签定位到iframe
        frame = driver.find_element_by_css_selector('#loginDiv iframe')
        # 切入iframe
        driver.switch_to.frame(frame)
        driver.find_element_by_name('email').send_keys('179644835')
        driver.find_element_by_name('password').send_keys('**********')
        driver.find_element_by_id('dologin').click()
        time.sleep(1)
        # 切出iframe
        driver.switch_to.default_content()
        driver.find_element_by_link_text('邮箱会员').click()


if __name__ == '__main__':
    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(MyTest('test_email'))
    f = open('./youdao.html','wb')
    runner = HTMLTestRunner(f,title='163邮箱测试报告',description='测试用例情况')
    runner.run(suite)
    f.close()

