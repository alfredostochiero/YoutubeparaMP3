import pafy  
import glob
import os
from tkinter import *

window = Tk()

window.title("Converter Youtube em mp3")
window.geometry('500x300')

btn = Button(window, text="Clique aqui")

btn.grid(column=0, row=0)

window.mainloop()



'''
diretorio = os.path.dirname(os.path.abspath(__file__))
  
url = input("Cole o link da música : ")
video = pafy.new(url) 
titulo = video.title

print(titulo)
  
bestaudio = video.getbestaudio() 
bestaudio.download(filepath=diretorio+"/Musicas") 

####
'''
