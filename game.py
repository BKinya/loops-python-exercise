
import random

number = random.randint(1, 10) #return random integers from low to high
tries = 1

u_name = input("Hello, what is your username?")
print("Hello", u_name+ ",", )

question = input("Would you like to play a game?[Y/N]")
if question == "N":
    print("oh..okay")
elif question == "Y":
    print("I'm thinking of a number between 1 & 10")
    guess = int(input("Have a guess: "))

    #loop until the user guesses a number that is equal to the suggested number
    while guess != number:
        tries += 1
        if guess > number:
            print("Guess Higher")
            guess = int(input("Try again: "))
        elif guess < number:
            print("Guess Lower")
            guess = int(input("Try again: "))
        
    print("You're right! You win! The number was {}. You got  its only {} tries".format(number, tries)) 