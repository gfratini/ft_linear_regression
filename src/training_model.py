from locale import normalize
from statistics import mean
from textwrap import indent
from .parse import parser
from .calculator import calculator
import pandas as pd

class trainerModule:
	def __init__(self, file: str) -> None:
		self.data = pd.read_csv(file)
		self.normalized = []
		self.clearThetas()
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

	def getThetas(self):
		parser2 = parser("thetas.csv")
		thetas = parser2.parse()
		if thetas == []:
			self.theta0 = 0.0
			self.theta1 = 0.0
		for row in thetas:
			try:
				self.theta0 = float(row["theta0"])
				self.theta1 = float(row["theta1"])
			except:
				print("thetas.csv is corrupted")
				exit()

	def normalize(self):
		mins = self.data.min()
		maxes = self.data.max()

		for row in self.data.values:
			self.normalized.append([
				(row[0] - mins.km) / (maxes.km - mins. km),
				(row[1] - mins.price) / (maxes.price - mins.price)
			])

	def train(self, learningRate: float):
		self.getThetas()
		length = self.data.count().km
		
		self.normalize()

		for i in range(1000):
			tmpTheta0 = learningRate * (self.sumIndex() / length)
			tmpTheta1 = learningRate * (self.sumIndexWeighted() / length)
			self.theta0 -= tmpTheta0
			self.theta1 -= tmpTheta1
			self.writeThetas(self.theta0, self.theta1)

	def sumIndex(self):
		reducer = 0
		for row in self.normalized:
			res = (self.theta0 + self.theta1 * row[0] - row[1])
			reducer += res
		return reducer

	def sumIndexWeighted(self):
		reducer = 0
		for row in self.normalized:
			res = (self.theta0 + self.theta1 * row[0] - row[1]) * row[0]
			reducer += res
		return reducer

	def res(self):
		self.__calculator.res()
