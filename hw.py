import random
from sys import exit
maxnumber = int(
    input("Choose a maximum number (will choose numbers between this range): "))
number = random.randint(1, maxnumber)
chances = 4
hints = 2
print(number)
print('I have chosen a number between 1 and {}. You have {} chances and {} hints remaining.'.format(maxnumber, chances, hints))
while chances != 0:
    numberguess = int(input("Enter your guess: "))
    if isinstance(numberguess, int):
        if numberguess != number:
            chances-=1
            print('\nIncorrect. {} chances and {} hints remaining'.format(chances, hints))
            if chances !=0:
                guess = input("Take a hint? ")
                if guess == 'yes':
                    if numberguess < number:
                        print('\nYour guess {} was too low\n{} chances and {} hints remaining'.format(numberguess, chances, hints))
                        hints-=1
                    elif numberguess > number:
                        print('\nYour guess {} was too high\n{} chances and {} hints remaining'.format(numberguess, chances, hints))
                        hints-=1
        elif numberguess == number:
            print('\nYou Win! The number was', number)
            exit()
if chances == 0:
    print('You loose. I was thinking of the number {}'.format(number))
