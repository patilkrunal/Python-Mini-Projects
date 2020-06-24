#! python3


def function(x, k, P):
	for i in range(k):
		A = input().split()
		# p[i] = [i for i in input().split]
		P.append(A)

	# print(P)

	L = list(zip(*P))
	# print(type(L[0][0]))
	# print(L)


	for i in range(x):
		mysum = sum( map(float, list(L[i])) )/k
		print(round(mysum,2))

if __name__ == '__main__':
	x, k = input().split()
	# x, k = 5, 3

	P = []
	# P = [ ['89', '90', '78', '93', '80'],
	#       ['90', '91', '85', '88', '86'],
	#       ['91', '92', '83', '89', '90.5'],
	# 		]

	function(int(x), int(k), P)