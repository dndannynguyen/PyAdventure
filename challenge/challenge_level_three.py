"""
Danny Nguyen
A01353084
"""
import random


def get_secret_word():
    all_words = ['international', 'immutable', 'javascript', 'canada', 'dictionary', 'recursion', 'iteration']
    return random.choice(all_words)


def show_game_rules(allowed_errors):
    print(f"\n\nWelcome to Level Three Game, Hangman!\n\n"
          f"We have the hidden word showed as '_ _ _'.\n"
          f"You have to enter the letter that you guess would appear in the word.\n"
          f"You can only make {allowed_errors} wrong guesses. \n")


def display_hidden_word(secret_word, guesses):
    message = '\nThe hidden word: '
    for letter in secret_word:
        if letter.lower() in guesses:
            message += letter + " "
        else:
            message += "_" + " "
    print(f"{message}")


def get_player_guess(allowed_errors):
    guess = input(f"Allowed Wrong Guess Left: {allowed_errors}. \n"
                  f"Your guess: ")
    return guess.lower()


def level_three_games():
    secret_word = get_secret_word()
    allowed_errors = 12
    guesses = []
    done = False

    show_game_rules(allowed_errors)

    while not done:
        display_hidden_word(secret_word, guesses)
        done = True
        guess = get_player_guess(allowed_errors)
        guesses.append(guess.lower())

        if guess.lower() not in secret_word.lower():
            allowed_errors -= 1
            if allowed_errors == 0:
                break

        done = True
        for letter in secret_word:
            if letter.lower() not in guesses:
                done = False
                break

    if done and allowed_errors > 0:
        print(f"You got it: '{secret_word}'.")
    else:
        print(f"You are out of guesses. The hidden word is {secret_word}")
    return done and allowed_errors > 0


def main():
    """
    Drive the program.
    """
    print(level_three_games())


if __name__ == '__main__':
    main()
