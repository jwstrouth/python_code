
# see example, https://www.askpython.com/python-modules/tkinter/tkinter-treeview-widget

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

class Basic():
    def __init__(self):
        self.window = tk.Tk()
    
    def run(self):
        self.window.mainloop()

class TreeView(Basic):

    def __init__(self):
    
        super().__init__()
        self.window.title("JWS Tree View")
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.config(background="green")
        
        self.name_label = tk.Label(self.window, text="Name:")
        self.name_label.grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1, sticky=tk.W)
        self.idnumber_label = tk.Label(self.window, text="ID:")
        self.idnumber_label.grid(row=1, column=0, sticky=tk.W)
        self.idnumber_entry = tk.Entry(self.window)
        self.idnumber_entry.grid(row=1, column=1, sticky=tk.W)
        self.submit_button = tk.Button(self.window, text="Insert", command=self.insertdata)
        self.submit_button.grid(row=2, column=1, sticky=tk.W)
        
        self.tv = ttk.Treeview(self.window, columns=("Name", "Id"))
        self.tv.heading('#0', text='Item')
        self.tv.heading('#1', text='Name')
        self.tv.heading('#2', text='Id')
        self.tv.column('#0', stretch=tk.YES)
        self.tv.column('#1', stretch=tk.YES)
        self.tv.column('#2', stretch=tk.YES)
        self.item1 = self.tv.insert('', 'end', 'first', text='First')
        self.item2 = self.tv.insert(self.item1, 'end', 'second', text='Second')
        self.tv.grid(row=3, columnspan=4, sticky='nsew')
        
        self.id = 0
        self.iid = 0

    def insertdata(self):
        print('Insert Data')
        self.tv.insert(self.item2, 
                       'end', 
                       iid=self.iid, 
                       text="Item_" + str(self.id),
                       values=("Name: " + self.name_entry.get(),
                         self.idnumber_entry.get()))
        self.id +=1
        self.iid +=1

if __name__ == '__main__':

    tv = TreeView()
    tv.run()
    

