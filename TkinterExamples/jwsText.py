
import tkinter as tk
from tkinter.filedialog import askopenfilename

class Basic():
    def __init__(self):
        self.window = tk.Tk()
    
    def run(self):
        self.window.mainloop()

class Text(Basic):

    def __init__(self):
    
        super().__init__()
        t = tk.Text(self.window, width=40, height=10)
        t.pack()

if __name__ == '__main__':

    t = Text()
    t.run()
