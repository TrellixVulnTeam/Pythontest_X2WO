# coding: utf-8
__author__ = 'Administrator'
print('zhanxueyou')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


b = webdriver.Chrome()
#b = webdriver.Chrome("D:/python32/chromedriver.exe")
b.get('http://www.baidu.com')
elem = b.find_element_by_id('kw1')
elem.send_keys('selenium')
elem1 = b.find_element_by_id('su1')
elem1.click()


