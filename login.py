from tkinter import *

screen = Tk()
screen.title("Log In")
screen.geometry("800x700")
screen.config(background = "red")
#label
use = Label(screen, text = "Username:", background = "Grey", font = ("courgette", 30))
use.place(x = 200, y = 200)
passwor = Label(screen, text = "Password:", background = "Grey", font = ("corugette", 30))
passwor.place(x = 200, y = 300)
#entry
entry = Entry(screen, background = "Grey", width = 20, font = ("courgette", 30))
entry.place(x = 350, y = 200)
passw = Entry(screen, background = "Grey", font = ("Grey", 30))
passw.place( x = 350, y = 300)
#button
submit = Button(screen, text = "Submit", background = "Grey", font = ("courgette", 30))
submit.place(x = 200, y = 375)
screen.mainloop()