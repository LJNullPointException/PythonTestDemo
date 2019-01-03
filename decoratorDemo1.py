#_*_ coding:utf-8_*_
import functools
def log(*text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**key):
			if text != None:
				print("%s %s()" %(text,func.__name__));
			else:
				print("%s()" %func.__name__);
			return func(*args,**key);
		return wrapper;
	return decorator;