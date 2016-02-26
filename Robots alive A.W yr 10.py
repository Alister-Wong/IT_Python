srobot = "robot"
mrobot = "robot"
lrobot = "ROBOT"
line = input("Line: ")
word = line.split()
letter = len(word)

if srobot in word:
    print("There is a small robot in the line.")
elif lrobot in word:
    print("There is a big robot in the line.")  
elif mrobot in (name.lower() for name in word):
    print("There is a medium robot in the line.")   
else:
    print("No robots here")
