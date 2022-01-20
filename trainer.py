# add "lib" to module path
from asyncore import read
import os, sys
sys.path.append(os.getcwd() + "/lib")

import matplotlib.pyplot as plt
import pandas as pd
from src.training_model import trainerModule

trainer2 = trainerModule("data.csv")
trainer2.train(0.01)
def calculate(val):
	return trainer2.theta0 + trainer2.theta1 * val
y_0 = calculate(trainer2.data.min().km)
y_1 = calculate(trainer2.data.max().km)

plt.plot([trainer2.data.min().km, trainer2.data.max().km], [y_0, y_1])
plt.plot(trainer2.data.km, trainer2.data.price, "ro")

plt.show()