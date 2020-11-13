from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'E:\chromdriver\chromedriver.exe')
driver.get('https://www.doing.net.cn')
ret = driver.page_source
with open('./第1个页面.html', 'wb') as f:
    f.write(ret.encode('utf-8'))


def toObtainHtml():
    for i in range(1, 4):
        driver.find_element_by_xpath("//div[@id='case_index']/a[1]").click()
        ret = driver.page_source
        with open('./第' + str(i) + '页_test.html', 'wb') as f:
            f.write(ret.encode('utf-8'))
        driver.back()
        time.sleep(1)
try:
    toObtainHtml()
except Exception as e:
    print(e)
    print('异常抛出')

driver.quit()