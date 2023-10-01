
import tkinter as tk

class Basic():
    def __init__(self):
        self.window = tk.Tk()
    
    def run(self):
        self.window.mainloop()

class FrameMgr(Basic):

    def __init__(self):
        super().__init__()
    
    def setup(self):
        frame1 = tk.Frame(master=self.window, width=100, height=100, bg="red")
        frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        frame2 = tk.Frame(master=self.window, width=50, height=50, bg="yellow")
        frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        frame3 = tk.Frame(master=self.window, width=25, height=25, bg="blue")
        frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

if __name__ == '__main__':
    f = FrameMgr()
    f.setup()
    f.run()
