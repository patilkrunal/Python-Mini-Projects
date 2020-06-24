import numpy as np

def TransposeandFlatten():
    n, m = map(int, input().split())

    matrix = []
    for i in range(n):
        mylist = np.array(list(map(int, input().split())))
        matrix.append(mylist)
    matrix = np.array(matrix)

    print(np.transpose(matrix))
    print(matrix.flatten())

def main():
    TransposeandFlatten()

if __name__ == '__main__':
    main()

