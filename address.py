from tkinter import *
#from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *
import os
import ast
ke = {}


screen = Tk()
screen.geometry("600x700")
screen.title("Address Book")

#functions

def ope():
    global ke
    res()
    titl = askopenfile(title = "Files")
    if titl:
        ke = ast.literal_eval(titl.read())
        
        for i in ke.keys():
            lis.insert(END, i)
        addr.configure(text = os.path.basename(titl.name))
    else:
        messagebox.showinfo("Warning", "The address book hasn't opened")

def res():
    naent.delete(0, END)
    addent.delete(0, END)
    mobent.delete(0, END)
    emaent.delete(0, END)
    birthent.delete(0, END)
    lis.delete(0, END)
    addr.configure(text = "My Address Book")
    

def disp(event):
    global ke
    scr = Toplevel(screen)
    inde = lis.curselection()
    inf = ""
    if inde:
        key = lis.get(inde[0])
        inf = "Name:" + key + "\n"
        inff = ke[key]
        inf += "Address:" + inff[0] + "\n"
        inf +="Mobile:" + inff[1] + "\n"
        inf +="Email:" + inff[2] + "\n"
        inf +="Birthday:" + inff[3] + "\n" 
    di = Label(scr)
    di.grid(row = 0, column = 0)
    di.configure(text = inf)
    
def upd():
    key = naent.get()
    if key == "":
        messagebox.showerror("Missing information", "Please review your entries")
    else:
        if key not in ke.keys():
            lis.insert(END, key)
        ke[key] = (addent.get(), mobent.get(), birthent.get(), emaent.get())
        clea()
        
def clea():
    naent.delete(0, END)
    addent.delete(0, END)
    mobent.delete(0, END)
    birthent.delete(0, END)
    emaent.delete(0, END)

def sav():
    tex = asksaveasfile(defaultextension = ".txt")
    if tex:
        print(ke, file = tex)
        res()
    else:
        messagebox.showerror("File is not saved", "Please save ")

def edi():
    clea()
    inde = lis.curselection()
    if inde:
        naent.insert(0, lis.get(inde))
        deta = ke[naent.get()]
        addent.insert(0, deta[0])
        mobent.insert(0, deta[1])
        emaent.insert(0, deta[2])
        birthent.insert(0, deta[3])
    else:
        messagebox.showerror("Name error", "Please enter a name")

def dele():
    inde = lis.curselection()
    if inde:
        del ke[lis.get(inde)]
        lis.delete(inde)
        clea()
    else:
        messagebox.showerror("Name error", "Please enter a name")
        
        
    
    

addr = Label(screen, text = "My Address Book", font = ("courgette", 17))
addr.place(x = 50, y = 30)

open = Button(screen, text = "Open", command = ope)
open.place(x = 200, y = 30)

lis = Listbox(screen, width = 30, height = 16)
lis.place(x = 20, y = 90)
lis.bind("<<ListboxSelect>>", disp)


name = Label(screen, text = "Name:", font = ("courgette", 17))
name.place(x = 330, y = 90)

naent = Entry(screen, width = 15, font = ("courgette", 17))
naent.place(x = 400, y = 90)

addre = Label(screen, text = "Address:", font = ("courgette", 17))
addre.place(x = 315, y = 130)

addent = Entry(screen, width = 15, font = ("courgette", 17))
addent.place(x = 400, y = 130)

mobi = Label(screen, text = "Mobile:", font = ("courgette", 17))
mobi.place(x = 325, y= 170)

mobent = Entry(screen, width = 15, font = ("courgette", 17))
mobent.place(x = 400, y = 170)

email = Label(screen, text = "Email:", font = ("courgette", 17))
email.place(x = 330, y = 210)

emaent = Entry(screen, width = 15, font = ("courgette", 17))
emaent.place(x = 400, y = 210)

birthday = Label(screen, text = "Birthday:", font = ("courgette", 17))
birthday.place(x = 305, y = 250)

birthent = Entry(screen, width = 15, font = ("courgette", 17))
birthent.place(x = 400, y = 250)

edit = Button(screen, text = "Edit", font = ("courgette", 17), command = edi)
edit.place(x = 50, y = 500)

delete = Button(screen, text = "Delete", font = ("courgette", 17), command = dele)
delete.place(x = 150, y = 500)

save = Button(screen, width = 30, text = "Save", font = ("courgette", 17), command = sav)
save.place(x = 85, y = 590)

update = Button(screen, text = "Update/Add", font = ("courgette", 17), command = upd)
update.place(x = 400, y = 500)















screen.mainloop()
