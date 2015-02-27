# coding: utf-8
# 使用两个任意的整数进行任意运算
from operator import add, sub
from random import randint, choice
# 定义一个+-字符与函数对应的字典
ops = {'+': add, '-': sub}
# 定义需要任意选用的+-符号
op = choice('+-')
# 定义需要使用的两个整数
nums = (randint(1, 10), randint(1, 10))
# 求得结果值
ans = ops[op](*nums)
print(ans)