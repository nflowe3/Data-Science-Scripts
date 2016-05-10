
def fib(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	elif x == 2:
		return 2
	else:
		return fib(x - 1) + fib(x - 2)

fib_sum = 0
i = 0
while fib(i) <= 4000000:
	if fib(i) % 2 == 0:
		fib_sum += fib(i) 

	i += 1

print(fib_sum)