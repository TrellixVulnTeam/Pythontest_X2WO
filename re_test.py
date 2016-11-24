# -*- coding: utf-8 -*-
"""正则表达式测试"""
import re

while True:
    PHONE = input('请输入你的电话号码: ')
    if re.match(r'\d{3}-\d{3,8}', PHONE):
        print('你的电话号码没毛病')
        break
    else:
        print('电话号码错误~~~')
        continue

