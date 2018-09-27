__author__ = 'Administrator'

from selenium import webdriver
from selenium import selenium
from selenium.webdriver.common.keys import Keys
import unittest
import time
import re

class AskLoginJump(unittest.TestCase):
    def test_login_jump(self):
        browser = webdriver.Chrome()
        browser.get('http://test.www.999ask.com')
        browser.find_element_by_xpath("//div[@class='top1_1']/a[1]").click()
        browser.back()

if __name__ == "__main__":
    unittest.main()

# browser = webdriver.Chrome()
#
# browser.get('http://test.www.999ask.com')
#
# elem = browser.find_element_by_class_name('top1_1')
#
# #elem.find_element_by_link_text('登录').click()
# browser.find_element_by_xpath("//div[@class='top1_1']/a[1]").click()




