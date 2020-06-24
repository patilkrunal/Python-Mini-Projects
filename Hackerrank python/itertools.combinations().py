#!/bin/python3
from itertools import combinations

def solve(s, k):
    for j in range(1,k+1):
        mylist = list(combinations(s, j))
        for i in mylist:
            print("".join(i), end="\n")


if __name__ == '__main__':
    s, k = input().split()
    solve(sorted(s), int(k))
