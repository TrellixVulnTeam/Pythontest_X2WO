#!/usr/bin/env/python
# -*- coding: utf-8 -*-
####################
#输入一个数字，然后输出这个数字的2次方值
####################
while True:
    try:
        x = int(input('请输入一个数字：'))
        break
    except ValueError:
        print('你输入的字符不是数字，请重新输入')
    
y = int(x) ** 2
print('你输入的数字的平方值为：', y)
