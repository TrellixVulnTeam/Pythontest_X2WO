# -*- coding: utf-8 -*-
from selenium import webdriver
import time, re, unittest
from selenium.webdriver.common.keys import Keys


class Fcinvest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://mm0105.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("txtusername").send_keys("zhanhezou")
        self.driver.find_element_by_id("txtpw").send_keys("895544zhan")
        time.sleep(20)
        self.driver.find_element_by_id("btnsubmit").click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()

        # time.sleep(3)

    def test(self):
        driver = self.driver
        driver.get(self.base_url + "/member/index")
        driver.find_element_by_css_selector("#playmmc > span").click()
        driver.switch_to.frame('mainframe')
        driver.find_element_by_css_selector(".header").click()
        time.sleep(2)
        driver.find_element_by_css_selector("a.dwd").click()
        unitmode = driver.find_element_by_css_selector("a#unitmode").get_attribute("class")
        if unitmode == 'yuan':
            driver.find_element_by_css_selector("a#unitmode").click()
            driver.find_element_by_css_selector("a#unitmode").click()
        driver.find_element_by_xpath("//ul[@id='dwwanwei']/li[3]/span").click()
        driver.find_element_by_xpath("//ul[@id='dwqianwei']/li[4]/span").click()
        driver.find_element_by_xpath("//ul[@id='dwbaiwei']/li[5]/span").click()
        driver.find_element_by_xpath("//ul[@id='dwshiwei']/li[6]/span").click()
        driver.find_element_by_xpath("//ul[@id='dwgewei']/li[7]/span").click()
        driver.find_element_by_css_selector("a.add_num").click()
        driver.find_element_by_css_selector("a.selected_submit").click()
        driver.find_element_by_css_selector(".l-btn-text.l-btn-focus").click()
        time.sleep(2)
        driver.find_element_by_css_selector(".l-btn-text.l-btn-focus").click()
        wanwei = driver.find_element_by_xpath(".//*[@id='codeslist']/li[1]/span[1]").text
        qianwei = driver.find_element_by_xpath(".//*[@id='codeslist']/li[1]/span[2]").text
        baiwei = driver.find_element_by_xpath(".//*[@id='codeslist']/li[1]/span[3]").text
        shiwei = driver.find_element_by_xpath(".//*[@id='codeslist']/li[1]/span[4]").text
        gewei = driver.find_element_by_xpath(".//*[@id='codeslist']/li[1]/span[5]").text
        print(wanwei, qianwei, baiwei, shiwei, gewei)




        time.sleep(10)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()