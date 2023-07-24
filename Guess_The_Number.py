import random

choice = ""
while True:
    try:
        choice = int(input("If you want to find the number, enter 1. If you want the computer to find it, enter 2: "))
        if choice == 1 or choice == 2:
            break
    except ValueError:
        print("Enter 1 or 2 please. No words")

#----------User Guess-----------
if choice == 1:
    def guessNumbUser(computer, user):
        if computer > user:
            print("UP!")
        else:
            print("DOWN!")

    computer = random.randint(0, 100)

    def userInput1():
        while True:
            user_input = input("Enter a number between 0 and 100 (both included): ")
            if user_input.isdigit():
                user = int(user_input)
                if 0 <= user <= 100:
                    return user
                else:
                    print("Please enter a number between 0 and 100.")
            else:
                print("Please enter numbers like 1, 2, 45, 100")

    user = userInput1()
    while user != computer:
        guessNumbUser(computer, user)
        user = int(input())
    print(f"Your answer: {user} is correct.")

#----------Comp Guess----------
elif choice == 2:
    def userInput2():
        while True:
            user_input = input("Please enter correct, up, or down: ")
            if user_input.upper() in ["CORRECT", "UP", "DOWN"]:
                return user_input.upper()
    def guessNumbComputer(computer, user):
        if user == "UP":
            computer = computer + computer / 2
        elif user == "DOWN":
            computer = computer - computer / 2
        return round(computer)

    computer = random.randint(0, 100)
    while True:
        print(f"Is {computer} correct?")
        user = userInput2()
        if user == "CORRECT":
            break
        else:
            computer = guessNumbComputer(computer, user)
    print("Correct Answer Was " + str(computer))

