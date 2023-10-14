import tkinter as tk
from tkinter.ttk import *
from imgdown import ImageDownloader
from pdfdown import PdfDownloader
from webpagedown import WebpageDownloader
from youtubedown import YoutubeDownloader

def imageDown():
    ob=ImageDownloader()
def pdfDown():
    ob=PdfDownloader()
def webDown():
    ob=WebpageDownloader()
def ytDown():
    ob=YoutubeDownloader()

window=tk.Tk()
window.title("File Downloader")
window.geometry("400x400")
window.config(bg="#000aff")
window.resizable(0,0)

titleLabel=tk.Label(window,text="File Downloader",bg="#000aff",fg="white",font=("Arial",15,'bold'))
titleLabel.pack(pady=30)

imgBtn=tk.Button(window, text = "Image Downloader",command=imageDown,bg="yellow",fg="#000aff",font=("Arial",10,"bold"))
imgBtn.pack(pady = 10,ipadx=10,ipady=5)

pdfbtn=tk.Button(window, text = "Pdf Downloader",command=pdfDown,bg="yellow",fg="#000aff",font=("Arial",10,"bold"))
pdfbtn.pack(pady = 10,ipadx=10,ipady=5)

webBtn=tk.Button(window, text = "Webpage Downloader",command=webDown,bg="yellow",fg="#000aff",font=("Arial",10,"bold"))
webBtn.pack(pady = 10,ipadx=10,ipady=5)

ytBtn=tk.Button(window, text = "YouTube Downloader",command=ytDown,bg="yellow",fg="#000aff",font=("Arial",10,"bold"))
ytBtn.pack(pady = 10,ipadx=10,ipady=5)

window.mainloop()


