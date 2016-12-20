#!/usr/bin/env/python
# -*- coding: utf-8 -*-
####################
# debug的所有工具代码
####################
import os
import time
import sys

print(time.strftime('%Y-%m-%d %H:%M:%S'), os.path.realpath(__file__), '错误信息(行号%s)' % sys._getframe().f_lineno)

