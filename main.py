from datetime import datetime
from tkinter import *


class Time:
    def __init__(self):
        self.A = [[0] * 6 for _ in range(4)]
        self.root = Tk()
        self.root.title('Clock')
        self.root.geometry('90x90')
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
        self.current = Label(self.root, font=('Consolas', 10), fg='#00FFFF', bg='#202020')
        self.binary_label = Label(self.root, font=('Consolas', 10), fg='#FFFFFF', bg='#202020')
        self.current.place(x=0, y=0, width=90)
        self.binary_label.place(x=0, y=20, width=90, height=70)
        self.loop()
        self.root.mainloop()

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

    def loop(self):
        self.binary(datetime.now().hour // 10, 0)
        self.binary(datetime.now().hour % 10, 1)
        self.binary(datetime.now().minute // 10, 2)
        self.binary(datetime.now().minute % 10, 3)
        self.binary(datetime.now().second // 10, 4)
        self.binary(datetime.now().second % 10, 5)
        self.current.config(text=f'{datetime.now().hour // 10}{datetime.now().hour % 10}:{datetime.now().minute // 10}{datetime.now().minute % 10}:{datetime.now().second // 10}{datetime.now().second % 10}')
        self.s = str(self.A).replace('],', '\n').replace('[', '').replace(']]', '').replace(' ', '').replace(',', ' ')
        self.binary_label.config(text=self.s)
        self.root.after(1000, self.loop)


_ = Time()
