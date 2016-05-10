from collections import Counter
from matplotlib import pyplot as plt

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x - 4 for x in histogram.keys()],		# shift every bar to the left by 4
	histogram.values(),							# give each bar its correct height
	8)											# give each bar a width of 8

plt.axis([-5, 105, 0, 5])	# x axis from -5 to 105, y axis from 0 to 5

plt.xticks([10 * i for i in range(11)])	# x axis labels from 0 to 100 in steps of 10
plt.xlabel("Decile")
plt.ylabel("Number of Students")
plt.title("Distribution of exam grades")
plt.show()