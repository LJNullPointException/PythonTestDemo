#_*_coding:utf-8_*_
import math
def quadratic(a,b,c):
	if not isTrueType(a)&isTrueType(b)&isTrueType(c):
		raise TypeError("Type bad error!!!!!!");
	else:
		return (a*b*c,2)
def isTrueType(temp):
	if not isinstance(temp,(int,float)):
		return False;
	else:
		return True;