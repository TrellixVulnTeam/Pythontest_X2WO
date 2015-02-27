# coding: utf-8
def safe_float(obj):
	try:
		retval = float(obj)
	except ValueError:		#这种方式只能扑捉特定已知类型的异常
	# except Exceptiong as e:	#这种方式可以扑捉所有类型的异常
		retval = 'could not vonvert non-number to float'
	except TypeError:
		retval = 'argument must be a string'
	return retval
