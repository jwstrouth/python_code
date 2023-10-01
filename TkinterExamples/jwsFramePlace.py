
import tkinter as tk

class Basic():
    def __init__(self):
        self.window = tk.Tk()
    
    def run(self):
        self.window.mainloop()

class FramePlace(Basic):

    def __init__(self):
        super().__init__()
        
    def setup(self):
        frame = tk.Frame(master=self.window, width=150, height=150)
        frame.pack()

        label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
        label1.place(x=0, y=0)

        label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
        label2.place(x=75, y=75)
        
if __name__ == '__main__':
    fp = FramePlace();
    fp.setup()
    fp.run()
