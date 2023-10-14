import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox,filedialog
import urllib.request
from PIL import Image
class ImageDownloader:
    urlPath=""
    def __init__(self):
        #initializing window
        self.imgwin=tk.Tk()
        self.imgwin.title("Image Downloader")
        self.imgwin.geometry("600x300")
        self.imgwin.config(bg="navy")
        self.imgwin.resizable(0,0)

        #Label for entry field
        urlLabel=tk.Label(self.imgwin,text="Paste your image url below",font=("Arial",16,"bold"),bg="navy",fg="white")
        urlLabel.pack(pady=30)

        #Textbox for URL Entry
        self.urlEntry = tk.Entry(self.imgwin,textvariable = self.urlPath, font=('calibre',15,'normal'),width="300")
        self.urlEntry.pack(padx=30,ipadx=5,ipady=3)

        #Download button
        download_btn=tk.Button(self.imgwin,text="Download Image",font=("Arial",10,"bold"),bg="lime",fg="navy",command=self.downlmage)
        download_btn.pack(pady=20,ipady=5,ipadx=10)

        self.imgwin.mainloop()
        
    def downlmage(self):
        if(self.urlEntry.get().strip(" ")!=""):
            savePath=filedialog.askdirectory()
            urllib.request.urlretrieve(self.urlEntry.get(), savePath+"/download.png")
            self.urlEntry.delete(0,'end')
            messagebox.showinfo("Success","Image downloaded")
            img=Image.open(savePath+"/download.png")
            img.show()
        else:
            messagebox.showerror("Error","Please enter valid image url")
        
