import os
import random
from dictionary import _dict

red = "\033[91m"
yellow = ""
green = "\033[92m"
end = "\033[0m"

words = ["fuck", "hello", "canada", "banana"]

def easy():
    head = ("    ___\n   |   |\n    ---")
    arm1 = ("___")
    arm2 = ("___")
    body = ("     |\n  " + arm1 + "|" + arm2 + "\n     |\n     |")
    leg1 = ("    /\ \n   /  \ ")
    leg2 = ("  /    \ \n /      \ ")
    print(head)
    print(body)
    print(leg1)
    print(leg2)

def medium():
    head = ("    ___\n   |   |\n    ---")
    arm1 = ("___")
    arm2 = ("___")
    body = ("     |\n  " + arm1 + "|" + arm2 + "\n     |\n     |")
    legs = ("    /\ \n   /  \ \n  /    \ \n /      \ ")
    print(head)
    print(body)
    print(legs)

#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------


def hangman():
    print("Welcome to the beloved game, Hang Man! Your task is to guess all the letters")
    print("in the word before the man hanging dies! every time you guess a letter NOT in the word")
    print("one characteristic of the hanging man falls off! If there are no more parts left of him,")
    print("yooouu loooooose. So guess correctly!")
    
    print("-" * 10, "menu", "-" * 10)
    print("|", "Unix(Mac/linux)".center(22), "|")
    print("|" + "-" * 24 + "|")
    print("|", "Windows".center(22), "|")
    print("-" * 26)

    operatingsys = input("Firstly, are you using a Unix based system (mac / linux) or windows?\n")
    while True:
        if operatingsys.lower() == "unix":
            clear = lambda: os.system('clear')
            break

        elif operatingsys.lower() == "windows":
            clear = lambda: os.system('cls')
            break

        else:
            operatingsys = input("Invalid input! unix, or windows?\n")


    clear()
    print("\n\n" + "-" * 10, "menu", "-" * 10)
    print("|", green, "Easy".center(20), end, "|")
    print("|" + "-" * 24 + "|")
    print("|", "Medium".center(22), "|")
    print("|" + "-" * 24 + "|")
    print("|", red, "Hard".center(20), end, "|")
    print("-" * 26)

    difficulty = input("Now, what would you like the game difficulty to be set at? easy, medium, or hard?\n")
    while True:
        if difficulty.lower() == "easy" or difficulty.lower() == "medium" or difficulty.lower() == "hard":
            break
        else:
            difficulty = input("You didnt choose a valid difficulty! Please try again!\n")


    if difficulty == "easy":
        print("Really? Easy mode? noob. Anywho,\n")
        wordnumber = random.randrange(0,3)
        word = words[wordnumber]
        print(word)
        guesses = ""

        guesses += "_" * len(word)
        print(guesses)
          

    elif difficulty == "medium":
        print("You choice difficulty: Medium, this is considered \"normal\" mode.\n")
    
    elif difficulty == "hard":
        print("Oh you trying Hard mode I see? Good luck chief!\n")

easy()
hangman()
