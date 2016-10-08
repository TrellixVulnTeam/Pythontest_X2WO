#!/usr/bin/env/python
__author__ = 'Zhanxueyou'
# -*- coding: utf-8 -*-
def fun_sum():
    """求五个值的和"""
    sum = 0
    a = []
    for i in range(5):
        print('请输入第', i+1, '个值：')
        while True:
            try:
                a.append(input())
                sum += int(a[i])
                break
            except ValueError:
                print('输入数值有误，请重新输入')
                a.pop()
    print('五数求和的值为：', sum)

if __name__ == '__main__':
    fun_sum()
