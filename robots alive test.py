def test:
    srobot = "robot"
    mrobot = "robot"
    lrobot = "ROBOT"
    line = input("Line: ")
    word = line.split()
    word1 = word.count("r, o, b, t")
    gay = len(word)
    count = 1 - gay
    print(word1)

    for i in line :
        count += 1
        print(count)
    if srobot in word:
        print("There is a small robot in the line.")
    elif lrobot in word:
        print("There is a big robot in the line.")  
    elif mrobot in line.lower():
        print("There is a medium robot in the line.")   
    else:
        print("No robots here")
