def DesignerDoorMat():
    Height, Width = map(int, input().split())
    # print(Height//2)

    # #Top Part
    x =  Height//2  # x=3
    for i in range(x):
        print( "-"*(3*x-3*i) + ".|."*(2*i+1) + "-"*(3*x-3*i))

    # #Central Line
    print( ("WELCOME").center(Width, '-') )

    # #Bottom Part
    for i in range(x):
        print("-"*(3*(i+1)) + ".|."*(2*(x-i-1)+1) + "-"*(3*(i+1)))

if __name__ == '__main__':
    DesignerDoorMat()