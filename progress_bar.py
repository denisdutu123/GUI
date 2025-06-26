from tkinter import *
from tkinter.ttk import *
import threading

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
    time.sleep(1)
    bar["value"] = 100
    screen.update_idletasks()
    time.sleep(1)
    bar["value"] = 150
    screen.update_idletasks()
    time.sleep(1)
    bar["value"] = 200
    screen.update_idletasks()
    time.sleep(1)
    bar["value"] = 250
   

bar = Progressbar(screen,style = "custom.Horizontal.TProgressbar", orient = HORIZONTAL, length = 250, mode = "determinate")
bar.place( x = 75, y =150)

#start = Button(screen, width = 10, text = "Start", command =lambda: 
#start.place(x = 75, y  = 225)
Button(screen, text = "Start", command = lambda: threading.Thread(target = button).start()).pack(pady = 10)


screen.mainloop()
