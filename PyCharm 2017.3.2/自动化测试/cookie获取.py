from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r'E:\chromdriver\chromedriver.exe')
# ret = driver.get('https://www.youdao.com')
ret = driver.get('https://www.doing.net.cn')
# data = driver.page_source
driver.find_element_by_class_name('xh-highlight').click()
# with open('./2.html','wb') as f:
#     f.write(data.encode('utf-8'))
# print(data)
# cookies = driver.get_cookies()
# cookies = driver.add_cookie({'name':'xiaoyu'})
# print(cookies)
# print(cookies[1].get('domain'))

#
# new_str = "alert('ok')"
# driver.execute_script(new_str)
time.sleep(10)
driver.quit()