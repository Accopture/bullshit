import random
from sys import exit


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