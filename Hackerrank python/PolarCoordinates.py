#!/bin/python3
from cmath import phase, polar


def solve():

    # complexval = '-1+2j'
    # number = complex(input())
    # print(abs(complex(number.real, number.imag)))
    # print(phase(complex(number.real, number.imag)))
    # -----------------------------------------------

    ans =  polar(complex(input()))
    print(ans[0])
    print(ans[1])

if __name__ == '__main__':
    solve()
