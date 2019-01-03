#_*_conding:utf-8_*_
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print("%s %s();" %(text,func.__name__));
			return func(*args,**kw);
		return wrapper;
	return decorator