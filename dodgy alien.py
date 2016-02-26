from tkinter import *
import tkinter as tk

window = Tk()
window.title('Dodgy Alien')

Dodgy = Canvas(window, height=500, width=500)
Dodgy.pack()

body = Dodgy.create_oval(100, 150, 300, 250, outline='red', fill='green')
eyeL = Dodgy.create_oval(100, 120, 150, 170, outline='red', fill='white')
eyeR = Dodgy.create_oval(250, 120, 300, 170, outline='red', fill='white')
irisL = Dodgy.create_oval(120, 145, 130, 155, outline='green', fill='red')
irisR = Dodgy.create_oval(270, 145, 280, 155, outline='green', fill='red')
mouth = Dodgy.create_oval(150, 220, 250, 240, outline='white', fill='red')

closeb = Button(window, text = "Quit", width = 15, height = 3, command = window.destroy, anchor = W)

closeb.place(x = 10, y = 10)
while True:
    Dodgy.move(irisL, 8, 0)
    Dodgy.move(irisR, 8, 0)
    Dodgy.after(300)
    Dodgy.update()
    Dodgy.move(irisL, -8,0)
    Dodgy.move(irisR, -8,0)
    Dodgy.after(300)
    Dodgy.update()
    
def eyes_mouth(event):
    key = event.keysym
    if key == "b":
        Dodgy.itemconfig(eyeR, fill = 'green')
        Dodgy.itemconfig(irisR, state = HIDDEN)
        Dodgy.itemconfig(eyeL, fill = 'green')
        Dodgy.itemconfig(irisL, state = HIDDEN)
        Dodgy.update()
    elif key == "v":
        Dodgy.itemconfig(eyeR, fill = 'white')
        Dodgy.itemconfig(irisR, state = NORMAL)
        Dodgy.itemconfig(eyeL, fill = 'white')
        Dodgy.itemconfig(irisL, state = NORMAL)
    elif key == "m":
        Dodgy.itemconfig(mouth, fill = 'red')
    elif key == "n":
        Dodgy.itemconfig(mouth, fill = 'black')    

Dodgy.bind_all('<Key>', eyes_mouth,)


