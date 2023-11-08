import numpy as np
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Giải hệ phương trình n ẩn")
win.geometry('900x500')
win.configure(bg='white')

Label(win, text='Giải hệ phương trình n ẩn', font=('Arial', 13), bg='white', fg='black', height=2, relief='solid',
      borderwidth=2, width=40).place(x=250, y=0)

sopt = StringVar()
Label(win, text='Nhập số phương trình', font=('Arial', 13), bg='white', fg='black', height=2, relief='solid',
      borderwidth=2, width=30).place(x=250, y=60)
Entry(win, textvariable=sopt, font=('Arial', 14), bg='white', fg='black', relief='solid', borderwidth=2,
      width=5).place(x=555, y=60)

a = 'abcdefghijklmnopqrstuvwxyz'
a1 = list(a)
A = []
entries_A = []
B = []
entries_B = []

class Cal:
    def __init__(self, A, entries_A, B, entries_B):
        self.A = A
        self.entries_A = entries_A
        self.B = B
        self.entries_B = entries_B

    def create(self):
        try:
            if int(sopt.get()) <= 0:
                messagebox.showwarning("Chú ý", "Số phương trình phải > 0")
            for i in range(int(sopt.get())):
                self.A.append([])
                self.entries_A.append([])
                self.B.append([])
                self.entries_B.append([])
                for j in range(int(sopt.get())):
                    self.A[i].append(StringVar())
                    if i != 0:
                        Label(win, background='white', font=('Arial', 12), text=' + ' + f'x{i} ',
                              width=3, bg='white', fg='black').place(x=250 + 80 * i, y=110 + 30 * j)
                    else:
                        Label(win, background='white', font=('Arial', 12), text = f'x{i} ',
                              width=3, bg='white', fg='black').place(x=250 + 80 * i, y=110 + 30 * j)
                    self.entries_A[i].append(Entry(win, textvariable=self.A[i][j], width=3))
                    self.entries_A[i][j].place(x=280 + 83 * j, y=110 + 30 * i)
                self.B[i].append(StringVar())
                Label(win, background='white', font=('Arial', 12), text=' = ',
                      width=3, bg='white', fg='black').place(x=310 + 83 * (int(sopt.get()) - 1), y=110 + 30 * i)
                self.entries_B[i].append(Entry(win, textvariable=self.B[i][0], width=3))
                self.entries_B[i][0].place(x=200 + 83 * (int(sopt.get()) + 1), y=110 + 30 * i)
        except:
            messagebox.showwarning("Chú ý", "Kiểu dữ liệu không đúng!")

    def get_mat_A(self):
        matrix_A = []
        for i3 in range(int(sopt.get())):
            matrix_A.append([])
            for j3 in range(int(sopt.get())):
                if self.A[i3][j3].get() != None:
                    matrix_A[i3].append(float(self.A[i3][j3].get()))
                else:
                    messagebox.showwarning("Thiếu dữ liệu", f'Nhập thiếu hệ số của {a1[j3]}{i3}')

        return np.array(matrix_A)

    def get_mat_B(self):
        matrix_B = []
        for i3 in range(int(sopt.get())):
            matrix_B.append([])
            for j3 in range(1):
                if self.B[i3][j3].get() != None:
                    matrix_B[i3].append(float(self.B[i3][j3].get()))
                else:
                    messagebox.showwarning("Thiếu dữ liệu", f'Nhập thiếu hệ số của phương trình thứ {i3}')
        return np.array(matrix_B)

    def calculate(self):
        try:
            A = Cal.get_mat_A(self)
            B = Cal.get_mat_B(self)
            if np.linalg.det(A) != 0:
                X = np.dot(np.linalg.inv(A), B)
                for i in range(int(sopt.get())):

                    Label(win, background='white', font=('Arial', 12), fg='black', text=f'x{i} = ',
                          width=4, bg='white').place(x=290 + 83 * i, y=270)
                    Label(win, background='white', font=('Arial', 12), fg='black', text=f'{round(X[i][0], 2)}' + ', ',
                          width=4, bg='white').place(x=330 + 83 * i, y=270)
            else:
                messagebox.showwarning("Lỗi!", "Ma trận không khả nghịch")
        except:
            messagebox.showwarning("Lỗi!", "Nhập sai!")

def clear():
    Label(win, background='white', width=180 * int(sopt.get()), height=20).place(x=240, y=110)
    Label(win, background='white', width=100).place(x=280, y=650)
    A = []
    entries_A = []
    B = []
    entries_B = []
    cal = Cal(A, entries_A, B, entries_B)
    Button(win, text='Create', command=cal.create, font=('Times new roman', 15), fg='black', bg='white', width=6,
       height=2, relief='solid', borderwidth=2).place(x=280, y=310)
    Button(win, text='Clear', command=clear, font=('Times new roman', 15), fg='black', bg='white', width=6, height=2,
       relief='solid', borderwidth=2).place(x=380, y=310)
    Button(win, text='Calculate', command=cal.calculate, font=('Times new roman', 15), fg='black', bg='white', width=8,
       height=2, relief='solid', borderwidth=2).place(x=480, y=310)


cal = Cal(A, entries_A, B, entries_B)
Button(win, text='Create', command=cal.create, font=('Times new roman', 15), fg='black', bg='white', width=6,
       height=2, relief='solid', borderwidth=2).place(x=280, y=310)
Button(win, text='Clear', command=clear, font=('Times new roman', 15), fg='black', bg='white', width=6, height=2,
       relief='solid', borderwidth=2).place(x=380, y=310)
Button(win, text='Calculate', command=cal.calculate, font=('Times new roman', 15), fg='black', bg='white', width=8,
       height=2, relief='solid', borderwidth=2).place(x=480, y=310)

win.mainloop()
