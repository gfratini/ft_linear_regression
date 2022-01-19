import pandas as pd

# exactly two columns are expected
# is assumed the first column is the independent variable

def read_thetas():
	return

class linear_model:
	def __init__(self, file: str) -> None:
		self.data = pd.read_csv(file)
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

	def theta0(self):
		means = self.data.mean()
		return means.price - self.theta1 * means.km

	def theta1(self):
		reducer_0 = 0
		reducer_1 = 0
		means = self.data.mean()

		for row in self.data.values:
			reducer_0 += (row[0] - means.km) * (row[1] - means.price)
			reducer_1 += (row[0] - means.km) ** 2
		return reducer_0 / reducer_1

	def least_squares(self):
		self.theta1 = self.theta1()
		self.theta0 = self.theta0()
		self.writeThetas(self.theta0, self.theta1)

	def train(self):
		self.least_squares()