__author__ = 'Zhanxueyou'

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class YpkLogin(unittest.TestCase):                                          # 如果要进行单元测试，需要继承unittest类TestCase
    def test_login_textbox(self):                       # 在一个类中定义测试模块
        sel = webdriver.Chrome()                            # 使用浏览器
        sel = webdriver.Firefox()                           #使用Firefox浏览器
        sel.get("http://www.ypk.com.cn")                    # 输入网站地址，打开网站
        #sel.find_element_by_class_name('login').click()
        sel.find_element_by_css_selector('.login').click()  # 使用css选择器定位
        sel.find_element_by_name('username').send_keys('zhanxueyou')    # 寻找元素，并填入内容
        sel.find_element_by_name('password').send_keys('123456' + Keys.RETURN)  # 输入密码后直接进行了回车操作
        #sel.switch_to_alert().accept()  # 跳转之后显示了alert提示框，使用该命令接受，相当于点击了‘确定’

