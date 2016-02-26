from tkinter import *
from time import sleep

restart = 0
gold = 0 #set amount of default gold (RECOMMENDED = 0)
lives = 5 #set amount of lives (RECOMMENDED = 5)
restart = 0 #DO NOT CHANGE

def everypath():
    global gold
    global lives
    global restart
    gold = 0 #set amount of default gold (RECOMMENDED = 0)
    lives = 5 #set amount of lives (RECOMMENDED = 5)
    restart = 0 #DO NOT CHANGE

    if restart == 0:
        window = Tk()
        window.title('Dungeon Explorer!')
        window.minsize(400, 100)
        def paths():
            pathIN = pathV.get()
            global lives
            global gold
            global number1to3var
            if pathIN == "1":

                window.destroy()
                window1 = Tk()
                window1.title('Dungeon Explorer!')
                window1.minsize(400, 100)
                def firstpath():
                    pathIN1 = pathV1.get()
                    global lives
                    global gold
                    if lives == 0:
                        window.destroy()
                    elif pathIN1 == "1":
                        path1 = Label(window1, text = "test1")
                    elif pathIN1 == "2":
                        window1.destroy()
                        window12 = Tk()
                        window12.title("Dungeon Explorer!")
                        window12.minsize(400, 100)

                        def firstpath2():
                            path121msg = Label(window121, text = "")

                        path12msg = Label(window12, text = "You have %s live(s)." % (lives), fg = "red").pack()
                        path12msg = Label(window12, text ="You head back the way you came from...").pack()
                        path12msg = Label(window12, text = "Or atleast thats where you thought you were going.").pack()
                        path12msg = Label(window12, text = "It seems to be an endless journey back to your origin").pack()
                        path12msg = Label(window12, text = "Doubt begins to cloud your mind and you find yourself lost.").pack()
                        path12msg = Label(window12, text = "").pack()

                        pathV12 = StringVar()
                        pathE12 = Entry(window12, textvariable = pathV12, bd = 5)
                        pathE12.pack()

                        ok12 = Button(window12, text ="OK", command = firstpath2, width = 10, height = 1, bd = 5).pack()
                    elif pathIN1 == "3":
                        window1.destroy()
                        window13 = Tk()
                        window13.title("Dungeon Explorer!")
                        window13.minsize(400, 100)
                        def firstpath3():
                            pathIN13 = pathV13.get()
                            global lives
                            global gold
                            if pathIN13 == "1":
                                window13.destroy()
                                window131 = Tk()
                                window131.title("Dungeon Explorer!")
                                window131.minsize(400, 100)

                                path131msg = Label(window131, text = "You have %s live(s)." % (lives), fg = "red").pack()
                                path131msg = Label(window131, text = "As you near the figure, recognisable features are appearing.").pack()
                                path131msg = Label(window131, text = "To your suprise, it was actually a goblin!").pack()
                                path131msg = Label(window131, text = "You prepare for battle, as the goblin notices you").pack()
                                path131msg = Label(window131, text = '"Hey, you new?" The goblin replied, as he saw you').pack()
                                path131msg = Label(window131, text = "You question his reply, only to find out that you and him are of the same kind.").pack()
                                path131msg = Label(window131, text = "You lose all your aggression and decide to team up with him.").pack()
                                path131msg = Label(window131, text = "He begins to follow you as he was lost himself.").pack()
                                path131msg = Label(window131, text = "You have gained yourself a companion!").pack()

                                pathV131 = StringVar()
                                pathE131 = Entry(window131, textvariable = pathV13, bd = 5)
                                pathE13.pack()

                                ok131 = Button(window131, text = "OK", command = firstpath3, width = 5, height = 1, bd = 5).pack()

                        path13msg = Label(window13, text = "After walking for what seems like an endless hike, a shadow is emerging.").pack()
                        path13msg = Label(window13, text = "As you get closer towards the shadow, it seems to be getting larger.").pack()
                        path13msg = Label(window13, text = "Now that you get a closer look, it has a humanoid look to it.").pack()
                        path13 = Label(window13, text = "Do you 1) Run for the shadow 2) Try to sneak past it and ignore the figure.", fg = "blue").pack()

                        pathV13 = StringVar()
                        pathE13 = Entry(window13, textvariable = pathV13, bd = 5)
                        pathE13.pack()

                        ok13 = Button(window13, text = "OK", command = firstpath3, width = 5, height = 1, bd = 5).pack()
                    else:
                        number1to31 = Tk()
                        number1to31.title("ERROR")
                        number1to31.minsize(200, 50)

                        number1to31msg = Label(number1to31, text = "Please Enter a number between 1 and 3").pack()
                        number1to31B = Button(number1to31, bd = 5, height = 1, width = 10, command = number1to3a1.destroy, text = "OK",).pack()
                        number1to31.after(3000, number1to31.destroy)

                path1msg = Label(window1, text = "You have %s live(s)." % (lives), fg = "red").pack()
                path1msg = Label(window1, text = "There is now a clearing, but the whole place is filled with a huge fog.").pack()
                path1msg = Label(window1, text = "After walking forward some more, you realise the floor is quite odd.").pack()
                path1msg = Label(window1, text = "You slipped on the ice, -1 life。").pack()
                lives = lives - 1
                path1msg = Label(window1, text = "You have %s lives remaining" % (lives), fg = "red").pack()

                pathV1 = StringVar()
                path1 = Label(window1, text = "Do you wish to 1) Push forward regardless 2) Turn back", fg = "blue").pack()
                path1 = Label(window1, text = " 3) Move to your right and hope for the best.", fg = "blue").pack()
                pathE1 = Entry(window1, textvariable = pathV1, bd = 5)
                pathE1.pack()

                ok1 = Button(window1, text = "OK", bd = 5, command = firstpath, width = 5, height = 1,).pack()


            elif pathIN == "2":

                window.destroy()
                window2 = Tk()
                window2.title('Dungeon Explorer!')
                window2.minsize(400, 100)


                def secondpath():
                    pathIN2 = pathV2.get()
                    global lives
                    global gold

                    if pathIN2 == "1":
                        window2.destroy()
                        window21 = Tk()
                        window21.title('Dungeon Explorer!')
                        window21.minsize(400, 100)

                        def secondpath1():
                            pathIN21 = pathV21.get()
                            global lives
                            global gold

                        path21msg = Label(window21, text = "You have %s live(s)." % (lives), fg = "red").pack()
                        path21msg = Label(window21, text = "A treasure chest is ahead! Only one thought is going through your mind.").pack()
                        path21msg = Label(window21, text = "The riches. As you near the chest, you are met with aggression.").pack()
                        path21msg = Label(window21, text = "It is a mimic! It begins to attack you, causing you to lose 2 lives.").pack()
                        path21msg = Label(window21, text = "You somehow fend it off and after getting out of the room it stopped attacking.").pack()
                        path21msg = Label(window21, text = "The riches. As you near the chest, you are met with aggression.").pack()
                        lives = lives - 2

                        path21 = Label(window21, text = "You have %s lives remaining" % (lives), fg = "red").pack()
                        path21 = Label(window21, text = "Three more paths appear ahead.").pack()
                        path21 = Label(window21, text = "Which path do you pick?").pack()

                        pathV21 = StringVar()
                        pathE21 = Entry(window21, textvariable = pathV21, bd = 5)
                        pathE21.pack()

                        ok21 = Button(window21, text = "OK", command = secondpath1, width = 5, height = 1, bd = 5).pack()
                    elif pathIN2 == "2":
                        window2.destroy()
                        window22 = Tk()
                        window22.title('Dungeon Explorer!')
                        window22.minsize(400, 100)

                        def secondpath21buy():
                            window22 = Tk()
                            window22.title('Dungeon Explorer!')
                            window22.minsize(400, 100)
                            sleep(0.5)
                            secondpath2()
                        def secondpath2():
                            pathIN22 = pathV22.get()
                            global shortsword
                            global bow
                            global leatherA
                            global shield
                            global lives
                            global gold

                            if pathIN22 == "1":
                                window22.destroy()
                                window221 = Tk()
                                window221.title("Dungeon Explorers!")
                                window221.minsize(400, 100)


                                def secondpath21():
                                    pathIN2211 = pathV2211.get()
                                    if pathIN2211 == "1":
                                        path2211msg = Label(window2211, text = "test")
                                def  shortswordb():
                                    global gold
                                    gold = gold - 2
                                    secondpath21buy()
                                def leatherAb():
                                    global gold
                                    gold = gold - 3
                                    secondpath21buy()
                                def shieldb():
                                    global gold
                                    gold = gold - 3
                                    secondpath21buy()
                                def bowb():
                                    global gold
                                    gold = gold - 4
                                    secondpath21buy()


                                path221msg = Label(window221, text = "You have %s live(s)." % (lives), fg = "red").pack()
                                path221msg = Label(window221, text = "You have %s gold(s)." % (gold), fg = "gold").pack()
                                path221msg = Label(window221, text = "You stumble upon a shop. It appears to have many wares.").pack()

                                buy221s = Button(window221, text = "Short Sword - 2 Gold ", command = shortswordb, width = 25, height = 1, bd = 5, fg = "green").pack(side = LEFT)
                                buy221l = Button(window221, text = "Leather Armour - 3 Gold ", command = leatherAb, width = 25, height = 1, bd = 5, fg = "brown").pack(side = RIGHT)
                                buy221b = Button(window221, text = "Bow and Arrows - 4 Gold ", command = bowb, width = 25, height = 1, bd = 5, fg = "red").pack(side = LEFT)
                                buy221sh = Button(window221, text = "Shield - 3 Gold ", command = shieldb, width = 25, height = 1, bd = 5, fg = "blue").pack(side = RIGHT)
                                blankmsg = Label(window221, text = "Done?").pack()
                                buy22 = Button(window221, text = "CONFIRM", command = secondpath21).pack()
                            elif pathIN22 == "2":
                                window22.destroy()
                                window222 = Tk()
                                window222.title("Dungeon Explorers!")
                                window222.minsize(400, 100)

                                path222msg = Label(window222, text = "You have %s live(s)." % (lives), fg = "red").pack()
                                path22 = Label(window222, text = "test2").pack()
                            else:
                                number1to322 = Tk()
                                number1to322.title("ERROR")
                                number1to322.minsize(200, 50)

                                number1to3msg22 = Label(number1to322, text = "Please Enter a number between 1 and 3").pack()
                                number1to3B22 = Button(number1to322, bd = 5, height = 1, width = 10, command = number1to322.destroy, text = "OK",).pack()
                                number1to322.after(3000, number1to322.destroy)
                        path22msg = Label(window22, text = "You have %s live(s)." % (lives), fg = "red").pack()
                        path22msg = Label(window22, text = "It is hard to see far ahead, only the terrain 2 metres ahead of you is visible.").pack()
                        path22msg = Label(window22, text = "Unable to see, you trip over a small bump.").pack()
                        path22msg = Label(window22, text = "As you lift your head, you see a door ahead of you.").pack()
                        path22msg = Label(window22, text = "Do you 1) Open and enter the door 2) Walk around the building", fg = "blue").pack()

                        pathV22 = StringVar()
                        pathE22 = Entry(window22, textvariable = pathV22, bd = 5)
                        pathE22.pack()

                        ok22 = Button(window22, text = "OK", command = secondpath2, width = 5, height = 1, bd = 5).pack()

                    elif pathIN2 == "3":
                        window2.destroy()
                        window23 = Tk()
                        window23.title('Dungeon Explorer!')
                        window23.minsize(400, 100)

                        def secondpath3():
                            pathIN23 = pathV23.get()
                            global lives
                            global gold

                            if pathIN23 == "1":
                                path23 = Label(window23, text = "test1")
                            elif pathIN23 == "2":
                                path23 = Label(window23, text = "test2")
                            else:
                                number1to323 = Tk()
                                number1to323.title("ERROR")
                                number1to323.minsize(200, 50)

                                number1to3msg23 = Label(number1to333, text = "Please Enter a number between 1 and 3").pack()
                                number1to3B23 = Button(number1to333, bd = 5, height = 1, width = 10, command = number1to333.destroy, text = "OK",).pack()
                                number1to323.after(3000, number1to333.destroy)

                        path23msg = Label(window23, text = "You have %s live(s)." % (lives), fg = "red").pack()
                        path23msg = Label(window23, text = "You found a safe passage and a bundle of rope!").pack()
                        path23msg = Label(window23, text = "There appears to be a clearing ahead").pack()
                        path23 = Label(window23, text = "Do you 1) Head for the clearing 2) Head deeper into the forest", fg = "blue").pack()

                        pathV23 = StringVar()
                        pathE23 = Entry(window23, textvariable = pathV23, bd = 5)
                        pathE23.pack()

                        ok23 = Button(window23, text = "OK", command = secondpath3, width = 5, height = 1, bd = 5).pack()

                    else:
                        number1to32 = Tk()
                        number1to32.title("ERROR")
                        number1to32.minsize(200, 50)

                        number1to3msg2 = Label(number1to32, text = "Please Enter a number between 1 and 3").pack()
                        number1to3B2 = Button(number1to32, bd = 5, height = 1, width = 10, command = number1to32.destroy, text = "OK",).pack()
                        number1to32.after(3000, number1to32.destroy)

                path2msg = Label(window2, text = "You have %s live(s)." % (lives), fg = "red").pack()
                path2msg = Label(window2, text = "You find 5 gold lying on the floor").pack()
                gold = gold + 5
                path2msg = Label(window2, text = "You now have a total of : %s gold" % (gold), fg = "green").pack()
                path2msg = Label(window2, text = "A shard of glass is also on the floor next to the abandoned house").pack()
                path2msg = Label(window2, text = "In the shard of glass, you see yourself.").pack()
                path2msg = Label(window2, text = "A green being.").pack()
                path2msg = Label(window2, text = "A goblin.").pack()

                path2msg = Label(window2, text = "Do you : 1) Head in the abandoned house 2) Go through the misty path 3) Head towards the forest", fg = "blue").pack()

                pathV2 = StringVar()
                pathE2 = Entry(window2, textvariable = pathV2, bd = 5)
                pathE2.pack()

                ok2 = Button(window2, text = "OK", bd = 5, command = secondpath, width = 5, height = 1).pack()

            elif pathIN == "3":
                death = Tk()
                death.title("RIP")
                death.minsize(400, 100)
                window.destroy()

                def restartingthird():
                    death.destroy()
                    everypath()

                lives = 0
                deathmsg3 = Label(death, text = "You have %s lives remaining" % (lives), fg = "red").pack()
                deathmsg3 = Label(death, text = "The ground beneath you suddenly went down slightly.").pack()
                deathmsg3 = Label(death, text = "Its movement was very smooth. Holes emerge from the walls.").pack()
                deathmsg3 = Label(death, text = "Arrows come flying out, in a rapid attempt to dodge the arrows, you trip over your own feet as your leg gets pierced by an arrow.").pack()
                deathmsg3 = Label(death, text = "This ends in you being unable to escape the floor as it slowly.").pack()
                deathmsg3 = Label(death, text = "Below you is a bottomless pit.").pack()
                deathmsg3 = Label(death, text = "Unable to move, you prepare for the inevitable.").pack()
                deathmsg3 = Label(death, text = "Death.").pack()
                deathmsgok = Button(death, bd = 5, text = "Quit", command = death.destroy, height = 2, width = 30).pack(side = LEFT)
                deathmsgretry = Button(death, bd = 5, text = "Retry", command = restartingthird, height = 2, width = 30).pack(side = RIGHT)
            else:
                number1to3 = Tk()
                number1to3.title("ERROR")
                number1to3.minsize(200, 50)

                number1to3msg = Label(number1to3, text = "Please Enter a number between 1 and 3").pack()
                number1to3B = Button(number1to3, height = 1, width = 10, bd = 5, command = number1to3.destroy, text = "OK",).pack()
                number1to3.after(3000, number1to3.destroy)

        welcome = Label(window, text = "Welcome to Dungeon Explorer!", fg = "Blue")
        welcome.pack()

        path = Label(window, text = "You have %s live(s)." % (lives), fg = "red").pack()
        path = Label(window, text = "Distant memories of human life flow throughout your mind.").pack()
        path = Label(window, text = "As you flex your arms and legs, it becomes clear that your hands have green smeared all over them.").pack()
        path = Label(window, text = "You quickly dismiss that fact because you know that nothing will happen without action.").pack()
        path = Label(window, text = "Do you 1) Go left 2) Go in the middle path 3) Go right", fg = "blue")
        path.pack()

        pathV = StringVar()
        pathE = Entry(window, textvariable = pathV, bd = 5)
        pathE.pack()

        ok = Button(window, text = "OK", command = paths, width = 5, height = 1, bd = 5).pack()
    else:
        restart = 0
        everypath()

everypath()
