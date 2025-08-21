from tkinter import *
from tkinter.ttk import *

screen = Tk()
screen.title("maths")

def generate():
    
    s1 = ""
    for i in range(1, numb1.get() +1):
        s1 += str(value.get())+"X"+str(i)+ " = " + str(value.get()*i)+"\n"
    display.config(text = s1)
        
        
        
        
    



display = Label(screen)
display.grid(row = 4, column = 0)

mt = Label(screen, text = "Mathematical Table")
mt.grid(row = 0, column = 0, padx = (10, 10), columnspan = 3)

stor = Button(screen, text = "generate", command = generate)
stor.grid(row = 2, column = 0)

nr = Label(screen, text = "Number and Range:")
nr.grid(row = 1, column = 0)

value = IntVar()
num = Combobox(screen, textvariable = value, width = 3)
num["values" ] = tuple(range(50))
num.grid(row = 1, column = 1)

numb1 = IntVar()
numb2 = Radiobutton(screen, text = "10", variable = numb1, value = 10)
numb3 =  Radiobutton(screen, text = "20", variable = numb1, value = 20)
numb4 =  Radiobutton(screen, text = "30", variable = numb1, value = 30)
numb1.set(10)
numb2.grid(row = 1, column = 2)
numb3.grid(row = 2, column = 2)
numb4.grid(row = 3, column = 2)







screen.mainloop()
