from tkinter import*

screen = Tk()
screen.geometry("700x300")

title = Label(screen, text = "Cars", font = ("courgette", 30))
title.pack()

horiz = Frame(screen)
horiz.pack()
vert = Frame(screen)
vert.pack(side = BOTTOM)

car1 = Button(horiz, text = "Ferrari", fg = "Red", bg = "White", font = ("courgette", 20))
car1.pack(side = LEFT)
car2 = Button(horiz, text = "BMW", fg = "Blue", bg = "White", font = ("courgette", 20))
car2.pack(side = LEFT)
car3 = Button(horiz, text = "McLaren", fg = "Orange", bg = "White", font = ("courgette", 20))
car3.pack(side = LEFT)
car4 = Button(vert, text = "Lamborghini", fg = "Yellow", bg = "White", font = ("courgette", 20))
car4.pack(side = BOTTOM, pady = 10)
car5 = Button(vert, text = "Aston Martin", fg = "Green", bg = "White", font = ("courgette", 20))
car5.pack(side = BOTTOM, pady = 10)
car6 = Button(vert, text = "Mercedes", fg = "Grey", bg = "White", font = ("courgette", 20))
car6.pack(side = BOTTOM, pady = 10)









screen.mainloop()