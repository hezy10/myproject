from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'E:\chromdriver\chromedriver.exe')
driver.get(r'https://www.baidu.com')
# driver.get(r'https://www.sogo.com')
# driver.find_element_by_id('kw').send_keys('图片')
# driver.find_element_by_id('su').click()
# 控制浏览器窗口大小
# driver.set_window_size(500,1000)
# driver.maximize_window()


# 控制浏览器前进与后退
# driver.back()        #后退
# time.sleep(3)
# driver.forward()     #前进

# 刷新
# driver.refresh()


# first_url = driver.current_url
# print(first_url)
#
# driver.find_element_by_link_text('新闻').click()
# # second_url = driver.current_url
# # print(first_url)
#
# # 查看当前操作句柄
# handle = driver.window_handles
# print(handle)
#
# # 切换操作句柄
# driver.switch_to.window(handle[1])
# print(driver.current_url)
# time.sleep(10)
print(driver.page_source)

driver.quit()