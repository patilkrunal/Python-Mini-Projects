#!/bin/python3
from itertools import product, repeat


def solve():
    # A = list(map(int, input().split()))
    # B = list(map(int, input().split()))
    A = [1, 2]
    B = [3, 4]

    # print(A, B)
    # print( [product(a, b)] for (a, b) in (A , B) )

    sum = list(product(A, B))
    for i in range(len(sum)):
        print(sum[i], end=" ")

if __name__ == '__main__':
    solve()
