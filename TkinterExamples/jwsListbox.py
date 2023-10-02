
import tkinter as tk
from tkinter.filedialog import askopenfilename

class Basic():
    def __init__(self):
        self.window = tk.Tk()
    
    def run(self):
        self.window.mainloop()

class List(Basic):

    def __init__(self):
    
        super().__init__()
        choices = ["apple", "orange", "banana"]
        choicesvar = tk.StringVar(value=choices)
        self.statusmsg = tk.StringVar()
        self.l = tk.Listbox(self.window, listvariable=choicesvar)
        self.s = tk.Label(self.window, textvariable=self.statusmsg)
        choices.append("peach")
        choicesvar.set(choices)
        self.l.selection_set(2)
        self.l.see(2)
        #l.pack()
        self.l.grid()
        self.s.grid()
        self.l.bind('<<ListboxSelect>>', self.show)
        self.l.bind('<Double-1>', self.show)
        self.l.bind('<Return>', self.show)
        
    def show(self, *args):
        i=self.l.curselection()
        print('selection = '+str(int(i[0])))
        self.statusmsg.set("selection %s" % str(int(i[0])))

if __name__ == '__main__':

    l = List()
    l.run()
