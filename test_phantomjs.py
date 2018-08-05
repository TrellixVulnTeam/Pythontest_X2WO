#!/usr/local/bin/python3

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/home/zhanxueyou/green/phantomjs_2_1_1/bin/phantomjs')#这里的executable_path填你phantomJS的路径

driver.get('http://www.so.com')

print(driver.title)

driver.quit()