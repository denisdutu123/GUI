from tkinter import *
from tkinter.ttk import *

screen = Tk()
screen.geometry("400x300")
screen.title("Progess Bar")
style = Style()
style.theme_use("default")
style.configure("custom.Horizontal.TPorgressbar", thickness = 30)
#progress bar

def button():
    import time
    bar["value"] = 50
    screen.update_idletasks()
    time.sleep(2)
    bar["value"] = 100
    screen.update_idletasks()
    time.sleep(2)
    bar["value"] = 150
    screen.update_idletasks()
    time.sleep(2)
    bar["value"] = 200
    screen.update_idletasks()
    time.sleep(2)
    bar["value"] = 250
   

bar = Progressbar(screen,style = "custom.Horizontal.TProgressbar", orient = HORIZONTAL, length = 250, mode = "determinate")
bar.place( x = 75, y =150)

start = Button(screen, width = 10, text = "Start", command = button)
start.place(x = 75, y  = 225)


screen.mainloop()