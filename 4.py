#!/usr/bin/env/python
# -*- coding: utf-8 -*-
####################
#编写Hello World脚本，在系统环境中执行
####################
import os
print('Hello World!')


print(os.path.realpath(__file__))
with open('4.txt', 'a') as f:
    f.write(os.path.realpath(__file__)+'\n')
    f.writelines('Hello'+'\n')
