while 0 < 1:
    print("What is my favourite food?")
    question = input("Guess?")
    if question.lower() == "electricity":
        print("You guessed it! Buzzzz")
        exit()
    else:
        print("Not even close.")
