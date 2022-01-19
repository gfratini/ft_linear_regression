# add "lib" to module path
from asyncore import read
import os, sys
sys.path.append(os.getcwd() + "/lib")

from src.training_model import trainerModule



# learningRate = 0.1

# trainer.train(learningRate)

# trainer.res()
from src.least_squares import linear_model
import matplotlib.pyplot as plt
import pandas as pd


# trainer = linear_model("data.csv")
# trainer.train()

trainer2 = trainerModule("data.csv")
trainer2.train(0.1)
y_0 = trainer2.theta0
y_1 = trainer2.theta0 + trainer2.theta1
plt.plot([0, 1], [y_0, y_1])
xs = []
ys = []
for row in trainer2.normalized:
	xs.append(row[0])
	ys.append(row[1])
plt.plot(xs, ys, "ro")
plt.show()