from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from selenium.common.exceptions import NoSuchElementException
import time


driver = webdriver.Chrome(executable_path=r'E:\chromdriver\chromedriver.exe')
driver.get('https://www.baidu.com')
# print(time.ctime())
# # 显示等待  指定某一个条件成立才继续执行
# try:
#
#     ret = WebDriverWait(driver, 5).until(es.presence_of_element_located((By.ID, 'kw')))
#
# # 出现异常执行except否则执行else
# except Exception as e:
#     print(e)
#     print('异常')
#
# else:
#     print('找到内容')
#     # 回车操作
#     ret.send_keys('图片', Keys.ENTER)
#     print(ret)
#     time.sleep(3)
# # finally一般用来做清理工作
# finally:
#     print('finally')
#     print(time.ctime())
#     driver.save_screenshot('b.png')
# # 隐式等待
# driver.implicitly_wait(5)
# print('开始时间：',time.ctime())
# try:
#     driver.find_element_by_id('kw').send_keys('图片')
# except NoSuchElementException as e:
#     print(e)
# finally:
#     print('finally')
#     driver.save_screenshot('c.png')
# print('结束时间：',time.ctime())
# driver.quit()


