from textwrap import indent
from .parse import parser
from .calculator import calculator


class trainerModule:
	def __init__(self, file: str) -> None:
		self.__parser = parser(file)
		self.__data = self.__parser.parse()
		self.clearThetas()
		self.__calculator = calculator(False)
		pass

	def clearThetas(self):
		try:
			with open("thetas.csv", "w") as file:
				file.write("theta0,theta1\n")
				file.close()
		except:
			try:
				with open("thetas.csv", "X") as file:
					file.write("theta0,theta1\n")
					file.close()
			except:
				print("error, could not create thetas.csv")

	def writeThetas(self, tmpTheta0, tmpTheta1):
		try: 
			with open("thetas.csv", "a") as file:
				file.write(str(tmpTheta0) + "," + str(tmpTheta1) + "\n")
		except:
			try:
				with open("thetas.csv", "X") as file:
					file.write("theta0,theta1\n")
					file.write(str(tmpTheta0) + "," + str(tmpTheta1) + "\n")
			except:
				print("error, could not create thetas.csv")

	def calculateIndex(self):
		index = 0;
		for row in self.__data:
			index += 1
		return index


	def train(self, learningRate: float):
		tmpTheta0 = 0
		tmpTheta1 = 0
		index = self.calculateIndex()

		for row in self.__data:
			row["index"] = index
			row["theta0"] = tmpTheta0
			row["theta1"] = tmpTheta1
			tmpTheta0 = learningRate * (1/index) * self.sumIndex()
			tmpTheta1 = learningRate * (1/index) * self.sumIndexWeighted()
			self.writeThetas(tmpTheta0, tmpTheta1)

	def sumIndex(self):
		reducer = 0
		for row in self.__data:
			res = abs(self.__calculator.calculate(int(row["km"])) - int(row["price"]))
			reducer += res
		return reducer

	def sumIndexWeighted(self):
		reducer = 0
		for row in self.__data:
			res = abs(self.__calculator.calculate(int(row["km"])) - int(row["price"]))
			res *= int(row["km"])
			reducer += res
		return reducer

	def res(self):
		self.__calculator.res()
