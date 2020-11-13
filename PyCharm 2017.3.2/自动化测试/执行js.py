from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'E:\chromdriver\chromedriver.exe')
ret = driver.get('https://www.baidu.com')
# new_str = "alert('ok')"
# driver.execute_script(new_str)
#
driver.find_element_by_name('wd').send_keys('图片')
driver.find_element_by_id('su').click()
time.sleep(2)
js = 'window.scrollTo(100,400)'
driver.execute_script(js)
driver.save_screenshot('d.png')
time.sleep(1)
driver.quit()