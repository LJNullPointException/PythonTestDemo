#_*_coding:utf-8_*_
def mabs(num):
	if not isinstance (num,(int, float)):
		print("typeErro we need Interge or Float ,but you give me s%" ,type(num))
		return;
	if num>0:
		return num;
	else:
		return -num;