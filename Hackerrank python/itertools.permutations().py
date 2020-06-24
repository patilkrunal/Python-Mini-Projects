# #!/bin/python3
# from itertools import permutations
#
#
# def solve():
#     s, n = input().split()
#     # s = "HACK"
#     # n = "2"
#     n = int(n)
#     mylist = list(permutations(s,n))
#     mylist.sort()
#     for i in mylist:
#         # print(i)
#         print("".join(i), end="\n")
# if __name__ == '__main__':
#     solve()



def permute(S, soFar, k):
    if len(soFar) == k:
        print(soFar)
        return
    else:
        for i in range(len(S)):
            permute(S[:i] + S[i+1:], soFar + S[i], k)

if __name__ == '__main__':
    S, k = input().split()
    permute(sorted(S), "", int(k))