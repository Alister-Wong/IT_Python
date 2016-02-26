from collections import Counter

line = input("Line: ")
if "robot" in line:
    print("There is a small robot in the line.")
elif "ROBOT" in line:
    words = line.split()
    ROBOTcount = 'R, O, B, T' in words
    print(ROBOTcount)
    print("There is a big robot here")
elif "robot" in line.lower():
    print("There is a medium robot in the line.")
else:
    print("No robots here")
    
