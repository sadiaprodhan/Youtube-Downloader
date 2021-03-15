from tkinter import *
from pytube import *

import sys
global file_size
var = Tk()
var.configure(background='#bfe1f5')
var.geometry('700x400')
var.resizable(0, 0)
var.title("Youtube-video Downloader")

Label(var, text="Youtube video downloader", font= 'TimesNewRoman 30 bold', bg='#bfe1f5').pack()

videolink = StringVar()
Label(var, text='Paste Link Here:', font = 'TimesNewRoman 15 bold',bg='#bfe1f5').place(x= 40 , y = 60)
linkentry= Entry(var,width= 80,textvariable= videolink).place(x= 40, y= 100)



def DownloadVideo():
    uri = YouTube(str(videolink.get()))
    result = uri.streams.get_highest_resolution()



    result.download(r'C:\Users\user\Downloads')

    Label(var, text='Downloaded',font='TimesNewRoman 18 bold', bg='#bfe1f5').place(x=270,y=200)

Button(var,text= 'Click to Download', font='TimesNewRoman 14', command=DownloadVideo).place(x=530,y=100)


var.mainloop()



