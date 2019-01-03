import json
def loasJson():
	filename = "jsontxt.txt"
	with open(filename) as file:
		number = json.load(file)
		print(number)

loasJson()