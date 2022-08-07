# A game where the user has to guess a randomly generated number
import random  # https://docs.python.org/3.9/library/random.html


def guess(x):
    random_number = random.randint(1, x)

    number = 0
    while number != random_number:
        number = int(input(f'Guess a number between 1 and {x}: '))

        if number < random_number:
            print("Too low.\n")

        elif number > random_number:
            print("Too high.\n")

    print(f'Congratulations! {number} is the magic number!')


def computer_guess(x):
    low = 1
    high = x

    feedback = ''
    number = 0
    while feedback != 'c':
        if low != high:
            number = random.randint(low, high)
        else:
            number = low

        feedback = input(f'\nIs {number} too high (H), too low (L), or correct (C)? ').lower()

        if feedback == 'h':
            high = number - 1

        elif feedback == 'l':
            low = number + 1

    print(f'\nThe computer guessed correctly. The magic number was {number}!')


guess(10)
computer_guess(10)
