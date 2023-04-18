import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 # random is between 1 and x, for this reason guess = 0, for make sure that we will not guess accidentaly the number

    # WHILE LOOP
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Wow, congrats. You have guessed the number {random_number} correctly!.')


guess(10)