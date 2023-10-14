import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox,filedialog
import pytube
import os
class YoutubeDownloader:
    urlPath=""
    def __init__(self):
        #initializing window
        self.ytwin=tk.Tk()
        self.ytwin.title("Youtube Downloader")
        self.ytwin.geometry("600x370")
        self.ytwin.config(bg="navy")
        self.ytwin.resizable(0,0)

        #label for url entry
        urlLabel=tk.Label(self.ytwin,text="Paste youtube video url below",font=("Arial",16,"bold"),bg="navy",fg="white")
        urlLabel.pack(pady=30)

        #Textbox for url entry
        self.urlEntry = tk.Entry(self.ytwin,textvariable = self.urlPath, font=('calibre',15,'normal'),width="300")
        self.urlEntry.pack(padx=30,ipadx=5,ipady=3)

        #label for download status
        self.status=tk.Label(self.ytwin,text="",font=("Arial",12,"bold"),bg="navy",fg="white")
        self.status.pack(pady=15)


        #Vidoe download button
        download_mp4=tk.Button(self.ytwin,text="Download MP4",font=("Arial",10,"bold"),bg="lime",fg="navy",command=self.downloadMP4)
        download_mp4.pack(pady=20,ipady=5,ipadx=10)

        #Audio download button
        download_mp3=tk.Button(self.ytwin,text="Download MP3",font=("Arial",10,"bold"),bg="lime",fg="navy",command=self.downloadMP3)
        download_mp3.pack(pady=10,ipady=5,ipadx=10)
        
        self.ytwin.mainloop()
    def downloadMP4(self):
        if(self.urlEntry.get().strip(" ")!=""):
            try:
                yt=pytube.YouTube(self.urlEntry.get())
                self.status.configure(text="Downloading...")
            except:
                self.status.configure(text="Download Failed...")
            savePath=filedialog.askdirectory()
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=savePath)
            self.urlEntry.delete(0,'end')
            self.status.configure(text="Download finished...")
            messagebox.showinfo("Success","Video downloaded")
        else:
            messagebox.showerror("Error","Please enter valid video url")

    def downloadMP3(self):
        if(self.urlEntry.get().strip(" ")!=""):
            try:
                yt=pytube.YouTube(self.urlEntry.get())
                self.status.configure(text="Downloading...")
            except:
                self.status.configure(text="Download Failed...")
            savePath=filedialog.askdirectory()
            stream = yt.streams.filter(only_audio=True).first()
            out_file=stream.download(output_path=savePath)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            self.urlEntry.delete(0,'end')
            self.status.configure(text="Download finished...")
            messagebox.showinfo("Success","Audio downloaded")
        else:
            messagebox.showerror("Error","Please enter valid video url")