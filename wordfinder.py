import random
from dictionary import _dict

x = random.choice(_dict)
print(x)

userinput = str(input("Guess a letter: "))
#User Inputs Letters
while True:
    if len(userinput)>=2:
        if userinput==x:
            print("Correct!, The word was",x)
            replay = str(input(("Would you like to play again? Y/N: ")))
            if  replay.lower()=="n":
                break
            elif replay.lower()=="y":
                break
                hangman()
        elif userinput!=x:
            print("Wrong!")
            #Function for drawing arm

