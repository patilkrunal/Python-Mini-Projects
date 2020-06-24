#!/bin/python3


def solve(s):
    L = list(s)
    # print(L)

    L[0] = L[0].capitalize()
    for i in range(len(L) - 1):
        if L[i] == " " and L[i + 1].isalpha():
            L[i + 1] = L[i + 1].capitalize()
    # print(L)
    return ("".join(L))

if __name__ == '__main__':
    # s = input()
    s = "chris alan"

    result = solve(s)
    print(result)
