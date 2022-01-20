from .parse import parser
import pandas as pd

class trainerModule:
	def __init__(self, file: str) -> None:
		self.data = pd.read_csv(file)
		self.theta0 = 0
		self.theta1 = 0
		self.clearThetas()
		self.normalize()
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

	def normalize(self):
		mins = self.data.min()
		maxes = self.data.max()
		normalized = []

		for row in self.data.values:
			normalized.append([
				(row[0] - mins.km) / (maxes.km - mins. km),
				(row[1] - mins.price) / (maxes.price - mins.price)
			])
		self.normalized = pd.DataFrame(normalized, columns=["km", "price"])

	def denorm_one(self, val):
		mins = self.data.min()
		maxes = self.data.max()
		return mins.price + val * (maxes.price - mins.price)

	def denorm(self):
		mins = self.data.min()
		maxes = self.data.max()
		range_x = maxes.km - mins.km
		range_y = maxes.price - mins.price
		theta1 = self.theta1 * (range_y / range_x)
		theta0 = self.theta0 * range_y - ((self.theta1 * mins.km * (range_y)) / range_x) + mins.price
		return theta0, theta1


	def train(self, learningRate: float):
		length = self.data.count().km

		for i in range(10000):
			tmpTheta0 = learningRate * (self.sumIndex() / length)
			tmpTheta1 = learningRate * (self.sumIndexWeighted() / length)
			self.theta0 -= tmpTheta0
			self.theta1 -= tmpTheta1
		theta0, theta1 = self.denorm()
		self.theta0 = theta0
		self.theta1 = theta1
		self.writeThetas(theta0, theta1)

	def sumIndex(self):
		reducer = 0
		for row in self.normalized.values:
			res = (self.theta0 + self.theta1 * row[0] - row[1])
			reducer += res
		return reducer

	def sumIndexWeighted(self):
		reducer = 0
		for row in self.normalized.values:
			res = (self.theta0 + self.theta1 * row[0] - row[1]) * row[0]
			reducer += res
		return reducer

	def res(self):
		self.__calculator.res()
