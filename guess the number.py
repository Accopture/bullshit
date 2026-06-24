import random
from sys import exit
def retry():
    while True:
        retinp = input("Wouldst thou like to try again? (Y/N): ").strip().upper()
        if retinp == "Y":
            return True
            
        elif retinp == "N":
            print("Fare thee well, brave soul!")
            sys.exit()
            
            print("Pray, enter Y or N.")

while True:
    try:
        randvar = random.randint(1, 20)
        nguess = int(input("Pray tell, A number has been chosen from 1 to 20, doth thee possess the wisdom to ascertain it?: "))
        
        if nguess == randvar:
            print("Huzzah! Thou hast guessed correctly!")
            if retry():
                continue
               
        else:
            print("Alas! The number was", randvar, "Better luck next time!")
            if retry():
                continue

             
    except ValueError:
        print("Pray, insert a number.")