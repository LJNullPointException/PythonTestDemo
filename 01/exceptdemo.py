import json
def dumpJson():
	filename = "jsontxt.txt"
	numbers = ['1','2','3','4']
	with open(filename,'w') as file:
		json.dump(numbers,file)
		print("save su")

dumpJson()