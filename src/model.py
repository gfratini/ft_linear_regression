from cmath import isnan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class linear_model:
	def __init__(self, file: str) -> None:
		self.file = file
		try:
			self.data = pd.read_csv(file)
		except:
			print(self.file, "is invalid")
			exit()
		self.theta0 = 0
		self.theta1 = 0
		self.__normalize()
		pass

	def __write_thetas(self):
		try: 
			with open("thetas.csv", "w") as file:
				file.write("theta0,theta1\n" + str(self.theta0) + "," + str(self.theta1) + "\n")
		except:
			try:
				with open("thetas.csv", "X") as file:
					file.write("theta0,theta1\n" + str(self.theta0) + "," + str(self.theta1) + "\n")
			except:
				print("error, could not create thetas.csv")

	def __normalize(self):
		mins = self.data.min()
		maxes = self.data.max()
		normalized = []

		for row in self.data.values:
			try:
				if isnan(row[0]) or isnan(row[1]):
					raise Exception
				normalized.append([
					(row[0] - mins.values[0]) / (maxes.values[0] - mins.values[0]),
					(row[1] - mins.values[1]) / (maxes.values[1] - mins.values[1])
				])
			except:
				print(self.file, "is invalid")
				exit()
		self.normalized = pd.DataFrame(normalized, columns=["km", "price"])

	def __denorm(self):
		mins = self.data.min()
		maxes = self.data.max()
		range_x = maxes.values[0] - mins.values[0]
		range_y = maxes.values[1] - mins.values[1]
		theta1 = self.theta1 * (range_y / range_x)
		theta0 = self.theta0 * range_y - ((self.theta1 * mins.values[0] * (range_y)) / range_x) + mins.values[1]
		self.theta0 = theta0
		self.theta1 = theta1

	def train(self, learning_rate: float):
		length = self.data.count().values[0]

		for i in range(10000):
			tmpTheta0 = learning_rate * (self.__total_error() / length)
			tmpTheta1 = learning_rate * (self.__total_error_weight() / length)
			self.theta0 -= tmpTheta0
			self.theta1 -= tmpTheta1
		self.__denorm()
		self.__write_thetas()
		self.__plot()

	def __total_error(self):
		reducer = 0
		for row in self.normalized.values:
			res = (self.theta0 + self.theta1 * row[0] - row[1])
			reducer += res
		return reducer

	def __total_error_weight(self):
		reducer = 0
		for row in self.normalized.values:
			res = (self.theta0 + self.theta1 * row[0] - row[1]) * row[0]
			reducer += res
		return reducer

	def	__plot(self):
		x = np.linspace(self.data.max().values[0], self.data.min().values[0])
		y = self.theta0 + self.theta1 * x

		plt.plot(x, y)
		plt.plot(self.data[self.data.columns[0]], self.data[self.data.columns[1]], "ro")

	def save_plot(self):
		plt.savefig("regression_result.png")

	def plot_live(self):
		plt.show()