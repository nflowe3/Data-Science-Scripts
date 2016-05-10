from math import sqrt, pi, exp, erf
from collections import Counter
from matplotlib import pyplot as plt
from random import random

def normal_pdf(x, mu=0, sigma=1):
	sqrt_two_pi = sqrt(2 * pi)
	return (exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

def normal_cdf(x, mu=0, sigma=1):
	return(1 + erf((x-mu) / sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
	""" Find the approximate inverse using binary search"""

	# if not standard, compute standard and rescale
	if mu != 0 or sigma != 1:
		return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

	low_z, low_p = -10.0, 0 	# normal_cdf(-10) is very close to 0
	hi_z, hi_p = 10, 1 			# normal_cdf(10) is very close to 1
	while hi_z - low_z > tolerance:
		mid_z = (low_z + hi_z) / 2
		mid_p = normal_cdf(mid_z)
		if mid_p < p:
			# midpoint is still too low, search above it
			low_z, low_p = mid_z, mid_p
		elif mid_p > p:
			# midpoint is still too high, search below it
			hi_z, hi_p = mid_z, mid_p
		else:
			break

	return mid_z 

def bernoulli_trial(p):
	return 1 if random() < p else 0

def binomial(n, p):
	return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p, n, num_points):
	data = [binomial(n, p) for _ in range(num_points)]

	# use a bar chart to show the actual binomial samples
	histogram = Counter(data)
	plt.bar([x - 0.4 for x in histogram.keys()],
			[v / num_points for v in histogram.values()],
			0.8,
			color='0.75')

	mu = p * n
	sigma = sqrt(n * p * (1 - p))

	# use a line chart to show the normal approximation
	xs = range(min(data), max(data) + 1)
	ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]
	plt.plot(xs, ys)
	plt.title("Binomial Distribution vs. Normal Approximation")
	plt.show()