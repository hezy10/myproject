from selenium import webdriver
import os

url = os.path.abspath('upfile.html')
print(url)
driver = webdriver.Chrome(executable_path=r'E:\chromdriver\chromedriver.exe')
driver.get(url)
driver.find_element_by_name('file').send_keys(r'D:\PyCharm 2017.3.2\自动化测试\a.jpg')
driver.find_element_by_id('sub').click()
