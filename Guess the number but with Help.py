import sys 
import random
def retry():
    while True:
        retinp = input("Wouldst thou like to try again? (Y/N): ").strip().upper()
        if retinp == "Y":
            return True
            
        elif retinp == "N":
            print("Fare thee well, brave soul!")
            sys.exit()
        else:    
            print("Pray, enter Y or N.")
            
print("Verily, a number from 1-200 hath been chosen, guess it in the field under")
while True:
        randvar = random.randint(1, 200)
        while True:
            try:
                usrint = int(input("Input thy guess: "))
                if usrint > randvar:
                    print("Lower")
                elif usrint < randvar:
                    print("Higher")
                elif usrint == randvar:
                    print("Brilliant! thou hast won the game!")
                    if retry():
                        break
            except ValueError:
                print("Insert integers, fellow")