from tkinter import *
import time
from tkinter import messagebox

screen = Tk()
screen.geometry("400x400")
screen.title("Timer")
hou = StringVar()
hou.set("00")

hour = Entry(screen, width = 2, bg = "White", fg = "Black", font = ("courgette", 25), textvariable = hou)
hour.place(x = 100, y = 90)

minu = StringVar()
minu.set("00")

minute = Entry(screen, width = 2, bg = "White", fg = "Black", font = ("courgette", 25), textvariable = minu)
minute.place(x = 150, y = 90)

sec = StringVar()
sec.set("00")

second = Entry(screen, width = 2, bg = "White", fg = "Black", font = ("courgette", 25), textvariable = sec)
second.place(x = 200, y = 90)

def timer():
    global hou, minu, sec
    numsec = int(hou.get()) * 3600 + int(minu.get()) * 60 + int(sec.get())
    while numsec > -1:
        minut, se = divmod(numsec, 60)
        ho = 0
        if minut > 60:
            ho, minut = divmod(minut, 60)
        hou.set("{00:2d}".format(ho))
        minu.set("{00:2d}".format(minut))
        sec.set("{00:2d}".format(se))
        screen.update()
        time.sleep(1)
        numsec -=1        
    

set = Button(screen, text = "Set Time Countdown", font = ("courgette", 25), command = timer)
set.place(x = 75, y = 225)








screen.mainloop()

