# coding: utf-8
try:
	assert 1 == 0, 'One does not equal zero silly!'
except AssertionError as args:
	print('%s: %s' % (args.__class__.__name__, args))