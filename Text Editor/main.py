import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.filedialog import *


class TextEditor:
    def __init__(self):
        self.currentPath=""

        #Initializing window
        self.window=tk.Tk()
        self.window.geometry("800x500")
        self.window.title("Untitled Project")
        self.window.iconbitmap("favicon.ico")

        #Add textarea and scrollbar
        scrollbar = Scrollbar(self.window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.textarea = tk.Text(self.window, yscrollcommand=scrollbar.set,font=('Times New Roman', 18)) 
        self.textarea.pack(fill=tk.BOTH,expand=True) 
        # configuring the scrollbar 
        scrollbar.config(command=self.textarea.yview)

        menubar = tk.Menu(self.window) 
        # Adding File Menu
        file = tk.Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='File', menu = file)
        file.add_command(label ='New File', command = self.openNew) 
        file.add_command(label ='Open', command =self.openFile) 
        file.add_command(label ='Save', command = self.saveFile) 
        file.add_separator() 
        file.add_command(label ='Exit', command = self.window.destroy)
        edit = tk.Menu(menubar, tearoff = 0) 
        menubar.add_cascade(label ='Edit', menu = edit)
        edit.add_command(label ='Cut', command = self.cutText) 
        edit.add_command(label ='Copy', command =self.copyText) 
        edit.add_command(label ='Paste', command =self.pasteText) 
        self.window.config(menu = menubar)
        self.window.mainloop()
    def openNew(self):
        TextEditor()
    def openFile(self):
        filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=[("Text files","*.txt"),("All files", "*.*")])
        if(filename!=self.currentPath):
            f=open(filename,'r')
            data=f.read()
            self.textarea.insert(1.0,data)
        self.currentPath=filename
        self.window.title(self.currentPath)
    def saveFile(self):
        if self.currentPath=="":
            self.currentPath = fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if self.currentPath:
                self.window.title(self.currentPath)
                with open(self.currentPath,"w") as f:
                    content=self.textarea.get(1.0,"end-1c")
                    f.write(content)
        else:
            with open(self.currentPath,"w") as f:
                content=self.textarea.get(1.0,"end-1c")
                f.write(content)
    def cutText(self):
        self.textarea.event_generate("<<Cut>>")
    def copyText(self):
        self.textarea.event_generate("<<Copy>>")
    def pasteText(self):
        self.textarea.event_generate("<<Paste>>")
n=TextEditor()


