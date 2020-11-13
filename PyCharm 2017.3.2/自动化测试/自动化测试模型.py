from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path=r'E:\chromdriver\chromedriver.exe')


def login(iframe,email,password):
    driver.get('https://mail.163.com/')
    # frame = driver.find_element_by_css_selector('#loginDiv iframe')
    frame = driver.find_element_by_css_selector(iframe)
    # 切入iframe
    driver.switch_to.frame(frame)
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id('dologin').click()

if __name__ == '__main__':
    login('#loginDiv iframe','123456','********')
    time.sleep(5)
    driver.quit()
