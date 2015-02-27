# coding: utf-8
def safe_float(object):
	try:
		retval = float(object)
	except(ValueError, TypeError) as diag:
		retval = str(diag)
	return retval

