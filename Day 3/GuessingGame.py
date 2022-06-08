# Goal for user is to guess a seecret number decided by the program
import random
secret =  random.randint(0, 9)
print("The number lies between 0 and 9, and you get only three guesses")

for i in range(0, 3):
    no = int(input("Guess the number: "))
    if no == secret:
        print("You guessed it!")
        break
else:
    print("Sorry, the number was: " + str(secret))