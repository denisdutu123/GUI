from tkinter import *
import calendar


screen = Tk()
screen.geometry("700x600")
screen.config(background = "Red")
def conversion():
    answ = ente.get()
    if (answ.replace(".", "", 1).isdigit()):
        error.place_forget()
        con = (float(answ)* 9/5) + 32
        answer.config(text = "Temperature in fahrenheit:"+str(con))
    else:
        error.config(text = "Enter appropriate value")

convert = Label(screen, text = "Celsius -> fahrenheit", font = ("Courgette", 40), background = "blue")
convert.place(x = 150, y = 100) 
enter = Label(screen, text = "Enter temperature in celsius :", font = ("Courgette", 25), background = "blue")
enter.place(x = 120, y = 250) 
answer = Label(screen, text = "Temperature in fahrenheit:", font = ("Courgette", 19), background = "blue")
answer.place(x = 150, y = 300)
error = Label(screen, font = ("Courgette", 19), background = "red")
error.place(x = 450, y = 300)  
ente = Entry(screen, width = 15)
ente.place(x = 450, y = 260)
conv = Button(screen, text = "Convert", background = "yellow", font = ("courgette", 20), command = conversion)
conv.place(x = 300, y = 350)










screen.mainloop()