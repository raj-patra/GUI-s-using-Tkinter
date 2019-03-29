"""

Simple Calculator using tkinter

Author : Raj Patra

Version 1.0

"""

from tkinter import *
import math


class Calculator():

    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def num_enter(self, num):
        self.result = False
        first_num = text.get()
        second_num = str(num)
        if self.input_value:
            self.current = second_num
            self.input_value = False
        else:
            if second_num == '.':
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display(self.current)

    def sum_of_total(self):
        self.result = False
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(text.get())

    def valid_function(self):
        if self.op == '+':
            self.total += self.current
        if self.op == '-':
            self.total -= self.current
        if self.op == '*':
            self.total *= self.current
        if self.op == '/':
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = '0'
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def display(self, value):
        text.delete(0, END)
        text.insert(0, value)

    def opPM(self):
        self.result = False
        self.current = -(float(text.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(text.get()))
        self.display(self.current)


added_value = Calculator()
root = Tk()
root.title("Calculator")
root.resizable(0, 0)
root.config(bg='black')
calc = Frame(root)
calc.grid()
# ================================Row0=======================================

text = Entry(calc, font=('Comic Sans MS', 20, 'bold'), bg='grey', bd=30,
             width=34, justify=RIGHT)
text.grid(row=0, column=0, columnspan=4, pady=1)
text.insert(0, '0')
# ================================Row1=======================================

btnClearEntry = Button(calc, pady=1, bd=4, bg='grey', width=8, height=2, text='CE', font=('Comic Sans MS', 20, 'bold'),
                       command=added_value.all_Clear_Entry).grid(row=1, column=0)

btnClear = Button(calc, pady=1, bd=4, bg='grey', width=8, height=2, text='C', font=('Comic Sans MS', 20, 'bold'),
                  command=added_value.Clear_Entry).grid(row=1, column=1)

btnSqrt = Button(calc, pady=1, bd=4, bg='grey', width=8, height=2, text='√', font=('Comic Sans MS', 20, 'bold'),
                 command=added_value.squared).grid(row=1, column=2)

btnAdd = Button(calc, pady=1, bd=4, bg='grey', width=8, height=2, text='+', font=('Comic Sans MS', 20, 'bold'),
                command=lambda: added_value.operation('+')).grid(row=1, column=3)

# ================================Row2=======================================

btn7 = Button(calc, pady=1, bd=4, bg='#25383C', width=8, height=2, text='7', font=('Comic Sans MS', 20, 'bold'),
              command=lambda: added_value.num_enter(7)).grid(row=2, column=0)

btn8 = Button(calc, pady=1, bd=4, bg='#25383C', width=8, height=2, text='8', font=('Comic Sans MS', 20, 'bold'),
              command=lambda: added_value.num_enter(8)).grid(row=2, column=1)

btn9 = Button(calc, pady=1, bd=4, bg='#25383C', width=8, height=2, text='9', font=('Comic Sans MS', 20, 'bold'),
              command=lambda: added_value.num_enter(9)).grid(row=2, column=2)

btnsub = Button(calc, pady=1, bd=4, bg='grey', width=8, height=2, text='-', font=('Comic Sans MS', 20, 'bold'),
                command=lambda: added_value.operation('-')).grid(row=2, column=3)

# ================================Row3=======================================

btn4 = Button(calc, pady=1, bd=4, bg='#25383C', width=8, height=2, text='4', font=('Comic Sans MS', 20, 'bold'),
              command=lambda: added_value.num_enter(4)).grid(row=3, column=0)

btn5 = Button(calc, pady=1, bd=4, bg='#25383C', width=8, height=2, text='5', font=('Comic Sans MS', 20, 'bold'),
              command=lambda: added_value.num_enter(5)).grid(row=3, column=1)

btn6 = Button(calc, pady=1, bd=4, bg='#25383C', width=8, height=2, text='6', font=('Comic Sans MS', 20, 'bold'),
              command=lambda: added_value.num_enter(6)).grid(row=3, column=2)

btnmul = Button(calc, pady=1, bd=4, bg='grey', width=8, height=2, text='*', font=('Comic Sans MS', 20, 'bold'),
                command=lambda: added_value.operation('*')).grid(row=3, column=3)

# ================================Row4=======================================

btn1 = Button(calc, pady=1, bd=4, bg='#25383C', width=8, height=2, text='1', font=('Comic Sans MS', 20, 'bold'),
              command=lambda: added_value.num_enter(1)).grid(row=4, column=0)

btn2 = Button(calc, pady=1, bd=4, bg='#25383C', width=8, height=2, text='2', font=('Comic Sans MS', 20, 'bold'),
              command=lambda: added_value.num_enter(2)).grid(row=4, column=1)

btn3 = Button(calc, pady=1, bd=4, bg='#25383C', width=8, height=2, text='3', font=('Comic Sans MS', 20, 'bold'),
              command=lambda: added_value.num_enter(3)).grid(row=4, column=2)

btnDiv = Button(calc, pady=1, bd=4, bg='grey', width=8, height=2, text='/', font=('Comic Sans MS', 20, 'bold'),
                command=lambda: added_value.operation('/')).grid(row=4, column=3)

# ================================Row5=======================================

btnDot = Button(calc, pady=1, bd=4, bg='grey', width=8, height=2, text='.', font=('Comic Sans MS', 20, 'bold'),
                command=lambda: added_value.num_enter('.') ).grid(row=5, column=0)

btn0 = Button(calc, pady=1, bd=4, bg='#25383C', width=8, height=2, text='0', font=('Comic Sans MS', 20, 'bold'),
              command=lambda: added_value.num_enter(0)).grid(row=5, column=1)

btnPM = Button(calc, pady=1, bd=4, bg='grey', width=8, height=2, text=chr(177), font=('Comic Sans MS', 20, 'bold'),
               command=added_value.opPM).grid(row=5, column=2)

btnEquals = Button(calc, pady=1, bd=4, bg='grey', width=8, height=2, text='=', font=('Comic Sans MS', 20, 'bold'),
                   command=added_value.sum_of_total).grid(row=5, column=3)

calc.config(bg='black')
root.mainloop()
