# add "lib" to module path
from cgi import test
import os, sys
sys.path.append(os.getcwd() + "/lib")

import pandas as pd

data = pd.read_csv("data.csv")

# print(
# 	data.km,
# 	data.sum().km,
# 	data.cumsum().km,
# 	data.mean().km,
# 	data.count(),
# 	sep="\n"
# )

for col in data.values:
	print(col)
	# for row in col:
	# 	print(row)
