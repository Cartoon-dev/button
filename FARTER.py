from tkinter import *
import playsound
from playsound import playsound
import os

farter = Tk()
farter.title('Fart Button')
farter.resizable(0, 0)
farter.minsize(230, 250)

lephoto = os.path.abspath("poopo.gif")


def fart():
    playsound(os.path.abspath("Fart_Meme_Sound.mp3"))


buttonImage = PhotoImage(file=lephoto)
Label(farter, image=buttonImage, bg='black').grid(row=0, column=0, sticky=E)

buton = Button(farter, text='fart', command=fart)

buton.grid()

farter.mainloop()
