import numpy as np

def Arrays():
    a = []
    a = np.array(input().split(), float)
    arr = a[::-1]
    # arr = np.flipud(a)
    print(arr)

def main():
    Arrays()

if __name__ == '__main__':
    main()

