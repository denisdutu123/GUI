from tkinter import *
import random
from tkinter import messagebox


screen = Tk()
screen.geometry("500x550")
screen.title("Jumbo Game")


correct = ["chicken", "burger", "chips", "night", "keyboard", "mouse", "spotify", "games", "dictonarie", "flower", "fragrance", "deodrant", "monitor", "house", "holiday", "england"]

wrong = ["ckicenh", "greurb", "spihc", "tgnih", "kyorybde", "mueos", "yiosptf", "asegm", "dcoaiernti", "rwlof", "rgacenraf", "dornedat", "mootrni", "ouseh", "ydlhoia", "lanengd"]

'''amount = len(correct)
print(amount)
rand = random.randint(0, 16)
print(wrong[rand])'''

corr = 0
total = 0
score = ""
ran = random.randint(0, 15)
def generate():
    global correct, wrong, ran
    rando = wrong[ran]
    display.config(text = rando)

def chek():
    global correct, wrong, corr, total, score, ran
    total +=1
    ent = entry.get()
    if correct[ran] == ent:
        messagebox.showinfo("Correct", "you have guessed the word")
        corr +=1
    else:
        messagebox.showinfo('Wrong', "that was not the word")
    score = "score:" + str(corr) + "/" + str(total)
    scor.config(text = score)
    res()

def res():
    global correct, wrong, ran
    ran = random.randint(0, 15)
    rando = wrong[ran]
    display.config(text = rando)
        
        

title = Label(screen, text = "Jumble Word Game", font = ("courgette", 25))
title.place(x = 150, y = 30)

entry = Entry(screen, width = 10, font = ("courgette", 20))
entry.place(x = 180, y = 210)

check = Button(screen, text = "Check", font = ("courgette", 20), command = chek)
check.place(x = 200, y = 280)

reset = Button(screen, text = "Reset", font = ("courgette", 20), command = res)
reset.place(x = 200, y = 340)

scor = Label(screen, text = "Score:", font = ("courgette", 25))
scor.place(x = 20, y = 500)

display = Label(screen, text = "dis", font = ("courgette", 20))
display.place(x = 210, y = 120)

generate()







screen.mainloop()