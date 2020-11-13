from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'E:\chromdriver\chromedriver.exe')
driver.get('https://www.doing.net.cn')
ret = driver.page_source
with open('./第1个页面.html','wb') as f:
    f.write(ret.encode('utf-8'))


driver.find_element_by_xpath("//div[@id='case_index']/a[1]").click()
ret1 = driver.page_source
with open('./第2个页面.html','wb') as f:
    f.write(ret1.encode('utf-8'))
driver.back()        #后退
time.sleep(1)        # 等待1秒

driver.find_element_by_xpath("//div[@id='case_index']/a[2]").click()
ret2 = driver.page_source
with open('./第3个页面.html','wb') as f:
    f.write(ret2.encode('utf-8'))
driver.back()        #后退
time.sleep(1)

driver.find_element_by_xpath("//div[@id='case_index']/a[3]").click()
ret3 = driver.page_source
with open('./第4个页面.html','wb') as f:
    f.write(ret3.encode('utf-8'))

driver.quit()