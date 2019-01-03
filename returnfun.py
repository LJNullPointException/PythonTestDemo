#_*_coding:utf-8_*_
def fun(n):
	def funinner():
		i = 50;
		i=i+n;
		print(i)
		return i;
	return funinner;
