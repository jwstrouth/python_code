
import tkinter as tk
from tkinter.filedialog import askopenfilename

class Basic():
    def __init__(self):
        self.window = tk.Tk()
    
    def run(self):
        self.window.mainloop()

class JWSIDEMgr(Basic):

    def __init__(self):
    
        super().__init__()
        self.window.title("JWS IDE")
        self.frame = tk.Frame(master=self.window, width=800, height=600)
        self.frame.pack()
        
        # create menu
        self.menu = tk.Menu(self.window)
        # file menu
        self.fileMenu = tk.Menu(self.menu, tearoff=0)
        self.fileMenu.add_command(label="Open", command=self.open)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.exit)
        self.menu.add_cascade(label="File", menu=self.fileMenu)
        # help menu
        self.helpMenu = tk.Menu(self.menu, tearoff=0)
        self.helpMenu.add_command(label="About", command=self.about)
        self.menu.add_cascade(label="Help", menu=self.helpMenu)
        
        self.window.config(menu=self.menu)
        
    def open(self):
        print("Open")
        
    def exit(self):
        self.window.quit()
        
    def about(self):
        print("About")
        


if __name__ == '__main__':

    jwsIDE = JWSIDEMgr()
    jwsIDE.run()


