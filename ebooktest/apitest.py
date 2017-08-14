#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
# 请求用户交易列表
# url = 'http://39.108.129.246:8000/api/getTransactionsByUser?address=7224593002791762865E'
# 请求用户状态信息
url = 'http://39.108.129.246:8000/api/getAccount?address=7224593002791762865E'
result = requests.get(url)
print(result.text)