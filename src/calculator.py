# add "lib" to module path
import os, sys
sys.path.append(os.getcwd() + "/lib")

from src.parse import parser
class calculator:

	def __init__(self, stdin: bool = True) -> None:
		self.__parser = parser("thetas.csv")
		self.__mileage = 0
		if self.__parser is None:
			self.__theta0 = 0
			self.__theta1 = 0
		else:
			self.getThetas()
			if self.error == True:
				return
		if self.error == False and stdin == True:
			self.__mileage = self.requestValue()
		else:
			self.__mileage = 0
		pass

	def requestValue(self):
		while True :
			try:
				mileage = int(input("enter mileage: "))
				if (mileage < 0):
					print("enter a POSITIVE number")
					continue
				return mileage
			except:
				print("enter a number, idiot...")
				continue

	def getThetas(self):
		thetas = self.__parser.parse()
		if thetas == []:
			self.__theta0 = 0.0
			self.__theta1 = 0.0
		for row in thetas:
			try:
				self.__theta0 = float(row["theta0"])
				self.__theta1 = float(row["theta1"])
			except:
				print("thetas.csv is corrupted")
				self.error = True
				return
		self.error = False

	def theta(self):
		return [self.__theta0, self.__theta1]

	def info(self):
		print("theta0\ttheta1\tmileage\n" + str(self.__theta0) + "\t" + str(self.__theta1) + "\t" + str(self.__mileage), "\n")

	def calculate(self, mileage=-1):
		self.getThetas()
		if mileage != -1:
			self.__mileage = mileage
		elif mileage < -1:
			return None
		self.__result = self.__theta0 + self.__theta1 * self.__mileage
		return self.__result

	def res(self):
		print("price for", self.__mileage, "kilometers:", self.__result)
