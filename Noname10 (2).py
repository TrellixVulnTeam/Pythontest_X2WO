#!/usr/bin/python
# -*- coding: utf-8 -*-

print('zhaxueyou')def fun(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
        print(a, end=' ')

fun(20)

