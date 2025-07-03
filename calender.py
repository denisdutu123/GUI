from tkinter import *
import calendar
#from tkinter.ttk import *

screen = Tk()
screen.geometry("250x200")
screen.config(background = "Red")
#style= ttk.Style()
#style.theme_use('default')

#function for calender
def calende():
    scr = Tk()
    scr.geometry("490x575")
    scr.config(background = "Grey")
    yea = int(cale.get())
    ca = calendar.calendar(yea)
    calen = Label(scr, text = ca, font = "Consolas 13 bold")
    calen.grid(row = 5, column = 1, padx = 20)
    scr.mainloop()
    

#labels
cal = Label(screen, text = "Calender", font = ("Courgette", 40), background = "blue")
cal.place(x = 40, y = 5)
year = Label(screen, text = "Enter Year", font = ("Courgette", 20), background = "orange")
year.place(x = 65, y = 60)
#entry
cale = Entry(screen, width = 15)
cale.place(x = 50, y = 90 )
#button
calend = Button(screen, text = "Show Calender", background = "yellow", font = ("courgette", 20), command = calende)
calend.place(x = 50, y = 120)
exit = Button(screen, text = "Exit", font = ("courgette", 20))
exit.place(x = 80, y = 160)





screen.mainloop()
