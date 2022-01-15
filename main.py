import os, sys
sys.path.append(os.getcwd() + "/lib")

import src.parse as csvparser
import numpy as np

parser = csvparser.parser("data.csv")

parser.parse()
