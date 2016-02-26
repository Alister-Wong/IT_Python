from tkinter import *
import tkinter as tk

window = Tk()
window.title('Dungeon Explorer!')
window.minsize(400, 100)

doorV = StringVar()
lives = 2
counter = -1
def okcount():
    global counter
    counter +=1/2
    counting.config(text = str(counter))
    return(counter)

counting = Label()
counting.pack()


def firstdoor():
        
    doorIN = doorV.get()

    if doorIN == "1" and okcount() != 1 and okcount() < 2:
        door1 = Label(window, text = "You slipped on the slippery surface, -1 life, now three more doors appear before you.").pack()

        
        
        if okcount() > 1 and okcount() < 4:
            error1 = Label(window, text = "ERROR: First door has been chosen already!").pack()

    elif doorIN == "2" and okcount() != 1 and okcount() < 2:
        door2 = Label(window, text = "Nothing happened, but you now see 3 more doors.").pack()

        if okcount() > 1 and okcount() < 4:
            error1 = Label(window, text = "ERROR: First door has been chosen already!").pack()

            def seconddoor2():

                doorV22= StringVar()
                counter22 = 0
                def okcount22():
                    global counter22
                    counter22 += 1/2
                    counting22.config(text = str(counter22))
                    return(counter22)

                counting22 = Label()     
                counting22.pack()
                
                doorIN22 = doorV22.get()
                
                if doorIN22 == "1":
                    door1 = Label(window, text = doorIN).pack()
                elif doorIN22 == "2":
                    door2 = Label(window, text = "").pack()
                    if okcount22() > 1 and okcount22() < 4:
                        error1 = Label(window, text = "ERROR: First door has been chosen already!").pack()
                elif doorIN22 == "3":
                    door3 = Label(window, text = "You found a safe way through and found a piece of rope!").pack()
                    if okcount22() > 1 and okcount22() < 4:
                        error1 = Label(window, text = "ERROR: First door has been chosen already!").pack()
                elif okcount22() > 1 and okcount22() < 4:
                    error1 = Label(window, text = "ERROR: First door has been chosen already!").pack()
            
        def seconddoor_ok(evt = None):
            okcount22()
            seconddoor2()
        
        door = Label(window, text = "Which Door do you pick?")
        door.pack()

        doorV22 = StringVar()
        doorE22 = Entry(window, textvariable = doorV)
        doorE22.pack()

        ok21 = Button(window, text = "OK", command = seconddoor_ok, width = 5, height = 1).pack()

    elif doorIN == "3" and okcount() != 1 and okcount() < 4:
        door3 = Label(window, text = "").pack()
        death = Tk()
        death.title("RIP")
        window.destroy()
        
        deathmsg = Label(death, text = "The ground beneath you disappeared! IT BURNS! IT'S LAVA").pack()
        deathmsg31 = Label(death, text = "You burnt to death. :(").pack()
        deathmsgok = Button(death, text = "OK", command = death.destroy).pack()
        
        if okcount() > 1:
            error1 = Label(window, text = "ERROR: First door has been chosen already!").pack()

    elif okcount() > 1 and okcount() < 4:
        error1 = Label(window, text = "ERROR: First door has been chosen already!").pack()
def firstdoor_ok(evt = None):
    okcount()
    firstdoor()

welcome = Label(window, text = "Welcome to Dungeon Explorer!")
welcome.pack()


door = Label(window, text = "Which Door do you pick?")
door.pack()

doorV = StringVar()
doorE = Entry(window, textvariable = doorV)
doorE.pack()

ok = Button(window, text = "OK", command = firstdoor_ok, width = 5, height = 1).pack()

window.mainloop()
