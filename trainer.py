# add "lib" to module path
import os, sys
sys.path.append(os.getcwd() + "/lib")

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from src.model import linear_model

trainer = linear_model("data.csv")
trainer.train(0.001, 100000)
trainer.save_plot()
# trainer.plot_live()