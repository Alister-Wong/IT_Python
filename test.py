from tkinter import *

root = Tk()

human = Canvas(root, height = 500, width = 500)
human.pack()

head = human.create_oval(65, 75, 140, 150, outline = "white", fill = "pink")
body = human.create_oval(55, 147, 150, 297, outline = "white", fill = "blue")
armR = human.create_oval(139, 177, 189, 193, outline = "white", fill = "blue")
