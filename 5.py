#!/usr/bin/env/python
# -*- coding: utf-8 -*-
####################
#编写一个脚本，在屏幕上显示你的名字、年龄、最喜欢的颜色，兴趣爱好等等
####################
#for line in open('4.txt'):
#	print(line)

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
	forward(200)
	left(170)
	if abs(pos()) < 1:
		break
end_fill()
done()
