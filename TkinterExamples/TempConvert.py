#!/usr/bin/env python3

from tkinter import *


class App:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.c_var = DoubleVar()
        self.f_var = DoubleVar()
        Label(self.frame, text='deg C').grid(row=0, column=0)
        Entry(self.frame, textvariable=self.c_var).grid(row=0, column=1)
        Label(self.frame, text='deg F').grid(row=1, column=0)
        Entry(self.frame, textvariable=self.f_var).grid(row=1, column=1)
        buttonC = Button(self.frame, text='Convert Celsius', command=self.convertCelsius)
        buttonC.grid(row=2, columnspan=2)
        buttonF = Button(self.frame, text='Convert Fahrenheit', command=self.convertFahrenheit)
        buttonF.grid(row=3, columnspan=2)

    def convertCelsius(self):
        c = self.c_var.get()
        f = 1.8 * c + 32
        self.f_var.set(f)
        
    def convertFahrenheit(self):
        f = self.f_var.get()
        c = (f-32)/1.8
        self.c_var.set(c)
        



if __name__ == '__main__':
    root = Tk()
    root.wm_title('Temp Convert')
    app = App(root)
    root.mainloop()
