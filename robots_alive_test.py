def robots_alive_test(line):
    srobot = "robot"
    mrobot = "robot"
    lrobot = "ROBOT"
    word = line.split()
    word1 = word.count("r, o, b, t")
    word2 = len(word)
    count = 1 - word2
    print(word1)

    for i in line :
        count += 1
    if srobot in word:
        print("There is a small robot in the line.")
    elif lrobot in word:
        print("There is a big robot in the line.")  
    for x in word:
        x = x.lower()
        if mrobot in x:
            print("There is a medium robot in the line.")   
    else:
        print("No robots here")
    return count
