from tkinter import*

screen = Tk()

def conversion():
    weight = float(wei.get())
    gra = weight * 1000
    pou = weight * 2.2
    ounc = weight * 35.274
    t1.delete("1.0", END)
    t1.insert(END, gra)
    t2.delete("1.0", END)
    t2.insert(END, pou)
    t3.delete("1.0", END)
    t3.insert(END, ounc)

l1 = Label(screen, text = "Enter the weight in kg:", font = ("courgette", 30))
l2 = Label(screen, text = "gram",font = ("courgette", 20))
l3 = Label(screen, text = "pounds",font = ("courgette", 20))
l4 = Label(screen, text = "ounces",font = ("courgette", 20))
wei = StringVar()
entry = Entry(screen, textvariable = wei, width = 30, font = 40)
convert = Button(screen, text = "Convert", command = conversion)
t1 = Text(screen, height = 1, width = 25)
t2 = Text(screen, height = 1, width = 25)
t3 = Text(screen, height = 1, width = 25)

#griding method
l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)
l3.grid(row = 1, column = 1)
l4.grid(row = 1, column = 2)
entry.grid(row = 0, column = 1)
convert.grid(row = 0, column = 2)
t1.grid(row = 2, column = 0)
t2.grid(row = 2, column = 1)
t3.grid(row = 2, column = 2)

screen.mainloop()
