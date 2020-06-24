#!/bin/python3


def solve():
    for i in range(int(input())):
        a, b = input().split()
        # print(type(a), type(b))
        try:
            print(int(a)//int(b))
        except Exception as e:
            print(f"Error Code: {e}")

if __name__ == '__main__':
    solve()