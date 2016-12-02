#!/usr/bin/env/python
# -*- coding: utf-8 -*-
####################
#编写Hello World脚本，在系统环境中执行
####################
import os
import time
print('Hello World!')


print(os.path.realpath(__file__))
print(os.path.dirname(__file__))
# with open('4.txt', 'a') as f:
#     f.write(time.strftime('%Y-%m-%d %H:%M:%S ') + os.path.realpath(__file__) + '\n')
#     f.writelines('Hello'+'\n')
