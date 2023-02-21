#Mastermind game in console

import random
import GameVariables as game_vars

#Generate code to guess
def generate_code():
    code = []
    code = [random.choice(game_vars.COLORS) for i in range(game_vars.MAX_NUMBER_OF_GUESSED_COLORS)]
    print("{}".format(code))
    return code

#Check if correct guess entered
def get_color_input():
    guess = input()
    guess = input_fix(guess)
    while (len(guess) != game_vars.MAX_NUMBER_OF_GUESSED_COLORS or check_input_errors(guess) is False):
        print("Bad input, please re-enter: ")
        guess = input()
        guess = input_fix(guess)

    return guess

#Check correct options entered
def check_input_errors(guess):
    for i in range(game_vars.MAX_NUMBER_OF_GUESSED_COLORS):
        if guess[i] not in game_vars.COLORS:
            print("{} is not a correct choice, correct choices are: {}".format(guess[i],game_vars.COLORS))
            return False

    return True

#Fix input
def input_fix(guess):
    guess = guess.upper().replace(" ", "").split()[0]
    guess = [*guess]

    return guess

#Check how many correct and incorrect guessed
def check_correct_incorrect(guess,code):
    return ([guess[i] == code[i] for i in range(game_vars.MAX_NUMBER_OF_GUESSED_COLORS)].count(True),
            [guess[i] == code[i] for i in range(game_vars.MAX_NUMBER_OF_GUESSED_COLORS)].count(False))

#Check if the guess is correct
def check_win(guess,guesses):
    if guess[0] == game_vars.CORRECTLY_GUESSED_NUMBER:
        print("Congratulations! It took you {} guesses, you win!".format(guesses))
        return True
    else:
        print("{} Correct | {} Incorrect".format(guess[0], guess[1]))
        return False

#Game loop
def guess_loop(code):
    guesses = game_vars.START_GUESS_COUNT
    while (guesses < game_vars.MAX_GUESSES):
        print("Enter your guess({}): ".format(guesses))
        guess = get_color_input()
        if check_win(check_correct_incorrect(guess,code),guesses):
            break
        guesses += 1


if __name__ == '__main__':
    guess_loop(generate_code())
