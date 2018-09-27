__author__ = 'Administrator'

from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import re


class baidu_click(unittest.TestCase):
    def test_baidu_click(self):             # 类中方法以test_开头，执行时就会当做测试用例执行
        sel = webdriver.Chrome()
        sel.get("http://www.baidu.com")
        sel.find_element_by_id('kw').send_keys('selenium' + Keys.RETURN)
        sel.quit()

    def test_baidu_search(self):
        sel =  webdriver.Chrome()
        sel.get("http://www.baidu.com")
        sel.find_element_by_id('kw').send_keys('python' + Keys.RETURN)


if __name__ == "__main__":
    unittest.main()
