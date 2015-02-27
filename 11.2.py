#!/usr/bin/env/python
# -*- coding: utf-8 -*-
####################
#使用函数方法将其与0做比较判断其大于0，小于0或等于0
####################
def fun(c):
    x = c
    print('你输入的是：', x)
    try:
        int(x)
    except ValueError:
        print('你输入的不是数字')

    if x < 0:
        print('你输入的是小于零的数字')
    elif x > 0:
        print('你输入的是大于0的数字')
    else:
        print('你输入的数字等于0')

if __name__ == '__main__':
    fun(5)
    fun(90)
    fun(3)
    fun(-3)
    fun(0)

