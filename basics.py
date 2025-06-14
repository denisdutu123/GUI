from tkinter import *

screen = Tk()
screen.geometry("700x600")
#background color
screen.config(background = "Green")
butt = Button(screen, background = "Blue", text = "Press", command = screen.destroy)
# positioning the button
butt.pack()
screen.mainloop()

