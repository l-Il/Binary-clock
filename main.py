from datetime import datetime
from time import sleep
from termcolor import colored


class Time:
    def __init__(self):
        self.A = [[0] * 6 for i in range(4)]
        self.output()

    def binary(self, i, column):
        if i == 0:
            self.A[0][column], self.A[1][column], self.A[2][column], self.A[3][column] = 0, 0, 0, 0
        elif i == 1:
            self.A[0][column], self.A[1][column], self.A[2][column], self.A[3][column] = 0, 0, 0, 1
        elif i == 2:
            self.A[0][column], self.A[1][column], self.A[2][column], self.A[3][column] = 0, 0, 1, 0
        elif i == 3:
            self.A[0][column], self.A[1][column], self.A[2][column], self.A[3][column] = 0, 0, 1, 1
        elif i == 4:
            self.A[0][column], self.A[1][column], self.A[2][column], self.A[3][column] = 0, 1, 0, 0
        elif i == 5:
            self.A[0][column], self.A[1][column], self.A[2][column], self.A[3][column] = 0, 1, 0, 1
        elif i == 6:
            self.A[0][column], self.A[1][column], self.A[2][column], self.A[3][column] = 0, 1, 1, 0
        elif i == 7:
            self.A[0][column], self.A[1][column], self.A[2][column], self.A[3][column] = 0, 1, 1, 1
        elif i == 8:
            self.A[0][column], self.A[1][column], self.A[2][column], self.A[3][column] = 1, 0, 0, 0
        elif i == 9:
            self.A[0][column], self.A[1][column], self.A[2][column], self.A[3][column] = 1, 0, 0, 1

    def output(self):
        while True:
            self.binary(datetime.now().hour // 10, 0)
            self.binary(datetime.now().hour % 10, 1)
            self.binary(datetime.now().minute // 10, 2)
            self.binary(datetime.now().minute % 10, 3)
            self.binary(datetime.now().second // 10, 4)
            self.binary(datetime.now().second % 10, 5)
            print('   ', colored(f'{datetime.now().hour // 10}{datetime.now().hour % 10}:{datetime.now().minute // 10}{datetime.now().minute % 10}:{datetime.now().second // 10}{datetime.now().second % 10}','cyan'))
            for i in range(4):
                for j in range(6):
                    print(f'{self.A[i][j]} ', end=' ')
                print()
            sleep(1)
            print()


_ = Time()
