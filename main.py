from datetime import datetime
from time import sleep
from termcolor import colored

A = [[0] * 6 for i in range(4)]


def output():
    for i in range(4):
        for j in range(6):
            print(f'{A[i][j]} ', end=' ')
        print()


def binary(i, column):
    if i == 0:
        A[0][column], A[1][column], A[2][column], A[3][column] = 0, 0, 0, 0
    elif i == 1:
        A[0][column], A[1][column], A[2][column], A[3][column] = 0, 0, 0, 1
    elif i == 2:
        A[0][column], A[1][column], A[2][column], A[3][column] = 0, 0, 1, 0
    elif i == 3:
        A[0][column], A[1][column], A[2][column], A[3][column] = 0, 0, 1, 1
    elif i == 4:
        A[0][column], A[1][column], A[2][column], A[3][column] = 0, 1, 0, 0
    elif i == 5:
        A[0][column], A[1][column], A[2][column], A[3][column] = 0, 1, 0, 1
    elif i == 6:
        A[0][column], A[1][column], A[2][column], A[3][column] = 0, 1, 1, 0
    elif i == 7:
        A[0][column], A[1][column], A[2][column], A[3][column] = 0, 1, 1, 1
    elif i == 8:
        A[0][column], A[1][column], A[2][column], A[3][column] = 1, 0, 0, 0
    elif i == 9:
        A[0][column], A[1][column], A[2][column], A[3][column] = 1, 0, 0, 1


while True:
    print('   ', colored(
        f'{datetime.now().hour // 10}{datetime.now().hour % 10}:{datetime.now().minute // 10}{datetime.now().minute % 10}:{datetime.now().second // 10}{datetime.now().second % 10}',
        'cyan'))
    binary(datetime.now().hour // 10, 0)
    binary(datetime.now().hour % 10, 1)
    binary(datetime.now().minute // 10, 2)
    binary(datetime.now().minute % 10, 3)
    binary(datetime.now().second // 10, 4)
    binary(datetime.now().second % 10, 5)
    output()
    sleep(1)
    print()
