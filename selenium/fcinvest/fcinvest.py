# -*- coding: utf-8 -*-
from selenium import webdriver
import time, re, unittest
import sys
from selenium.webdriver.common.keys import Keys


class Fcinvest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://mm0105.com/"
        # self.driver.maximize_window()
        self.verificationErrors = []
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("txtusername").send_keys('zhanhezou')
        self.driver.find_element_by_id("txtpw").send_keys('895544zhan')
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
        # 选择主钱包还是活动钱包，默认是主钱包，不用做选择操作
        # driver.find_element_by_css_selector("#activitywallet").click()
        # driver.find_element_by_css_selector("#hostwallet").click()
        # 下行与上行效果相同，用于选择活动钱包
        # driver.find_element_by_xpath(".//*[@id='activitywallet']").click()
        times = ('2', '6', '18', '54', '162', '486', '1458', '4374', '13122', '39366', '118098', '354294', '1062882', '3188646', '9565938', '28697814', '86093442', '258280326', '774840978')
        while True:
        # 中奖次数是2时就退出程序
        # cishu = 0
        # while cishu < 2:
            for beishu in times:
                # 循环执行投注
                driver.find_element_by_xpath("//ul[@id='dwwanwei']/li[3]/span").click()
                driver.find_element_by_xpath("//ul[@id='dwqianwei']/li[4]/span").click()
                driver.find_element_by_xpath("//ul[@id='dwbaiwei']/li[5]/span").click()
                driver.find_element_by_xpath("//ul[@id='dwshiwei']/li[6]/span").click()
                driver.find_element_by_xpath("//ul[@id='dwgewei']/li[7]/span").click()
                driver.find_element_by_css_selector("a.add_num").click()
                driver.find_element_by_css_selector("a.selected_submit").click()
                driver.find_element_by_css_selector(".l-btn-text.l-btn-focus").click()
                time.sleep(2)
                # no_money_message = driver.find_element_by_xpath("html/body/div[4]/div[2]/div[2]").text
                # 上下两种方式相同，分别是xpath和css定位方式
                no_money_message = driver.find_element_by_css_selector(".messager-body.panel-body.panel-body-noborder.window-body>div:nth-child(2)").text
                if '账户余额不足' in no_money_message:
                    print('余额不足')
                    driver.quit()
                driver.find_element_by_css_selector(".l-btn-text.l-btn-focus").click()

                # 获取上一次的中奖数字
                wanwei = driver.find_element_by_xpath(".//*[@id='codeslist']/li[1]/span[1]").text
                qianwei = driver.find_element_by_xpath(".//*[@id='codeslist']/li[1]/span[2]").text
                baiwei = driver.find_element_by_xpath(".//*[@id='codeslist']/li[1]/span[3]").text
                shiwei = driver.find_element_by_xpath(".//*[@id='codeslist']/li[1]/span[4]").text
                gewei = driver.find_element_by_xpath(".//*[@id='codeslist']/li[1]/span[5]").text
                print(wanwei, qianwei, baiwei, shiwei, gewei)

                if wanwei == '2' or qianwei == '3' or baiwei == '4' or shiwei == '5' or gewei == '6':
                    print("\033[7;31;40m%s\033[0m" % '中奖了')
                    driver.find_element_by_xpath(".//*[@id='tomultiple']").clear()
                    driver.find_element_by_xpath(".//*[@id='tomultiple']").send_keys('1')
                    break
                else:
                    print("\033[7;32;40m%s\033[0m" % '没中奖')
                    driver.find_element_by_xpath(".//*[@id='tomultiple']").clear()
                    driver.find_element_by_xpath(".//*[@id='tomultiple']").send_keys(beishu)
            # cishu += 1
        time.sleep(10)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
