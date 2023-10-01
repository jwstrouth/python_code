
import tkinter as tk

def Test():
    window = tk.Tk()

    frame_a = tk.Frame()
    label_a = tk.Label(master=frame_a, text="I'm in Frame A")
    label_a.pack()

    frame_b = tk.Frame()
    label_b = tk.Label(master=frame_b, text="I'm in Frame B")
    label_b.pack()

    # Swap the order of `frame_a` and `frame_b`
    frame_b.pack()
    frame_a.pack()

    window.mainloop()


class Basic():
    def __init__(self):
        self.window = tk.Tk()
        print("Basic __init__")
    
    def run(self):
        print("Basic run")
        self.window.mainloop()

class Label(Basic):

    def __init__(self):
        super().__init__()
        self.frame_a = tk.Frame()
        self.frame_b = tk.Frame()      
    
    def setupA(self):
        self.label_a = tk.Label(master=self.frame_a, text="I'm in Frame A")
        self.label_a.pack()
        print("Label setup a")
        
    def setupB(self):
        self.label_b = tk.Label(master=self.frame_b, text="I'm in Frame B")
        self.label_b.pack()
        print("Label setup b")
        
    def swap(self):
        # Swap the order of `frame_a` and `frame_b`
        self.frame_b.pack()
        self.frame_a.pack()
    
if __name__ == '__main__':
    #b = Basic()
    #b.run()
    #Test()
    l = Label()
    l.setupA()
    l.setupB()
    l.swap()
    l.run()

