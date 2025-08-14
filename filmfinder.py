from tkinter import *

screen = Tk()
screen.config(background = "Black")
screen.geometry("500x300")
screen.title("film finder")


main = Label(screen, text = " TOP 50 trending series/ movies", font = ("courgette", 15), bg = "Black", fg = "Red")
main.pack()

add = Button(screen, text = "Add", font = ("courgette", 15), bg = "Black", fg = "Red")
add.pack(side = RIGHT, padx = 5, pady = 5)

ent = Entry(screen, width = 20)
ent.pack(padx = 5, pady = 5)

open = Button(screen, text = "Open", font = ("courgette", 15), bg = "Black", fg = "Red")
open.pack( padx = 5, pady = 5)

verti = Frame(screen)
scroll = Scrollbar(verti, orient = "vertical")
scroll.pack(side = RIGHT, fill = Y)
list = Listbox(verti, width = 60, yscrollcommand = scroll.set, bg = "Grey")

for i in range(1, 50):
    list.insert(END, "Movie/series" + str(i))
list.pack(side = LEFT, padx = 5)
scroll.config(command = list.yview)
verti.pack(side = RIGHT, padx = 5)


screen.mainloop()