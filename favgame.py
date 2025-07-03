from tkinter import *

screen = Tk()
screen.title("Log In")
screen.geometry("800x700")
screen.config(background = "red")
def info():
    detuse = entry.get()
    detfgam = fgame.get()
    detsgame = sgame.get()
    file = open("text.txt", 'a')
    file.write(f"Username:{detuse}, first choice: {detfgam}\n, second choice:{detsgame}\n")
    #clear entry box
    entry.delete(0, END)
    fgame.delete(0, END)
    sgame.delete(0, END)

box = Spinbox(screen, from_=0, to= 1)
box.place(x = 550, y = 290)


#label
use = Label(screen, text = "Username:", background = "Grey", font = ("courgette", 30))
use.place(x = 100, y = 100)
firgame = Label(screen, text = "Call of Duty or Fortnite?", background = "Grey", font = ("corugette", 30))
firgame.place(x = 200, y = 225)
secgame = Label(screen, text = "Apex or Roblox?", background = "Grey", font = ("corugette", 30))
secgame.place(x = 200, y = 325)
#entry
entry = Entry(screen, background = "Grey", width = 20, font = ("courgette", 30))
entry.place(x = 250, y = 100)
fgame = Entry(screen, background = "Grey", font = ("Grey", 30))
fgame.place( x = 150, y = 275)
sgame = Entry(screen, background = "Grey", font = ("Grey", 30))
sgame.place( x = 150, y = 375)
#button
submit = Button(screen, text = "Submit", background = "Grey", font = ("courgette", 30), command = info)
submit.place(x = 200, y = 600)
screen.mainloop()