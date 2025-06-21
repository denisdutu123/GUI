from tkinter import *

screen = Tk()
screen.title("Log In")
screen.geometry("900x800")
screen.config(background = "Grey")
#label
first = Label(screen, text = "Firstname:", background = "Blue", font = ("courgette", 33))
first.place(x = 200, y = 200)
second = Label(screen, text = "surname:", background = "Blue", font = ("corugette", 33))
second.place(x = 200, y = 300)
address = Label(screen, text = "Address:", background = "Blue", font = ("corugette", 33))
address.place(x = 200, y = 375)
#entry
fir = Entry(screen, background = "Blue", width = 20, font = ("courgette", 33))
fir.place(x = 425, y = 200)
sec = Entry(screen, background = "Blue", font = ("Grey", 33))
sec.place( x = 425, y = 300)
addr = Entry(screen, background = "Blue", font = ("Grey", 33))
addr.place( x = 425, y = 375)
#button
signup = Button(screen, text = "Sign up", background = "red", font = ("courgette", 33))
signup.place(x = 200, y = 500)
screen.mainloop()