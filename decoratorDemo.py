#_*_coding:utf-8_*_
import functools;
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**key):
			print("%s %s()" %(text,func.__name__));
			return func(*args,**key);
		print("call end")
		return wrapper;
	return decorator;