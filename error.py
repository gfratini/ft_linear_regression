# add "lib" to module path
import os, sys
sys.path.append(os.getcwd() + "/lib")

import pandas as pd

data = pd.read_csv("data.csv")

theta0 = 0
theta1 = 0

with open("thetas.csv", "r") as file:
	headers = file.readline().strip("\n").split(",")
	thetas = file.readline().strip("\n").split(",")
	try:
		theta0 = float(thetas[0])
		theta1 = float(thetas[1])
	except:
		theta0 = 0
		theta1 = 0


abs_error = 0
calc_mean = 0
i = 1
for row in data.values:
	i += 1
	y = row[1]
	calc_y = theta0 + theta1 * row[0]
	abs_error += abs(y - calc_y)
	calc_mean += calc_y

calc_mean /= i

abs_error /= i

rel_error = (abs_error / calc_mean) * 100

print("absolute error is {:.2f}, relative error is {:.2f}%".format(abs_error, rel_error))