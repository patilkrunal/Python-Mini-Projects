def AlphabetRangoli(n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    L = []

    # 5 = {e d c b a b c d e}
    w = 4*n-3
    for i in range(n):
        s = "-".join(alpha[i:n])
        # print(s)
        L.append((s[::-1] + s[1:]).center(w, '-'))
        # print(L[i])
    print("\n".join(L[:0:-1] + L))


if __name__ == '__main__':
    n = int(input())
    # n = 10
    AlphabetRangoli(n)