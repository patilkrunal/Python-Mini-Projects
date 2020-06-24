def Lists():
    a = []
    n = int(input())
    for i in range(n):
        cmd, *mylist = input().split()
        if cmd == 'insert':
            a.insert(int(mylist[0]), int(mylist[1]))
        elif cmd == 'print':
            print(a)
        elif cmd == 'remove':
            a.remove(int(mylist[0]))
        elif cmd == 'append':
            a.append(int(mylist[0]))
        elif cmd == 'sort':
            a.sort()
        elif cmd == 'pop':
            a.pop()
        else:
            a.reverse()

def main():
    Lists()

if __name__ == '__main__':
    main()

    # 12
    # insert 0 5
    # insert 1 10
    # insert 0 6
    # print
    # remove 6
    # append 9
    # append 1
    # sort
    # print
    # pop
    # reverse
    # print

    # [6, 5, 10]
    # [1, 5, 9, 10]
    # [9, 5, 1]