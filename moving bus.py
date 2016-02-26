import tkinter as tk

win = tk.Tk()
win.title("Moving Bus")
win.minsize(800, 400)

bus = tk.Canvas(win, height = 600, width = 1200)
bus.pack()

main = bus.create_rectangle(35, 150, 400, 300, fill = "red")
wheelL = bus.create_oval(70, 275, 130, 335, outline = "black", fill = "black")
wheelR = bus.create_oval(305, 275, 365, 335, outline = "black", fill = "black")

personbody = bus.create_polygon(475, 275, 560, 275, 520, 180, outline = "black", fill = "green")
personhead = bus.create_oval(500, 160, 540, 200, fill = "white")
personlegL = bus.create_line(490, 275, 490, 295)
personlegR = bus.create_line(545, 275, 545, 295)
personfootL = bus.create_line(490, 295, 480, 295)
personfootL = bus.create_line(545, 295, 555, 295)


for i in range(1, 75):
    bus.move(main, 2, 0)
    bus.move(wheelL, 2, 0)
    bus.move(wheelR, 2, 0)
    bus.after(100)
    bus.update()
