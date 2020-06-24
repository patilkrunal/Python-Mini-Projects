import numpy as np

def ShapeandReshape():
    a = np.array(input().split(), int)
    a.shape = (3, 3)
    print(a)

def main():
    ShapeandReshape()

if __name__ == '__main__':
    main()

