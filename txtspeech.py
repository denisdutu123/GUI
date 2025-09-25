from tkinter import *
from gtts import gTTS
import os
from googletrans import Translater 


screen = Tk()
screen.geometry("700x700")

def txspe():
    langua = "en"
    ent = entry.get()
    if ent.strip() == "":
        return
    conver = gTTS(text = ent, lang = langua, slow = False)
    conver.save("filess.mp3")
    os.system("afplay filess.mp3")

tpframe = Frame(screen, bg = "Red", height = 250)
tpframe.pack(fill = X)
btframe = Frame(screen, bg = "Blue", height = 450)
btframe.pack(fill = X)

title = Label(tpframe, text = "Text To Speech", font = ("courgette", 35), bg = "Red")
title.place(x = 220, y = 80)

entry = Entry(btframe, width = 30, font = ("courgette", 25))
entry.place(x = 90, y = 120)

submit = Button(btframe, width = 20, text = "Submit", bg = "Blue", command = txspe)
submit.place(x = 230, y = 300)

translate = Button(btframe, width = 20, text = "Translate")
translate.place(x = 230, y = 350)


















screen.mainloop()
