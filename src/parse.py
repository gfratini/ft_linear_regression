import csv
import pandas as pd
class parser :

	def __init__(self, file: str) -> None:
		self.__file = file
		pass

	def parse(self):
		dataset = pd.read_csv(self.__file)

		try:
			with open(self.__file, newline='') as file :
				reader = csv.reader(file)
				headers = next(reader)
				return [dict(zip(headers,i)) for i in reader]
		except:
			return None
