from tkinter import *


screen = Tk()
screen.geometry("600x700")
screen.title("Formula 1 App")


titl = Label(screen, text = "Formula One", font = ("Bold", 40), fg = "Red", bg = "Black", width = 25)
titl.grid(row = 0, column = 0)

next = Label(screen, text = "Next Grand Prix :", font = ("courgette", 15))
next.place(x = 50, y = 80)

new = Label(screen, font = ("courgette", 20), bg = "Grey", width = 38, height = 17)
new.place(x = 50, y = 160)

news = Label(screen, text = "Top News", font = ("courgette", 20), fg = "Yellow")
news.place(x = 235, y = 160)

box1 = Label(screen, width = 55, height = 5 , bg = "Dark Grey")
box1.place(x = 50, y = 200)

tex1 = Label(screen, text = "26 Aug : Cadillac sign Valtteri Bottas and Sergio Perez as there 2026 drivers", font = ("courgette", 14))
tex1.place(x = 50, y = 220)

box2 = Label(screen, width = 55, height = 5 , bg = "Dark Grey")
box2.place(x = 50, y = 320)

tex2 = Label(screen, text = "24 Aug: Cadillac and Audi are to be making their debut to Formula 1 in the \n 2026 season", font = ("courgette", 14))
tex2.place(x = 50, y = 340)

box3 = Label(screen, width = 55, height = 5 , bg = "Dark Grey")
box3.place(x = 50, y = 440)

tex3 = Label(screen, text = "23 Aug: George Russel's new Mercedes contract will be confirmed 'When \n the time is right'", font = ("courgette", 14))
tex3.place(x = 50, y = 460)

race = Label(screen, text = "Netherlands", font = ("courgette", 15), fg = "Light Blue")
race.place(x = 210, y = 80)

tim = Label(screen, text = "11:30 / 29 Aug", font = ("courgette", 15), fg = "Light Blue")
tim.place(x = 210, y = 100)

def perso():
    scr = Toplevel(screen)
    scr.geometry("600x700")
    
    
    def detail():
        use = ema.get()
        pas = passw.get()
        tea = str(team.get())
        file = open("formula.txt", 'a')
        file.write(f"Username:{use}, password: {pas}, favourite team: {tea} \n")
        ema.delete(0, END)
        passw.delete(0, END)
    
    email = Label(scr, text = "Enter Email:", font = ("courgette", 20))
    email.place(x = 50, y = 70)
    ema = Entry(scr, width = 25, font = ("courgette", 20))
    ema.place(x = 170, y = 70)
    password = Label(scr, text = "Enter Password:", font = ("courgette", 20))
    password.place(x = 50, y = 110)
    passw = Entry(scr, width = 20, font = ("courgette", 20))
    passw.place(x = 200, y = 110)
    save = Button(scr, text = "Save information", font = ("courgette", 20), command = detail)
    save.place(x = 50, y = 500)
    titl1 = Label(scr, text = "Formula One", font = ("Bold", 40), fg = "Red", bg = "Black", width = 25)
    titl1.grid(row = 0, column = 0)
    follow = Label(scr, text = "Follow your favourite team:", font = ("courgette", 20))
    follow.place(x = 50, y = 180)
    team = StringVar()
    team1 = Radiobutton(scr, text = "McLaren", textvariable = team, value = "McLaren")
    team2 =  Radiobutton(scr, text = "Ferrari", textvariable = team, value = "Ferrari")
    team3 =  Radiobutton(scr, text = "Red Bull Racing", textvariable = team, value = "Red Bull racing")
    team4 =  Radiobutton(scr, text = "Aston Martin", textvariable = team, value = "Aston Martin")
    team5 =  Radiobutton(scr, text = "Haas", textvariable = team, value = "Haas")
    team6 =  Radiobutton(scr, text = "Mercedes", textvariable = team, value = "Mercedes")
    team7 =  Radiobutton(scr, text = "Williams", textvariable = team, value = "Williams")
    team8 =  Radiobutton(scr, text = "Kick Sauber", textvariable = team, value = "kick Sauber")
    team9 =  Radiobutton(scr, text = "Racing Bulls", textvariable = team, value = "Racing Bulls")
    team10 =  Radiobutton(scr, text = "Alpine", textvariable = team, value = "Alpine")
    team.set("McLaren")
    team1.place(x = 50, y = 220)
    team2.place(x = 50, y = 240)
    team3.place(x = 50, y = 260)
    team4.place(x = 50, y = 280)
    team5.place(x = 50, y = 300)
    team6.place(x = 50, y = 320)
    team7.place(x = 50, y = 340)
    team8.place(x = 50, y = 360)
    team9.place(x = 50, y = 380)
    team10.place(x = 50, y = 400)

personal = Button(screen, text = "Account", font =  ("courgette", 15), bg = "White", command = perso)
personal.place(x = 450, y = 80)

def sched():
    scrr = Toplevel(screen)
    scrr.geometry("600x700")
    canvas = Canvas(scrr, width = 550, height = 620)
    canvas.pack(side = LEFT, fill = BOTH, expand = True)
    scroll = Scrollbar(scrr, orient = "vertical", command = canvas.yview)
    scroll.pack(side = RIGHT, fill = Y)
    canvas.configure(yscrollcommand = scroll.set)
    fra = Frame(canvas, bg = "Black")
    canvas.create_window((0, 0), window=fra, anchor="nw")
    fra.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    til1 = Label(fra, text = "Formula One", font = ("Bold", 40), fg = "Red", bg = "Black", width = 25)
    til1.place(x = 300, y = 20)
    
    
    ra1 = Label(fra, text = "Australia Grand Prix: 14 Mar / Practice 1 \n 14 Mar / Practice 2 \n 15 Mar / Practice 3 \n 15 Mar / Qualifying \n 16 Mar / Race", font = ("courgette", 9), bg = "Dark Grey")
    ra1.place(x = 20, y = 55)
    ra2 = Label(fra, text = "China Grand Prix: 21 Mar / Practice 1 \n 21 Mar / Sprint Qualifying \n 22 Mar / Sprint \n 22 Mar / Qualifying \n 23 Mar / Race", font = ("courgette", 9), bg = "Dark Grey")
    ra2.place(x = 20, y = 120)
    ra3 = Label(fra, text = "Japan Grand Prix: 04 Apr / Practice 1 \n 04 Apr / Practice 2 \n 05 Apr / Practice 3 \n 05 Apr/ Qualifying \n 06 Apr / Race", font = ("courgette", 9), bg = "Dark Grey")
    ra3.place(x = 20, y = 185)
    ra4 = Label(fra, text = "Bahrain Grand Prix: 11 Apr / Practice 1 \n 11 Apr / Practice 2 \n 12 Apr / Practice 3 \n 12 Apr/ Qualifying \n 13 Apr / Race", font = ("courgette", 9), bg = "Dark Grey")
    ra4.place(x = 20, y = 250)
    ra5 = Label(fra, text = "Saudi Arabia Grand Prix: 18 Apr / Practice 1 \n 18 Apr / Practice 2 \n 19 Apr / Practice 3 \n 19 Apr/ Qualifying \n 20 Apr / Race", font = ("courgette", 9), bg = "Dark Grey")
    ra5.place(x = 20, y = 315)
    ra6 = Label(fra, text = "Miami Grand Prix: 02 May / Practice 1 \n 02 May / Sprint Qualifying \n 03 May / Sprint \n 03 May/ Qualifying \n 04 May / Race", font = ("courgette", 9), bg = "Dark Grey")
    ra6.place(x = 20, y = 380)
    ra7 = Label(fra, text = "Emilia-Romagna Grand Prix: 16 May / Practice 1 \n 16 May / Practice 2 \n 17 May / Practice 3 \n 17 May/ Qualifying \n 18 May / Race", font = ("courgette", 9), bg = "Dark Grey")
    ra7.place(x = 20, y = 445)
    #scroll.config(command = )
    #fra.pack(side = RIGHT)
    

schedule = Button(screen, text = "Schedule", font = ("courgette", 15), command = sched)
schedule.place(x = 150, y = 600)

def res():
    scrrr = Toplevel(screen)
    scrrr.geometry("600x700")

results = Button(screen, text = "Results", font = ("courgette", 15), command = res)
results.place(x = 300, y = 600)













screen.mainloop()
