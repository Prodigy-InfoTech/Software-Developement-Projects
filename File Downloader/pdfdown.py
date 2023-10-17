import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox,filedialog
import urllib.request
class PdfDownloader:
    urlPath=""
    def __init__(self):
        #initializing window
        self.pdfwin=tk.Tk()
        self.pdfwin.title("Pdf Downloader")
        self.pdfwin.geometry("600x300")
        self.pdfwin.config(bg="navy")
        self.pdfwin.resizable(0,0)


        #Label for entry field
        urlLabel=tk.Label(self.pdfwin,text="Paste your pdf url below",font=("Arial",16,"bold"),bg="navy",fg="white")
        urlLabel.pack(pady=30)

        #Textbox for URL Entry
        self.urlEntry = tk.Entry(self.pdfwin,textvariable = self.urlPath, font=('calibre',15,'normal'),width="300")
        self.urlEntry.pack(padx=30,ipadx=5,ipady=3)

        #Download button
        download_btn=tk.Button(self.pdfwin,text="Download Pdf",font=("Arial",10,"bold"),bg="lime",fg="navy",command=self.downPdf)
        download_btn.pack(pady=20,ipady=5,ipadx=10)
        
        self.pdfwin.mainloop()
    def downPdf(self):
        if(self.urlEntry.get().strip(" ")!=""):
            savePath=filedialog.askdirectory()
            urllib.request.urlretrieve(self.urlEntry.get(), savePath+"/download.pdf")
            self.urlEntry.delete(0,'end')
            messagebox.showinfo("Success","Pdf downloaded")
        else:
            messagebox.showerror("Error","Please enter valid pdf url")
