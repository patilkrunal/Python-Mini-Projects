
def print_formatted(n):
    w = len(bin(n))-2   # subtract 2 to remove 0x from the starting
    for i in range(1,n+1):
        print(str(i).rjust(w,' '),str(oct(i))[2:].rjust(w,' '),str(hex(i)[2:].upper()).rjust(w,' '),str(bin(i)[2:]).rjust(w,' '))
        # print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)