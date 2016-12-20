#!/usr/bin/env/python
# -*- coding: utf-8 -*-
####################
#编写Hello World脚本，在系统环境中执行
####################
import os
import time
print('Hello World!')


print(os.path.realpath(__file__))	# 当前文件的路径
print(os.path.dirname(__file__))	# 当前文件的相对路径的目录，显示为空
print(os.path.abspath(os.path.dirname(__file__)))	# 当前文件的绝对路径的目录
# with open('4.txt', 'a') as f:
#     f.write(time.strftime('%Y-%m-%d %H:%M:%S ') + os.path.realpath(__file__) + '\n')
#     f.writelines('Hello'+'\n')
