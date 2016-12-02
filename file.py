# coding: utf-8
# file operating
f = open('hello_world.py', 'r', encoding='utf-8')
s1 = f.readline()	# 读取了第一句
s2 = f.readline()	# 读取了第二句
print(s1)
print(s2)
for eachline in f:	# 一下子读取所有行，输出和文件访问不必再进行交替，适用于文件大小适中的文件
	print(eachline)
f.close()

