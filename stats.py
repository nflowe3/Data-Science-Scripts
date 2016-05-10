from math import sqrt
from collections import Counter
from vector import sum_squares, dot

def mean(x):
	return sum(x) / len(x)

def median(v):
	n = len(v)
	sorted_v = sorted(v)
	midpoint = n // 2

	if n % 2 == 1:
		return sorted_v[midpoint]
	else:
		lo = midpoint - 1
		hi = midpoint
		return (sorted_v[lo] + sorted_v[hi]) / 2

def mode(x):
	""" Returns a list, might be more than one mode """
	counts = Counter(x)
	max_count = max(counts.values())
	return [x_i for x_i, count in counts.iteritems() if count == max_count]

def quantile(x, p):
	""" Returns the pth percentile in x """
	p_index = int(p * len(x))
	return sorted(x)[p_index]

def data_range(x):
	return max(x) - min(x)

def de_mean(x):
	""" translate x by subtracting its mean (so the result has mean 0) """
	x_bar = mean(x)
	return [x_i - x_bar for x_i in x]

def variance(x):
	""" assumes x has at least two elements """
	n = len(x)
	deviations = de_mean(x)
	return sum_squares(deviations) / (n - 1)

def standard_deviation(x):
	return sqrt(variance(x))

def covariance(x, y):
	n = len(x)
	return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
	stdev_x = standard_deviation(x)
	stdev_y = standard_deviation(y)
	if stdev_x > 0 and stdev_y > 0:
		return covariance(x, y) / stdev_x / stdev_y