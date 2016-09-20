# -*- coding: utf-8 -*-
import unittest # python的单元测试框架类库
import requests # python处理http相关的类库
from lib.config import Config #  车E族项目的公共的环境配置相关的方法
from lib.login import * # 登录、退出、获取Session等常用方法

# mayanwei 2016-06-01 加油卡充值相关接口

class ShihuaICBenefit(unittest.TestCase):
    def tearDown(self):
        logout()

    def test_shihuaICBenefit_ICPreCheck(self):
        response_login = login(Config.username, Config.password)
        cookie = get_user_session(response_login)
        api_url = "/webapp/ShihuaICBenefit/ICPreCheck"
        header = common_header()
        header["Cookie"] = cookie
        params_ = {
            'cardNo': Config.icCardNo,
            'no_use_money': '',
            'money': '1000',
            'choose_payment':	"addmore",
            'no_use_card': Config.bankcard,
            'accountNo': Config.bankcard,
            'payType':	 '1'
        }

        result = requests.post(Config.host_url + api_url, headers=header, params=params_)
        assert result.json()['code'] == '00000', "result.json()['code']= %s" % result.json()['code']

    def test_shihuaICBenefit_ICPreRecharge(self):
        response_login = login(Config.username, Config.password)
        cookie = get_user_session(response_login)
        print cookie
        api_url = "/webapp/ShihuaICBenefit/ICPreRecharge"
        header = common_header()
        header["Cookie"] = cookie
        params_ = {
             "cardNo": Config.icCardNo,
             "no_use_money":	'',
             "money": '1',
             "choose_payment"	: Config.bankcard,
             "no_use_card":	'',
             "accountNo": Config.bankcard,
             "payType": 1
        }

        result = requests.post(Config.host_url + api_url, headers=header,params=params_)
        assert result.content.find('立即充值'), "加油卡充值确认页异常 %s \r\n" % result.content

    def test_shihuaICBenefit_rechargePage(self):
        response_login = login(Config.username,Config.password)
        cookie = get_user_session(response_login)
        print cookie
        api_url = "/webapp/shihuaICBenefit/rechargePage"
        header = common_header()
        header['Cookie'] = cookie

        result = requests.get(Config.host_url+ api_url,headers=header)
        print result.status_code
        # print result._content('<option value="1000111100000000001" selected>1000111100000000001</option>')
        assert result.status_code == '200', "result.status_code: %s" % result.status_code



