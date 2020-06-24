import re

def Incorrect_Regex():
    for _ in range(int(input())):
        exp = input()
        try:
            re.compile(exp)
            print("True")
        except re.error:
            print("False")

def main():
    Incorrect_Regex()

if __name__ == '__main__':
    main()

