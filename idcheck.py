#!usr/bin/end python

import string

alphas = string.ascii_letters + '_'
nums = string.digits
alphnums = alphas + nums
print('Welcome to the Identifier Checker v1.0')
print('Testees must be at least 2 chars long.')
inp = input('Identifier to test:')

if len(inp) > 1:
    if inp[0] not in alphas:
        print('''invalid: first symbol must be alphabetic''')
    else:
        for otherChar in inp[1:]:
        	if otherChar not in alphnums:
            # if otherChar not in alphas + nums:		# 此处这样重复计算在性能上是非常低效的
                print('''invalid: remaining symbols must be alphanumeric''')
            break
            else:
                print('okay as an identifier')
