# -*- coding: utf-8 -*-
import unittest

import requests

from lib.config import *


def login():
	""" login实现用户登录功能 """
	header = {
			'Content-Type': request_headers['Content-Type'],
			'Host': host[8034],
			'Connection': request_headers['Connection'],
			'User-Agent': request_headers['User-Agent1'],
			'Accept-Encoding': request_headers['Accept-Encoding']
		}
	login_data = {
			'CyLoginForm[username]': list(login_user.keys())[0],
			'CyLoginForm[type]': '0',
			'CyLoginForm[rememberMe]': '1',
			'CyLoginForm[password]': login_user[list(login_user.keys())[0]],
			'CyLoginForm[deviceToken]': 'AiZDsjfgTovpX0-w3u9olgcL8RYgW5J0i5WOgjvvGxFw',
			'CyLoginForm[client]': 'android', 'companyKey': '', 'token': '',
			'CyLoginForm[type]': '0', 'ajax': '1',
		}
	# json_data = 'CyLoginForm' # 在请求中不写json=json_data参数也可以
	user_login = requests.post('http://'+host[8034]+'/api/user/shihuaAPPLogin', data=login_data, headers=header)
	user_login.raise_for_status()		# 如果响应的状态值不是200，则抛出异常
	if user_login.json()['code'] != '00000':
		print '登录不成功'
	return user_login

user = login()


class Recharge(unittest.TestCase):
	""" 车e族充值接口测试用例
	"""
	def test_recharge(self):
		assert user.json()['code'] == '00000', '登录不成功'


class Oil(unittest.TestCase):
	""" 车e族银行卡加油接口测试用例
	"""
	def test_oil_pay(self):
		""" 接口跳转测试用例
		"""
		assert user.json()['code'] == '00000', '登录不成功'
		oil_data = {
			# 'deviceUserId': '43b4bfc2374b1ad715f59d3ae4bc6dae',
			'deviceUserId': 'd758ad7563433c2797694371edd152aa',
			'dutyCode': '2016051704',
			'companyKey': request_body['companyKey'],
			'token': user.json()['data']['token']
		}
		# print user.content
		# print user.headers
		oil_headers = {
			'Host': host[8034],
			'Connection': request_headers['Connection'],
			'Accept': request_headers['Accept'],
			'Upgrade-Insecure-Requests': request_headers['Upgrade-Insecure-Requests'],
			'User-Agent': request_headers['User-Agent2'],
			'Accept-Encoding': request_headers['Accept-Encoding'],
			'Accept-Language': request_headers['Accept-Language'],
			'Cookie': user.headers['Set-Cookie'],
			'X-Requested-With': request_headers['X-Requested-With'],
		}
		# 不写header会跳转到线上的下载页面
		# oil_pay = requests.get('http://'+host[8034]+'/webapp/shihua/oilPay', params=oil_data)
		oil_pay = requests.get('http://'+host[8034]+'/webapp/shihua/oilPay', headers=oil_headers, params=oil_data)
		# print oil_pay.url
		# print oil_pay.content
		assert '我要支付' in oil_pay.content, '页面内容查询失败'

	def test_oil_confirm(self):
		""" 订单确认页面测试用例

		如果无法跳转到订单确认页面，有可能是银联接口问题，但是在测试环境会出现，线上几乎不会出现
		如果可以正常跳转到订单确认页面，可以选择取消订单操作（加油订单无法使用自动超时关闭订单，需要手动关闭订单）
		"""


