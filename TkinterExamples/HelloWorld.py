
from tkinter import *
from tkinter import ttk

def Test():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()

class Basic():
    def __init__(self):
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=10)
    
    def run(self):
        self.root.mainloop()
        
class Hello(Basic):
    
    def __init__(self):
        super().__init__()
        
    def setup(self):
        self.frame.grid()
        ttk.Label(self.frame, text="Hello World!").grid(column=0, row=0)
        ttk.Button(self.frame, text="Quit", command=self.root.destroy).grid(column=1, row=0)
        ttk.Button(self.frame, text="Hi", command=self.show).grid(column=2, row=0)
        
    def show(self):
        print('Hi')
        
if __name__ == '__main__':
    #Test()
    h = Hello()
    h.setup()
    h.run()
    

