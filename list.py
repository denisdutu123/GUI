from tkinter import *

screen = Tk()
#screen.geometry("800x400")

save = Button(screen, text = "Save", font = ("courgette", 15))
save.pack(side = LEFT, padx = 5, pady = 5)



add = Button(screen, text = "Add", font = ("courgette", 15))
add.pack(side = RIGHT, padx = 5, pady = 5)

open = Button(screen, text = "Open", font = ("courgette", 15))
open.pack( padx = 5, pady = 5)

delete = Button(screen, text = "Delete", font = ("courgeette", 15))
delete.pack(padx = 5, pady = 5)

ent = Entry(screen, width = 20)
ent.pack(padx = 5, pady = 5)

verti = Frame(screen)
scroll = Scrollbar(verti, orient = "vertical")
scroll.pack(side = RIGHT, fill = Y)
list = Listbox(verti, width = 60, yscrollcommand = scroll.set, bg = "orange")

for i in range(1, 50):
    list.insert(END, "Item" + str(i))
list.pack(side = LEFT, padx = 5)
scroll.config(command = list.yview)
verti.pack(side = RIGHT, padx = 5)












screen.mainloop()
