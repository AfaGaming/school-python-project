# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
name = input("What's your name? ")
print(f"Hello, {name}! Welcome to the video games quiz!")
questionNumber = 1
score = 0
while (questionNumber <= 7):
    if questionNumber == 1:
        print(f"Q1. When was Minecraft released?")
        print(f"a. 2011")
        print(f"b. 2009")
        print(f"c. 2013")
        print(f"d. 2016")
        userAnswer = input("Your answer: ")
        if userAnswer == "a" or userAnswer == "A":
            print("That is correct!")
            score = score + 1
        else:
            print("That is not correct! The answer was option A.")
    if questionNumber == 2:
        print(f"Q2. When was Roblox released?")
        print(f"a. 1975")
        print(f"b. 2009")
        print(f"c. 2006")
        print(f"d. 1979")
        userAnswer = input("Your answer: ")
        if userAnswer == "c" or userAnswer == "C":
            print("That is correct!")
            score = score + 1
        else:
            print("That is not correct! The answer was option C.")
    if questionNumber == 3:
        print(f"Q3. When was Subway Surfers released?")
        print(f"a. 2004")
        print(f"b. 2009")
        print(f"c. 2006")
        print(f"d. 2012")
        userAnswer = input("Your answer: ")
        if userAnswer == "d" or userAnswer == "D":
            print("That is correct!")
            score = score + 1
        else:
            print("That is not correct! The answer was option D.")
    if questionNumber == 4:
        print(f"Q4. Who orignally made Minecraft?")
        print(f"a. Bill Gates")
        print(f"b. Notch")
        print(f"c. Kevin")
        print(f"d. Jeff")
        userAnswer = input("Your answer: ")
        if userAnswer == "b" or userAnswer == "B":
            print("That is correct!")
            score = score + 1
        else:
            print("That is not correct! The answer was option B.")
    if questionNumber == 5:
        print(f"Q5. Who currently owns Minecraft?")
        print(f"a. Apple")
        print(f"b. Notch")
        print(f"c. Microsoft")
        print(f"d. Riot Studios")
        userAnswer = input("Your answer: ")
        if userAnswer == "c" or userAnswer == "C":
            print("That is correct!")
            score = score + 1
        else:
            print("That is not correct! The answer was option C.")
    if questionNumber == 6:
        print(f"Q6. When did Microsoft buy Minecraft?")
        print(f"a. 2014")
        print(f"b. 2020")
        print(f"c. 2015")
        print(f"d. 2023")
        userAnswer = input("Your answer: ")
        if userAnswer == "a" or userAnswer == "A":
            print("That is correct!")
            score = score + 1
        else:
            print("That is not correct! The answer was option A.")
    if questionNumber == 7:
        if score  > 3:
            i = 1
            while i <= 5:
                print(f"Well done! You got {score}/6")
                i=i+1
        else:
            print(f"Well done! You got {score}/5")
        print("Thanks for playing!")
    questionNumber = questionNumber + 1;
