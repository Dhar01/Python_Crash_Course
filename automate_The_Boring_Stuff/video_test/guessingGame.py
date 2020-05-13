# this is a guess the number game

import random

print("Hello! What's your name?")
name = input()

print('Well, ' + name + ', I am thinking of a nubmer between 1 to 29')
secretNumber = random.randint(1, 20)


for guessesTaken in  range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess to high')
    else:
        break       # this condition is for the correct guess!

if guess == secretNumber:
    print('Good job, ' + name + '! Your guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope , the number I was thinking of was ' + str(secretNumber))