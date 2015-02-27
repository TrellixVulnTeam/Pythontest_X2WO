# coding: utf-8
# python 写入文件

poem = ['白日依山尽，', '黄河入海流。', '欲穷千里目，', '更上一层楼。']

file = open('poem.txt', 'w+')
#------单行写入------
for stc in poem:
	file.write(stc+'\n')
#------多行写入-------
file.writelines(poem)

file.close()

f = open('poem.txt', 'r')
s = f.readlines()
for x in s:
	print(x)

f.close()