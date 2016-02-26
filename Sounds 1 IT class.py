from tkinter import*
import tkinter as tk
import winsound
import time
import sys

limit = 15 #change this value to edit the limit of the beeps

while True:
    try:
        user = int(input('How many times do you want to play the sound? '))
    except ValueError:
        print('Please Enter a Number! ')
        continue
    if user > limit:
        print('Please input a number which is 15 or lower! ')
        continue
    else:
        break

def action1():
    for i in range(user):
        winsound.Beep(300,150)
    else:
        print('Played the sound', user, 'times.')
def action2():
    for i in range(user):
        winsound.Beep(700,400)
    else:
        print('Played the sound', user, 'times.')

window = tk.Tk()
window.title('Button Sounds')
window.minsize(400, 50)
window.lift()

button1 = tk.Button(window, text = 'Low', width = 15, height = 3, command = action1)
button2 = tk.Button(window, text = 'High', width = 15, height = 3, command = action2)

button1.pack()
button1.place(x = 70, y = 50)
button2.pack()
button2.place(x = 200, y = 50)
