from tkinter import*

screen = Tk()
screen.geometry("800x400")
screen.config(background = "Blue")
title = Label(screen, text = "Guess the number between 1 to 30", font = ("courgette", 30), background = "Blue")
title.pack(pady = (20, 0))

enter = Entry(screen, width = 15, font = ("courgette", 25))
enter.pack(pady = 40)
buttons = Frame(screen, bg = "Blue")
buttons.pack(side = BOTTOM)

accept = Button(buttons, text = "Accept", font = ("courgette", 20), bg = "Blue")
accept.pack(side = LEFT, pady = 20)

reset = Button(buttons, text = "Reset", font = ("courgette", 20), bg = "Blue")
reset.pack(side = LEFT, pady = 15)





screen.mainloop()


