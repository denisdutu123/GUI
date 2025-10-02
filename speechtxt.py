from tkinter import *
from tkinter import messagebox
import speech_recognition as sr
from tkinter import filedialog

screen = Tk()
screen.geometry("700x500")
screen.title("speech to text")

def click():
    recogn = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speaking recognition started")
        aud = recogn.listen(source)
        try:
            text = recogn.recognize_google(aud)
        except:
            text = "You are currently not speaking"
        output.delete(1.0, END)
        output.insert(END, text)

def sav():
    sa = filedialog.asksaveasfile(defaultextension = ".txt")
    if sa:
        sa.write(output.get(1.0, END))
        sa.close()
    else:
        messagebox.showerror("Warning message", "text not saved")

main = Label(screen, text = "Voice Notepad", font = ("courgette", 25), bg = "Blue")
main.place(x = 250, y = 60)

clickonme = Button(screen, text = "Click on me!\n To start recording", font = ("courgette", 20), command = click)
clickonme.place(x = 20, y = 200)

output = Text(screen, width = 20, height = 3, font = ("courgette", 20))
output.place(x = 250, y = 200)

save = Button(screen, text = "save the text", font = ("courgette", 20), command = sav)
save.place(x = 530, y = 220)

  













screen.mainloop()
