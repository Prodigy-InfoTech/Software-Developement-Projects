import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox,filedialog
import urllib.request
class WebpageDownloader:
    urlPath=""
    def __init__(self):
        #initializing window
        self.webdown=tk.Tk()
        self.webdown.title("Webpage Downloader")
        self.webdown.geometry("600x300")
        self.webdown.config(bg="navy")
        self.webdown.resizable(0,0)


        #Label for entry field
        urlLabel=tk.Label(self.webdown,text="Paste your webpage url below",font=("Arial",16,"bold"),bg="navy",fg="white")
        urlLabel.pack(pady=30)

        #Textbox for URL Entry
        self.urlEntry = tk.Entry(self.webdown,textvariable = self.urlPath, font=('calibre',15,'normal'),width="300")
        self.urlEntry.pack(padx=30,ipadx=5,ipady=3)\

        #Download button
        download_btn=tk.Button(self.webdown,text="Download Webpage",font=("Arial",10,"bold"),bg="lime",fg="navy",command=self.downWebpage)
        download_btn.pack(pady=20,ipady=5,ipadx=10)

        self.webdown.mainloop()
    def downWebpage(self):
        if(self.urlEntry.get().strip(" ")!=""):
            savePath=filedialog.askdirectory()
            urllib.request.urlretrieve(self.urlEntry.get(), savePath+"/index.html")
            self.urlEntry.delete(0,'end')
            messagebox.showinfo("Success","Webpage downloaded")
        else:
            messagebox.showerror("Error","Please enter valid pdf url")