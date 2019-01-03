#_*_coding:utf-8_*_
# 递归调用
def fact(n):
	if n==1:
		return 1;
	return n*fact(n-1)
