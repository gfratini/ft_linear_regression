# add "lib" to module path
import os, sys
sys.path.append(os.getcwd() + "/lib")

class calculator:

	def __init__(self) -> None:
		self.__get_thetas()
		self.__request_value()
		pass

	def __request_value(self):
		while True :
			try:
				input_value = int(input("enter a value: "))
				self.__input_value = input_value
				return
			except EOFError:
				exit()
			except:
				print("enter a number")
				continue

	def __get_thetas(self):
		try:
			with open("thetas.csv", "r") as file:
				file.readline()
				thetas = file.readline().strip("\n").split(",")
				self.__theta0 = float(thetas[0])
				self.__theta1 = float(thetas[1])
		except:
			print("Training data not found or corrupted")
			self.__theta0 = 0
			self.__theta1 = 0

	def run(self):
		self.__result = self.__theta0 + self.__theta1 * self.__input_value
		return self.__input_value, self.__result
