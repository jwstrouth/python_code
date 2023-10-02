import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

class Basic():
    def __init__(self):
        self.window = tk.Tk()
    
    def run(self):
        self.window.mainloop()

class Canvas(Basic):

    def __init__(self):
    
        super().__init__()
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        #self.window.config(background="green")
        self.window.title("JWS Canvas Sketcher <click left mouse, hold, and drag>")
        #self.window.columnconfigure(0, weight=1)
        #self.window.rowconfigure(0, weight=1)
        #self.frame = tk.Frame(master=self.window, width=800, height=600)
        #self.frame.grid()
        
        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        
        self.canvas.bind('<Button-1>', self.saveposn)
        self.canvas.bind('<B1-Motion>', self.addline)
        self.canvas.bind('<B1-ButtonRelease>', self.donestroke)
        
        id = self.canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setcolor("red"))
        id = self.canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setcolor("blue"))
        id = self.canvas.create_rectangle((10, 60, 30, 80), fill="green", tags=('palette', 'palettegreen'))
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setcolor("green"))
        id = self.canvas.create_rectangle((10, 85, 30, 105), fill="white", tags=('palette', 'palettewhite'))
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setcolor("white"))
        id = self.canvas.create_rectangle((10, 110, 30, 130), fill="black", tags=('palette', 'paletteblack'))
        self.canvas.tag_bind(id, "<Button-1>", lambda x: self.setcolor("black"))
        
        self.setcolor('black')
        self.canvas.itemconfigure('palette', width=5)
        
        #self.canvas.create_line(10, 10, 100, 100, fill='red', width=5)
        
    def saveposn(self, event):
        # press left mouse button
        self.lastx, self.lasty = event.x, event.y
        #print('Button-1 (left mouse press)')
        
    def addline(self, event):
        # hold left mouse and drag to new event position
        self.canvas.create_line(self.lastx, self.lasty, event.x, event.y, fill=self.color, width=5, tags='currentline')
        # save the new position to the last x and y
        self.saveposn(event)
        #print('B1-Motion (hold left mouse and drag)')
        
    def setcolor(self, newcolor):
        self.color = newcolor
        self.canvas.dtag('all', 'paletteSelected')
        self.canvas.itemconfigure('palette', outline='lightgray')
        self.canvas.addtag('paletteSelected', 'withtag', 'palette%s' % self.color)
        self.canvas.itemconfigure('paletteSelected', outline='#999999')
        
    def donestroke(self, event):
        self.canvas.itemconfigure('currentline', width=5)
        

if __name__ == '__main__':

    c = Canvas()
    c.run()
    
