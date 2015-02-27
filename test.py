#!/usr/bin/env/python
# -*- coding: utf-8 -*-
####################
#文本菜单程序，(1)手动输入五个数，求五个数的和(2)求五个数的平均值(X)退出。
####################
def sort_nums(x, y, z):
    for i in range(2):
        if x < y:
            x, y = y, x
        if y < z:
            y, z = z, y
    print(x, y, z)
if __name__ == '__main__':
    sort_nums(1, 2, 3)
    sort_nums(2, 1, 3)
    sort_nums(1, 3, 2)
    sort_nums(3, 1, 2)
    sort_nums(3, 2, 1)
    sort_nums(2, 3, 1)
