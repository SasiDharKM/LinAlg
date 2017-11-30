#Just a library to code linear algebraic functions

class Vector(object):
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple(coordinates)
			self.dimension = len(coordinates)

		except ValueError:
			raise ValueError('The coordinates must be non-empty')

		except TypeError:
			raise TypeError('The coordinates must be an iterable')

	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)

	def __eq__(self, v):
		return self.coordinates == v.coordinates

	def plus(self, v):
		# A function to add two vectors
		new_coordinates = []
		n = len(self.coordinates)
		for i in range(n):
			new_coordinates.append(self.coordinates[i] + v.coordinates[i])
		return Vector(new_coordinates)
