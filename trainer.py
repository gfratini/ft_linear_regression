# add "lib" to module path
import os, sys
sys.path.append(os.getcwd() + "/lib")

from src.trainerDef import trainerModule

trainer = trainerModule("data.csv")