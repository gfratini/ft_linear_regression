from .parse import parser
class trainerModule:
	def __init__(self, file: str) -> None:
		self.__parser = parser(file)
		self.__data = self.__parser.parse()
		pass

	