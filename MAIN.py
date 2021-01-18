import os
import random
from dictionary import _dict

red = "\033[91m"
yellow = ""
green = "\033[92m"
end = "\033[0m"

words = ["fuck", "hello", "canada", "banana"]

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
    print("     |            / \ ")
    print("     |           /   \ ")
    print("     |          /     \ ")
    print("     |")
    print("-----------")

def lives5():
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

def lives4():
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

def lives3():
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

def lives2():
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

def lives1():
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

def lives0():
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
        
        lives = 6
        print("Really? Easy mode? noob. Anywho, you have", lives, "lives, good luck!\n")
        word = random.choice(_dict)
        print(word)
        guess = []
        lives6()
        
        while lives > 0:
            userinput = str(input("\nGuess a letter: "))
            if len(userinput)>=2:
                if userinput==words:
                    print("Correct!, The word was",word)
                    replay = str(input(("Would you like to play again? Y/N: ")))
                    if  replay.lower()=="n":
                        break
                    elif replay.lower()=="y":
                        break
                        hangman()
                elif userinput!=words:
                    print("Wrong!")
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
                    print("bruh you silly, that letter is not in the word!")
                    lives -= 1
                    if lives == 5:
                        clear()
                        lives5()
                    elif lives == 4:
                        clear()
                        lives4()
                    elif lives == 3:
                        clear()
                        lives3()
                    elif lives == 2:
                        clear()
                        lives2()
                    elif lives == 1:
                        clear()
                        lives1()
                    elif lives == 0:
                        clear()
                        lives0()
                    print("You have", lives, "attempts left!\n")
                    print("".join(emptyview))
                if emptyview == list(word):
                    print("".join(emptyview))
                    print("You won!")
                    break 

    elif difficulty == "medium":
        print("You choice difficulty: Medium, this is considered \"normal\" mode.\n")
    
    elif difficulty == "hard":
        print("Oh you trying Hard mode I see? Good luck chief!\n")



#User Inputs Letters


#Takes an input from the user and determines whether they are trying to guess the entire word

   
          

# find if letter is in the word and for those that arentnare replaced with blank

lives6()
hangman()

  


