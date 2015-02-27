#!/usr/bin/env/python
# -*- coding: utf-8 -*-
####################
#输入一个数字，将其与0做比较判断其大于0，小于0或等于0
####################
while True:
    try:
        x = int(input('请输入一个数字： '))
        break
    except ValueError:
        print('你输入的字符不是数字，请重新输入')

if x > 0:
    print('该值是大于零的值')
elif x < 0:
    print('该值是小于零的值')
else:
    print('该值等于0')

 