
import tkinter as tk

class Basic():
    def __init__(self):
        self.window = tk.Tk()
    
    def run(self):
        self.window.mainloop()

class FrameGrid(Basic):

    def __init__(self):
        super().__init__()
        
    def setup(self):
        for i in range(3):
            self.window.columnconfigure(i, weight=1, minsize=75)
            self.window.rowconfigure(i, weight=1, minsize=50)
            
            for j in range(3):
                frame = tk.Frame(master=self.window,
                                relief=tk.RAISED,
                                borderwidth=1)
                frame.grid(row=i, column=j, padx=10, pady=10)
                label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
                label.pack(padx=5, pady=5)

if __name__ == '__main__':
    fg = FrameGrid();
    fg.setup()
    fg.run()
