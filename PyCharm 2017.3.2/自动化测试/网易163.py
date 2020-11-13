from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'E:\chromdriver\chromedriver.exe')
driver.get('https://mail.163.com/')


# frame = driver.find_element_by_css_selector('#loginDiv iframe')
# # 切入iframe
# driver.switch_to.frame(frame)
# driver.find_element_by_name('email').send_keys('18336900298')
# driver.find_element_by_name('password').send_keys('123456789')
# # driver.find_element_by_id('dologin').click()
# # print(driver.page_source)
# time.sleep(10)
#
#
# # 切出iframe
# driver.switch_to.default_content()
# driver.find_element_by_link_text('邮箱会员').click()
# # 获取当前页面的所有内容
# print(driver.page_source)
# driver.quit()
# todo 切入iframe
frame = driver.find_element_by_css_selector('#loginDiv iframe')
driver.switch_to.frame(frame)
driver.find_element_by_name('email').send_keys('11166633312')
driver.find_element_by_name('password').send_keys('***********')
driver.find_element_by_id('dologin').click()

# todo 切出iframe
driver.switch_to.default_content()
driver.find_element_by_link_text('海外用户登录').click()
print(driver.page_source)
time.sleep(10)
driver.quit()
