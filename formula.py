from tkinter import *


screen = Tk()
screen.geometry("600x700")
screen.title("Formula 1 App")


titl = Label(screen, text = "Formula One", font = ("Bold", 40), fg = "Red", bg = "Black", width = 25)
titl.grid(row = 0, column = 0)

next = Label(screen, text = "Next Grand Prix :", font = ("courgette", 15))
next.place(x = 50, y = 80)

race = Label(screen, text = "Netherlands", font = ("courgette", 15), fg = "Light Blue")
race.place(x = 210, y = 80)

tim = Label(screen, text = "11:30 / 29 Aug", font = ("courgette", 15), fg = "Light Blue")
tim.place(x = 210, y = 100)

def perso():
    scr = Tk()
    scr.geometry("600x700")

personal = Button(screen, text = "Account", font =  ("courgette", 15), bg = "White", command = perso)
personal.place(x = 450, y = 80)

def sched():
    scrr = Tk()
    scrr.geometry("600x700")

schedule = Button(screen, text = "Schedule", font = ("courgette", 15), command = sched)
schedule.place(x = 150, y = 600)

def res():
    scrrr = Tk()
    scrrr.geometry("600x700")

results = Button(screen, text = "Results", font = ("courgette", 15), command = res)
results.place(x = 300, y = 600)















screen.mainloop()