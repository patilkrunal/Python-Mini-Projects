#! python3
import time

def function():
	# Calculate the product of the first 100,000 numbers.
	product = 1
	for i in range(1, 100000):
		product = product * i
	return product

if __name__ == '__main__':
	startTime = time.time()
	prod = function()
	endTime = time.time()

	print(f'The result is {len(str(prod))} digits long.')
	print(f'Took {endTime - startTime} seconds to calculate.')
