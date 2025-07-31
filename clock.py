from tkinter import *
from tkinter.ttk import*
from time import strftime

screen = Tk()
screen.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    labe.config(text = string)
    labe.after(1000, time)

labe = Label(screen, font = ("courgette", 25 ), background = "Red", foreground  = "green")
labe.pack()



time()
screen.mainloop()