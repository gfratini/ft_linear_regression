import csv

class parser :

	def __init__(self, file: str) -> None:
		self.__file = file
		pass

	def parse(self):
		with open(self.__file, newline='') as file :
			reader = csv.DictReader(file)
			print("km:\tprice:")
			# print(reader.restval)
			for row in reader :
				print(row["km"], "\t" ,row["price"])