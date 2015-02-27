# coding: utf-8
'''readTextFile.py  -- read and display text file'''
import os

while True:
	fname = input('Enter filename:')
	if not os.path.exists(fname):
		print("Open file error\nPlease input filename again(input '.' to exit):")
		continue
	elif fname == '.':
	# elif fname == 'q':		# ??????如果是‘.’就可以正常退出，如果是其他字母就不行了??????
	# 如果输入的是字母，就会默认被识别为文件名而无法退出
		quit()
	else:
		# display contents to the screen
		fobj = open(fname, 'r')
		for eachLine in fobj:
			print(eachLine)
		fobj.close()
