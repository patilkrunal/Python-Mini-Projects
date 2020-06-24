#!/bin/python3
import calendar


def solve(month, day, year):
# def solve():

    weekday = {'0': 'MONDAY', '1': 'TUESDAY', '2': 'WEDNESDAY', '3': 'THURSDAY', '4': 'FRIDAY', '5': 'SATURDAY',
               '6': 'SUNDAY', }
    # print(weekday['0'])
    print(weekday[str(calendar.weekday(year, month, day))])


if __name__ == '__main__':
    mnth, day, yr = input().split()
    solve(int(mnth), int(day), int(yr))
    # solve()