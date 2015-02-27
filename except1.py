# coding: utf-8

def safe_float(obj):
	try:
		retval = float(obj):
	except(ValueError, TypeError):
		retval = 'argument must be a number or numeric string.'
	return retval

