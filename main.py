
from src.calculator import calculator

calculator = calculator()

val, res = calculator.run()

print("price for {} kilometers is ${:.2f}".format(val, res))