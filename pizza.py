from tkinter import *
from tkinter.ttk import*

screen = Tk()
screen.geometry("500x250")
screen.title("Pizza Hut")
def orde():
    pizz = piz.get()
    choi = str(cho.get())
    ty = str(typ.get())
    output.config(text = f"You've ordered,{ty}, {choi}, {pizz}, pizzas") 
    


output = Label(screen)
output.grid(row = 5, column = 1)

ti = Label(screen, text = " Welcome To Pizza Hut")
ti.grid(row = 0, column = 1)

sele = Label(screen, text = "Select your favourite pizza")
sele.grid(row = 1, column = 0)

ent = Label(screen, text = "Enter quantity:")
ent.grid(row = 2, column = 0)

ord = Button(screen, text = "order", command = orde)
ord.grid(row = 4, column = 1)

piz = Combobox(screen)
piz["values"] = ("Pepproni", "chicken", "Mexican style", "vegan")
piz.grid(row = 1, column = 1)
piz.current(0)

typ = IntVar()
wor = Combobox(screen, textvariable = typ)
wor["values" ] = tuple(range(10))
wor.grid(row = 2, column = 1)

cho = StringVar()
cho1 = Radiobutton(screen, text = "s", variable = cho, value = "s")
cho1.grid(row = 1, column = 3)
cho2 = Radiobutton(screen, text = "m", variable = cho, value = "m")
cho2.grid(row = 2, column = 3)
cho3 = Radiobutton(screen, text = "l", variable = cho, value = "l")
cho3.grid(row = 3, column = 3)









screen.mainloop()