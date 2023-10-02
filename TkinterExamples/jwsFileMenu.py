
import tkinter as tk
from tkinter.filedialog import askopenfilename

def Test():

    def donothing():
        x = 0
   
    window = tk.Tk()
    menubar = tk.Menu(window)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    window.config(menu=menubar)
    window.mainloop()


class Basic():
    def __init__(self):
        self.window = tk.Tk()
    
    def run(self):
        self.window.mainloop()
        
class FileMenu(Basic):

    def __init__(self):
        super().__init__()
        self.window.title("JWS File Menu")
    
    def setup(self):
        
        menubar = tk.Menu(self.window)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.browser)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.window.config(menu=menubar)
        self.file_explorer = tk.Label(self.window, text="Explore files")
        #button = tk.Button(self.window, 
        #                   text="Browser Folder", 
        #                   font=("Roboto", 14), command=self.browser)
        self.file_explorer.pack()
        #button["fg"] = "red"
        #button["bg"] = "blue"
        #button.pack(pady=10)
        
    def donothing(self):
        pass
        
    def browser(self):
        f_path = askopenfilename(initialdir="/",
                                 title="Select File",
                                 filetypes=(("Text Files","*.*"), ("All Files", "*.*")))
        self.file_explorer.configure(text="File Opened: "+str(f_path))
        
if __name__ == '__main__':
    #Test()
    fm = FileMenu()
    fm.setup()
    fm.run()
    
