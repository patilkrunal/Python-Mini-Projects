def nested_list():
    data = []
    for _ in range(int(input())):
        data.append([input(), float(input())])

    second_lowest = sorted(list(set([marks for name, marks in data])))[1]
    ans = sorted([name for name, marks in data if marks == second_lowest])
    print('\n'.join(ans))

def main():
    nested_list()

if __name__ == '__main__':
    main()