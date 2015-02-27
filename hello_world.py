# -*- coding: utf-8 -*-
# first python test
print("hello world!")
count = 0

while count < 3:
	print('loop #%d' % count)
	count += 1

print('I like to use the Internet for:')
for item in ['e-mail', 'net-surfing', 'homework', 'chat']:
	print(item)


for num in range(10):
	print(num)

# foo = 'abc'			# 引用模块内部属性时，如果该变量可用，就不会使用到下面的foo函数
for c in foo:
	print(c)

for i in range(len(foo)):
	print(foo[i], '(%d)' % i)

for i, ch in enumerate(foo, start=0):		# 使用enumerate函数
	print(i, ch)


squared = [x ** 2 for x in range(4)]
for i in squared:
	print(i)

def add_two_nums(x):				# 函数的小括号即使在没有参数的情况下也不能省略
	'apply + operation to argument'
	return(x + x)

