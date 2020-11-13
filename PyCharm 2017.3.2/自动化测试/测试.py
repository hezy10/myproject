from selenium import webdriver
import time


# 创建了一个操作句柄
driver = webdriver.Chrome(executable_path=r'E:\chromdriver\chromedriver.exe')
# driver = webdriver.Chrome()

# 模拟请求           #####reponse......响应######
data = driver.get(url=r'https://www.baidu.com')
# driver.get(url=r'https://github.com/')
# print(data)

# todo 通过id进行定位
# ret = driver.find_element_by_id('kw').send_keys('图片')
# ret = driver.find_element_by_class_name('wd')
# ret = driver.find_element_by_name("wd").send_keys('tupain')
ret = driver.find_element_by_class_name('s_ipt').send_keys('tupian')
# print(ret)
time.sleep(3)


# todo 点击事件
# driver.find_element_by_id('su').click()
# driver.find_element_by_id('su').click()
# driver.find_element_by_class_name('bg s_btn').click()
driver.find_element_by_link_text("百度一下").click()

time.sleep(2)

# 进行滚动条定位
# js = 'window.scrollTo(100,400)'
# driver.execute_script(js)
#
# time.sleep(2)

# 自动化测试模型
# 1、线性测试
# 2、模块化驱动测试
# 3、数据驱动测试
# 4、关键字
# todo 关闭浏览器
driver.quit()