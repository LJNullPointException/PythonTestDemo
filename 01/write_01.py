filename = "write01.txt"
def write():
	with open(filename,'w') as file:
		file.write("I love you\n");
		file.write("I miss you")

def read():
	with open(filename) as file:
		print(file.readline().rstrip())

write()
read()
