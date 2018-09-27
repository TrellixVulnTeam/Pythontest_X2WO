__author__ = 'Administrator'

from selenium import webdriver
from selenium import selenium
from selenium.webdriver.common.keys import Keys
import unittest
import re


class TestLoginJump(unittest.TestCase):
    """测试登录的跳转是否正常

    """

    def init_visit_homepage(self):
        browser = webdriver.Chrome()
        browser.get('http://test.www.999ask.com')
        return browser

    def test_login(self):
        browser = self.init_visit_homepage()
        browser.find_element_by_xpath("//div[@class='top1_1']/a[1]").click()
        browser.back()
        browser.quit()


if __name__ == "__main__":
    unittest.main()
