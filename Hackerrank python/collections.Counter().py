#!/bin/python3
from collections import Counter


def solve():
    # X = int(input())        # 10
    # shoes = Counter(map(int, input().split()))
    # N = int(input())      # 6
    # sum = 0
    # for i in range(N):
    #     size, price = map(int, input().split())
    #     if shoes[size] and shoes[size]>0:
    #         sum += price
    #         shoes[size] -= 1
    # print(sum)
# -----------------------------------
    # n = input()
    # boots = map(int, input().split())
    # orders = [map(int, input().split()) for _ in range(int(input()))]
    # result = 0
    # for i in orders:
    #     if i[0] in boots:
    #         result += i[1]
    #         boots.remove(i[0])
    # print(result)
# ---------------------------------------
    from collections import Counter
    n = int(input())
    s = Counter(map(int, input().split()))
    x = int(input())
    total = []
    for i in range(x):
        a, b = map(int, input().split())
        if s[a] > 0:
            total.append(b)
            s.subtract(Counter([a]))
        else:
            pass

    print(sum(total))

if __name__ == '__main__':
    solve()
