# Make a series of classes that print a triangle

class Shape:
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)

class Triangle(Shape):
	def printRow(self, i):
		print(self.printChar * (i + 1))
		
shapes = Triangle()
shapes.print()