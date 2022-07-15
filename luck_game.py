from random import randint


def guess_a_number():
    while True:
        try:
            guessed_number = int(input('Select a number between 1 and 10: '))
        except ValueError:
            print('You may only enter a numeric value, please try again')
            continue

        if guessed_number < 1 or guessed_number > 10:
            print('Your number must be between 1 and 10')
            continue

        return guessed_number


def is_guess_correct(target, guess):
    if guess > target:
        print('Your guess is too big')
        return False

    if guess < target:
        print('Your guess is too small')
        return False

    print('You win the game')
    return True


target_number = randint(1, 10)
while True:
    player_guess = guess_a_number()
    player_wins = is_guess_correct(target_number, player_guess)

    if not player_wins:
        continue

    play_again = input('Would you like to play again? Type Y to play again and anything else to quit: ')
    if play_again.lower() != 'y':
        break

    target_number = randint(1, 10)

print('Thank you for playing.')
