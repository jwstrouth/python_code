
import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

def Test():
    window = tk.Tk()

    for relief_name, relief in border_effects.items():
        frame = tk.Frame(master=window, relief=relief, borderwidth=5)
        frame.pack(side=tk.LEFT)
        label = tk.Label(master=frame, text=relief_name)
        label.pack()

    window.mainloop()

class Basic():
    def __init__(self):
        self.window = tk.Tk()
    
    def run(self):
        self.window.mainloop()

class FrameEffect(Basic):

    def __init__(self):
        super().__init__()
            
    def setup(self):
        for relief_name, relief in border_effects.items():
            self.frame = tk.Frame(master=self.window, relief=relief, borderwidth=5)
            self.frame.pack(side=tk.LEFT)
            self.label = tk.Label(master=self.frame, text=relief_name)
            self.label.pack()

if __name__ == '__main__':
    #Test()
    #b = Basic()
    #b.run()
    fe = FrameEffect()
    fe.setup()
    fe.run()
