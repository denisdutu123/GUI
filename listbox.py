from tkinter import*



screen = Tk()
screen.geometry("700x150")
screen.title("List box")

title = Label(screen, text = "shopping list", font = ("courgette", 20))
title.pack()

scroll = Scrollbar(screen)
scroll.pack(side = RIGHT, fill = Y)

list = Listbox(screen, height = 50, width = 20, activestyle = "dotbox", font = ("courgette", 15), fg = "Green", yscrollcommand = scroll.set)

list.insert(1, "Bread")
list.insert(2, "Flour")
list.insert(3, "Ham")
list.insert(4, "Pizza")
list.insert(5, "Bread")
list.insert(6, "Flour")
list.insert(7, "Ham")
list.insert(8, "Pizza")
list.pack()
scroll.config(command = list.yview)





screen.mainloop()