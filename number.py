from tkinter import*
import random

screen = Tk()
screen.geometry("800x400")
screen.config(background = "Blue")
#function for check button
num = random.randint(1, 30)
atte = 0
def check():
    ent = int(enter.get())
    global atte 
    atte +=1
    if ent == num:
        result.config(text = f"Result: correct You guessed it in {atte} tries.")
    elif ent > num:
        result.config(text = "Result: guess lower")
    else:
        result.config(text = "result: guess higher")

#function for reset
def res():
    global atte, num
    num = random.randint(1, 30)
    atte = 0
    result.config(text = "results:")
    enter.delete(0, END)
title = Label(screen, text = "Guess the number between 1 to 30", font = ("courgette", 30), background = "Blue")
title.pack(pady = (20, 0))

result = Label(screen, text = "Result:", font = ("courgette", 30), background = "Blue")
result.pack(pady = (20, 0), padx = (0, 20))

enter = Entry(screen, width = 15, font = ("courgette", 25))
enter.pack(pady = 40)
buttons = Frame(screen, bg = "Blue")
buttons.pack(side = BOTTOM)

accept = Button(buttons, text = "Accept", font = ("courgette", 20), bg = "Blue", command = check)
accept.pack(side = LEFT, pady = 20)

reset = Button(buttons, text = "Reset", font = ("courgette", 20), bg = "Blue", command = res)
reset.pack(side = LEFT, pady = 15)





screen.mainloop()
