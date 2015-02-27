# coding: utf-8
'''make-textfile.py  --  create text file'''
import os
ls = os.linesep		# 给出当前平台给出的行终止符，win使用‘\r\n’，Linux使用‘\n’,而mac使用‘\n’

while True:
	# get filename
	fname = input("Please input the file name(if you want to exit，input'.')：")
	if fname == '.':		# 如果想直接退出就键入‘.’直接退出程序
		quit()
	elif os.path.exists(fname):
		print("ERROR: %s already exists" % fname)
		continue
	else:
		break


# get file content (text) lines
all = []
print("\nEnter lines('.' by itself to quit).\n")

# loop until user terminates input
while True:
	entry = input('>')
	if entry == '.':
		break
	else:
		all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print('DONE!')