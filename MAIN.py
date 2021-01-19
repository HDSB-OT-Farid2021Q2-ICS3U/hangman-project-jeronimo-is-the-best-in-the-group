import os
import random
import time
from dictionary import _dict

red = "\033[91m"
yellow = "\033[1;33m"
green = "\033[92m"

end = "\033[0m"
def lives10():
    print("     _______________")
    print("     |             |")
    print("     |            ---")
    print("     |           |   |")
    print("     |            ---")
    print("     |             |")
    print("     |            /|\ ")
    print("     |           / | \ ")
    print("     |          /  |  \ ")
    print("     |         /\  |  /\ ")
    print("     |            / \ ")
    print("     |           /   \ ")
    print("     |          /     \ ")
    print("     |")
    print("-----------")

def lives9():
    print("     _______________")
    print("     |             |")
    print("     |            ---")
    print("     |           |   |")
    print("     |            ---")
    print("     |             |    ")
    print("     |            /|\   ")
    print("     |           / | \  ")
    print("     |          /  |  \ ")
    print("     |         /\  |   ")
    print("     |            / \ ")
    print("     |           /   \ ")
    print("     |          /     \ ")
    print("     |")
    print("-----------")


def lives8():
    print("     _______________")
    print("     |             |")
    print("     |            ---")
    print("     |           |   |")
    print("     |            ---")
    print("     |             |")
    print("     |            /|\ ")
    print("     |           / | \ ")
    print("     |          /  |  \ ")
    print("     |             |   ")
    print("     |            / \ ")
    print("     |           /   \ ")
    print("     |          /     \ ")
    print("     |")
    print("-----------")

def lives7():
    print("     _______________")
    print("     |             |")
    print("     |            ---")
    print("     |           |   |")
    print("     |            ---")
    print("     |             |")
    print("     |            /|\ ")
    print("     |           / | \ ")
    print("     |          /  |  \ ")
    print("     |             |")
    print("     |              \ ")
    print("     |               \ ")
    print("     |                \ ")
    print("     |")
    print("-----------")

def lives6():
    print("     _______________")
    print("     |             |")
    print("     |            ---")
    print("     |           |   |")
    print("     |            ---")
    print("     |             |")
    print("     |            /|\ ")
    print("     |           / | \ ")
    print("     |          /  |  \ ")
    print("     |             |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("-----------")

def lives5():
    print("     _______________")
    print("     |             |")
    print("     |            ---")
    print("     |           |   |")
    print("     |            ---")
    print("     |             |")
    print("     |             |\ ")
    print("     |             | \ ")
    print("     |             |  \ ")
    print("     |             |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("-----------")

def lives4():
    print("     _______________")
    print("     |             |")
    print("     |            ---")
    print("     |           |   |")
    print("     |            ---")
    print("     |             |")
    print("     |             |")
    print("     |             |")
    print("     |             |")
    print("     |             |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("-----------")

def lives3():
    print("     _______________")
    print("     |             |")
    print("     |          -------")
    print("     |         | .   . |")
    print("     |         |  ___  |")
    print("     |         | |   | |")
    print("     |          -------")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("-----------")

def lives2():
    print("     _______________")
    print("     |             |")
    print("     |          -------")
    print("     |         | .   x |")
    print("     |         |       |")
    print("     |         |  ___  |")
    print("     |          -------")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("-----------")
def lives1():
    print("     _______________")
    print("     |             |")
    print("     |          -------")
    print("     |         | x   x |")
    print("     |         |       |")
    print("     |         |  ___  |")
    print("     |          -------")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("-----------")
def lives0():
    print("     _______________")
    print("     |             |")
    print("     |          -------")
    print("     |         | x   x |")
    print("     |         |       |")
    print("     |         | xxxxx |")
    print("     |          -------")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("-----------")
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------


def hangman():
    print("Welcome to the beloved game, Hang Man! Your task is to guess all the letters")
    print("in the word before the man hanging dies! every time you guess a letter NOT in the word")
    print("one part of the hanging man falls off! If there are no more parts left of him,")
    print("yooouu loooooose. So guess correctly!")
    
    #takes user's operating system for the clear() function
    print("-" * 10, "menu", "-" * 10)
    print("|", "Unix(Mac/linux)".center(22), "|")
    print("|" + "-" * 24 + "|")
    print("|", "Windows".center(22), "|")
    print("-" * 26)

    operatingsys = input("Firstly, are you using a Unix based system or windows?\n\n")
    while True:
        if operatingsys.lower() == "unix":
            clear = lambda: os.system('clear')
            break

        elif operatingsys.lower() == "windows":
            clear = lambda: os.system('cls')
            break

        else:
            operatingsys = input("Invalid input! unix, or windows?\n")

    #takes the users desired gamemode, and adjusts game difficulty accordingly
    clear()
    print("\n\n" + "-" * 10, "menu", "-" * 10)
    print("|", green, "Easy".center(20), end, "|")
    print("|" + "-" * 24 + "|")
    print("|",yellow, "Medium".center(20), end, "|")
    print("|" + "-" * 24 + "|")
    print("|", red, "Hard".center(20), end, "|")
    print("-" * 26)

    difficulty = input("Now, what would you like the game difficulty to be set at? easy, medium, or hard?\n\n")
    while True:
        if difficulty.lower() == "easy" or difficulty.lower() == "medium" or difficulty.lower() == "hard":
            break
        else:
            difficulty = input("You didnt choose a valid difficulty! Please try again!\n")


    #if easy, the use had 10 attempts before they lose, program chooses random word from _dict, and shows user the number of letters the word has.

    if difficulty == "easy":
        lives = 10
        print("Really? Easy mode? noob. Anywho, you have", lives, "lives, good luck!\n")
        word = random.choice(_dict)
        print("you have ", lives, "attempts ")
        guess = []
        lives10()
        e = len(word)
        print('_ ' * e)
        print(word)
    

        while True:
            if lives == 0:
                lives0()
                print("".join(emptyview))
                print("Sorry, you lost :( \nThe word was", word)
                killswitch()
            userinput = str(input("\nGuess a letter: "))
            clear()
            while userinput in guess:
                clear()
                if lives == 10:
                    lives10()
                elif lives == 9:
                    lives9()
                elif lives == 8:
                    lives8()
                elif lives == 7:
                    lives7()
                elif lives == 6:
                    lives6()
                elif lives == 5:
                    lives5()
                elif lives == 4:
                    lives4()
                elif lives == 3:
                    lives3()
                elif lives == 2:
                    lives2()
                elif lives == 1:
                    lives1()
                elif lives == 0:
                    lives0()
                print("".join(emptyview))
                userinput = input("\nYou have already guessed this letter, guess another one: ")
                clear()
            guess.append(userinput)
            if len(userinput)>=2:
                if userinput==word:
                    print("Correct!, The word was",word)
                    killswitch()
                elif userinput!=word:
                    print("Wrong!")
                    lives -= 1
            elif len(userinput)==1:
                guess.append(userinput) 
                emptyview = [i if i in guess else '_' for i in word]
                clear()
                if lives == 10:
                    lives10()
                elif lives == 9:
                    lives9()
                elif lives == 8:
                    lives8()
                elif lives == 7:
                    lives7()
                elif lives == 6:
                    lives6()
                elif lives == 5:
                    lives5()
                elif lives == 4:
                    lives4()
                elif lives == 3:
                    lives3()
                elif lives == 2:
                    lives2()
                elif lives == 1:
                    lives1()
                elif lives == 0:
                    lives0()
                print("".join(emptyview))
                if userinput not in word:
                    clear()
                    print("bruh you silly, that letter is not in the word!")
                    lives -= 1
                    if lives == 10:
                        lives10()
                    elif lives == 9:
                        lives9()
                    elif lives == 8:
                        lives8()
                    elif lives == 7:
                        lives7()
                    elif lives == 6:
                        lives6()
                    elif lives == 5:
                        lives5()
                    elif lives == 4:
                        lives4()
                    elif lives == 3:
                        lives3()
                    elif lives == 2:
                        lives2()
                    elif lives == 1:
                        lives1()
                    elif lives == 0:
                        lives0()
                    print("You have", lives, "attempts left!\n")
                    print("".join(emptyview))
                if emptyview == list(word):
                    print("You won!")
                    killswitch()
                    break





    elif difficulty == "medium":
        print("You choice difficulty: Medium, this is considered \"normal\" mode.\n")
        lives = 8
        print("you have ", lives, "attempts ")
        word = random.choice(_dict)
        guess = []
        lives8()
        e = len(word)
        print('_ ' * e)
        print(word)


        while True:
            if lives == 0:
                clear()
                lives0()
                print("".join(emptyview))
                print("Sorry, you lost :( \nThe word was", word)
                killswitch()
            userinput = str(input("\nGuess a letter: "))
            while userinput in guess:
                clear()
                if lives == 8:
                    lives8()
                elif lives == 7:
                    lives7()
                elif lives == 6:
                    lives6()
                elif lives == 5:
                    lives5()
                elif lives == 4:
                    lives4()
                elif lives == 3:
                    lives3()
                elif lives == 2:
                    lives2()
                elif lives == 1:
                    lives1()
                elif lives == 0:
                    lives0()
                print("".join(emptyview))
                userinput = input("\nYou have already guessed this letter, guess another one: ")
                clear()
            guess.append(userinput)
            if len(userinput)>=2:
                if userinput==word:
                    print("Correct!, The word was",word)
                    killswitch()
                elif userinput!=word:
                    print("Wrong!")
                    lives -= 1
            elif len(userinput)==1:
                guess.append(userinput) 
                emptyview = [i if i in guess else '_' for i in word]
                clear()
                if lives == 8:
                    lives8()
                elif lives == 7:
                    lives7()
                elif lives == 6:
                    lives6()
                elif lives == 5:
                    lives5()
                elif lives == 4:
                    lives4()
                elif lives == 3:
                    lives3()
                elif lives == 2:
                    lives2()
                elif lives == 1:
                    lives1()
                elif lives == 0:
                    lives0()
                print("".join(emptyview))
                if userinput not in word:
                    clear()
                    print("bruh you silly, that letter is not in the word!")
                    lives -= 1
                    if lives == 8:
                        lives8()
                    elif lives == 7:
                        lives7()
                    elif lives == 6:
                        lives6()
                    elif lives == 5:
                        lives5()
                    elif lives == 4:
                        lives4()
                    elif lives == 3:
                        lives3()
                    elif lives == 2:
                        lives2()
                    elif lives == 1:
                        lives1()
                    elif lives == 0:
                        lives0()
                    print("You have", lives, "attempts left!\n")
                    print("".join(emptyview))
                if emptyview == list(word):
                    print("You won!")
                    killswitch()
                   
                    break
    




    elif difficulty == "hard":
        print("Oh you trying Hard mode I see? Good luck chief!\n")
        lives = 6
        print("you have ", lives, "attempts ")
        word = random.choice(_dict)
        guess = []
        lives6()
        e = len(word)
        print('_ ' * e)
        print(word)


        while True:
            if lives == 0:
                lives0()
                print("".join(emptyview))
                print("Sorry, you lost :( \nThe word was", word)
                killswitch()
            userinput = str(input("\nGuess a letter: "))
            while userinput in guess:
                clear()
                if lives == 6:
                    lives6()
                elif lives == 5:
                    lives5()
                elif lives == 4:
                    lives4()
                elif lives == 3:
                    lives3()
                elif lives == 2:
                    lives2()
                elif lives == 1:
                    lives1()
                elif lives == 0:
                    lives0()
                print("".join(emptyview))
                userinput = input("\nYou have already guessed this letter, guess another one: ")
                clear()
            guess.append(userinput)
            if len(userinput)>=2:
                if userinput==word:
                    print("Correct!, The word was",word)
                    killswitch()
                elif userinput!=word:
                    print("Wrong!")
                    lives -= 1
            elif len(userinput)==1:
                guess.append(userinput) 
                emptyview = [i if i in guess else '_' for i in word]
                clear()
                if lives == 6:
                    lives6()
                elif lives == 5:
                    lives5()
                elif lives == 4:
                    lives4()
                elif lives == 3:
                    lives3()
                elif lives == 2:
                    lives2()
                elif lives == 1:
                    lives1()
                elif lives == 0:
                    lives0()
                print("".join(emptyview))
                if userinput not in word:
                    clear()
                    print("bruh you silly, that letter is not in the word!")
                    lives -= 1
                    if lives == 6:
                        lives6()
                    elif lives == 5:
                        lives5()
                    elif lives == 4:
                        lives4()
                    elif lives == 3:
                        lives3()
                    elif lives == 2:
                        lives2()
                    elif lives == 1:
                        lives1()
                    elif lives == 0:
                        lives0()
                    print("You have", lives, "attempts left!\n")
                    print("".join(emptyview))
                if emptyview == list(word):
                    print("You won!")
                    killswitch()
                   
                    break





def killswitch():
    while True:
        answer = input("Would you like to play again? y/n?\n")
        if answer.lower() == "y":
            print("Proceed with caution")
            hangman()
        elif answer.lower() == "n":
            print("Hasta La Vista Baby")
            exit()

lives10()
hangman()

  


