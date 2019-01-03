filename = "name.txt"
def write():
	name = input("please input your name:\n")
	with open(filename,'w') as file:
		file.write(name)

def read():
	with open(filename) as file:
		print("this is your name:"+file.read()) 

write()
read()
