from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(5)

driver.get('https://zhuanlan.zhihu.com/p/26276505')
driver.find_element_by_id('username').send_keys('admin')
time.sleep(1)
driver.find_element_by_id('password').send_keys('admin123')
time.sleep(1)
driver.find_element_by_xpath("//input[@id='verifycode]").send_keys('0000')
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
driver.find_element_by_css_selector("body > div.container > div > form > div:nth-child(6) > button").click()
