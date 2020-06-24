#! python 3
cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
	a, b = 0, 1
	for i in range(n):
		yield a
		a, b = b, a + b


if __name__ == '__main__':
	n = int(input())
	print(list(map(cube, fibonacci(n))))