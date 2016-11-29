# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Ex(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.rqbao.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ex(self):
        driver = self.driver
        driver.get(self.base_url + "/menu-loan.html")
        driver.find_element_by_id("loanAmount").clear()
        driver.find_element_by_id("loanAmount").send_keys("1000")
        driver.find_element_by_id("loanPeriod").clear()
        driver.find_element_by_id("loanPeriod").send_keys("1000")
        driver.find_element_by_xpath("(//input[@name='monthOrDay'])[2]").click()
        driver.find_element_by_xpath("(//input[@name='monthOrDay'])[2]").click()
        Select(driver.find_element_by_id("borrowType")).select_by_visible_text(u"企业")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
