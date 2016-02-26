from tkinter import *

lives = 2

window = Tk()
window.title('Dungeon Explorer!')
window.minsize(400, 100)

def firstdoor():  
    doorIN = doorV.get()

    if doorIN == "1":
        door1 = Label(window, text = "").pack()

        window.destroy()
        window21 = Tk()
        window21.title('Dungeon Explorer!')
        window21.minsize(400, 100)

        door21msg = Label(window21, text = "You slipped on the slippery surface, -1 life, now three more doors appear before you.").pack()

        doorV21 = StringVar()
        door21 = Label(window21, text = "Which Door do you pick?")
        door21.pack()
        doorE21 = Entry(window21, textvariable = doorV21, bd = 5)
        doorE21.pack()

        ok21 = Button(window21, text = "OK", bd = 5, command = seconddoor21, width = 5, height = 1,).pack()


    elif doorIN == "2":
        door2 = Label(window, text = "").pack()
        
        window.destroy()
        window22 = Tk()
        window22.title('Dungeon Explorer!')
        window22.minsize(400, 100)


        def seconddoor22():

            doorV22 = StringVar()

            doorIN22 = doorV22.get()

            if doorIN22 == "1":
                door122 = Label(window22, text = doorIN).pack()
            elif doorIN22 == "2":
                door222 = Lrabel(window22, text = "test").pack()
            elif doorIN22 == "3":
                door322 = Label(window22, text = "You found a safe way through and found a piece of rope!").pack()
            else:
                number1to322 = Tk()
                number1to322.title("ERROR")
                number1to322.minsize(200, 50)

                number1to3msg22 = Label(number1to322, text = "Please Enter a number between 1 and 3").pack()
                number1to3B22 = Button(number1to322, bd = 5, height = 1, width = 10, command = number1to322.destroy, text = "OK",).pack()
                number1to322.after(3000, number1to322.destroy)
           
        door22msg = Label(window22, text = "Nothing happened, but you now see 3 more doors.").pack()

        doorV22 = StringVar()
        door22 = Label(window22, text = "Which Door do you pick?")
        door22.pack()
        doorE22 = Entry(window22, textvariable = doorV22, bd = 5)
        doorE22.pack()

        ok22 = Button(window22, text = "OK", bd = 5, command = seconddoor22, width = 5, height = 1).pack()

        window22.mainloop()
    elif doorIN == "3":
        door3 = Label(window, text = "").pack()
        global death
        death = Tk()
        death.title("RIP")
        window.destroy()
        
        deathmsg = Label(death, text = "The ground beneath you disappeared! IT BURNS! IT'S LAVA").pack()
        deathmsg31 = Label(death, text = "You burnt to death. :(").pack()
        deathmsgok = Button(death, bd = 5, text = "OK", command = death.destroy).pack()
    else:
        number1to3 = Tk()
        number1to3.title("ERROR")
        number1to3.minsize(200, 50)

        number1to3msg = Label(number1to3, text = "Please Enter a number between 1 and 3").pack()
        number1to3B = Button(number1to3, height = 1, width = 10, bd = 5, command = number1to3.destroy, text = "OK",).pack()
        number1to3.after(3000, number1to3.destroy)
def seconddoor21():
    doorV22 = StringVar()

    doorIN22 = doorV22.get()
    
    if doorIN22 == "1":
        door1 = Label(window22, text = doorIN).pack()
    elif doorIN22 == "2":
        door2 = Label(window22, text = "").pack()
    elif doorIN22 == "3":
        door3 = Label(window22, text = "You found a safe way through and found a piece of rope!").pack()

doorV = StringVar()
welcome = Label(window, text = "Welcome to Dungeon Explorer!")
welcome.pack()

door = Label(window, text = "Which Door do you pick?")
door.pack()

doorV = StringVar()
doorE = Entry(window, textvariable = doorV, bd = 5)
doorE.pack()

ok = Button(window, text = "OK", command = firstdoor, width = 5, height = 1, bd = 5).pack()
