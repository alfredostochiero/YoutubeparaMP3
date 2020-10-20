import pafy  
import glob
import os
from tkinter import *

window = Tk()

window.title("Converter Youtube em mp3")
window.geometry('500x300')

lbl = Label(window, text="Cole a url no campo a seguir: ")
lbl.grid(column=0, row=0)

txt = Entry(window, width=35)
txt.grid(column=1,row=0)



def clicked():

    diretorio = os.path.dirname(os.path.abspath(__file__))
    
    url = txt.get()
    

    video = pafy.new(url) 
    title = video.title

    lbl.configure(text=title+' baixado com sucesso !! ')

    bestaudio = video.getbestaudio() 
    bestaudio.download(filepath=diretorio+"/Musicas") 






btn = Button(window, text="Clique aqui",command=clicked)

btn.grid(column=2, row=0)

window.mainloop()

