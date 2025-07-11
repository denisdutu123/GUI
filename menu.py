from tkinter import *
from tkinter.ttk import*

screen = Tk()
screen.title("Main Menu")
men = Menu(screen)
files = Menu(men, tearoff = 0)
men.add_cascade(label = "file", menu = files)
files.add_command(label = "new file", command = None)
files.add_command(label = "open folder", command = None)
files.add_separator()
files.add_command(label = "close folder", command = None)
files.add_command(label = "open recent", command = None)

edit = Menu(men, tearoff = 0)
men.add_cascade(label = "edit", menu = edit)
edit.add_command(label = "cut", command = None)
edit.add_command(label = "copy", command = None)
edit.add_separator()
edit.add_command(label = "paste", command = None)
edit.add_command(label = "replace", command = None)

help = Menu(men, tearoff = 0)
men.add_cascade(label = "help", menu = help)
help.add_command(label = "new file", command = None)
help.add_command(label = "open folder", command = None)
help.add_separator()
help.add_command(label = "close folder", command = None)
help.add_command(label = "open recent", command = None)
screen.config(menu = men)
mainloop()
