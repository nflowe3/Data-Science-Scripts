import math

"""
* Basic implementation of various vector related operations
* Author : Nigel Flower
"""

def vector_add(v, w):
	""" Adds the corresponding elements """
	return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
	""" Subtracts corresponding elements """ 
	return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
	""" Sums all corresponding elements """
	result = vectors[0]
	for vector in vectors:
		result = vector_add(result, vector)
	return result

def scalar_multiply(c, v):
	""" c is a constant, v is a vector """
	return [c * v_i for v_i in v]

def dot(v, w):
	""" Dot product of v and w """
	return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_squares(v):
	""" Sum of the squared values of a vector"""
	return dot(v, v)

def magnitude(v):
	""" The magnitude of a vector, i.e. the length"""
	return math.sqrt(sum_squares(v))

def squared_distance(v, w):
	""" Distance between two vectors, squared """
	return sum_squares(vector_subtract(v, w))

def distance(v, w):
	""" Absolute distance between two vectors """
	return magnitude(vector_subtract(v, w))
