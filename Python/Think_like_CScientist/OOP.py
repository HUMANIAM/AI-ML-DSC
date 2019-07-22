"""OOP is a programming paradigm. design the program as a set of objects and relationship
between them."""

class Point(object):
	"""Point has 2 attrs x axis and y axis two dimensional point"""
	def __init__(self, x=0, y=0):
		# super(Point, self).__init__()
		self.x = x
		self.y = y


	def distance_from_origin(self):
		""" compute the distance from origin"""
		return ((self.x ** 2) + (self.y ** 2)) ** 0.5

	def to_string(self):
		""""convert point object to string of this format (x, y)"""
		return "({0}, {1})".format(self.x, self.y)

	def __str__(self):
		return "({0}, {1})".format(self.x, self.y)


	def __add__(self, otherPoint):
		return Point(self.x + otherPoint.x, self.y + otherPoint.y)


	def __mul__(self, otherPoint):
		return Point(self.x * otherPoint.x, self.y * otherPoint.y)

	def __rmul__(self, scalar):
		return Point(scalar * self.x, scalar * self.y)




def main():
	p = Point(3, 4)
	p1 = Point(3, 4)

	print(p == p1)		
if __name__ == '__main__':
	main()