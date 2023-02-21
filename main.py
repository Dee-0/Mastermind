#Mastermind game in console

import random
import GameVariables as game_vars

#Generate code to guess
def generate_code():
    code = []
    for i in range(game_vars.MAX_NUMBER_OF_GUESSED_COLORS):
        x = random.choice(game_vars.COLORS)
        code.append(x)
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

#Check amount of correct colors guessed
def check_correct_count(guess,code):
    correct = 0
    for i in range(game_vars.MAX_NUMBER_OF_GUESSED_COLORS):
        if guess[i] == code[i]:
            correct += 1

    return correct

#Check amount of incorrect colors guessed
def check_incorrect_count(guess,code):
    incorrect = 0
    for i in range(game_vars.MAX_NUMBER_OF_GUESSED_COLORS):
        if guess[i] != code[i]:
            incorrect += 1

    return incorrect

#Check if the guess is correct
def check_win(correct,incorrect,guesses):
    if correct == 4:
        print("Congratulations! It took you {} guesses, you win!".format(guesses))
        return True
    else:
        print("{} Correct | {} Incorrect".format(correct, incorrect))
        return False

#Game loop
def guess_loop(code):
    guesses = game_vars.START_GUESS_COUNT
    while (guesses < game_vars.MAX_GUESSES):
        print("Enter your guess({}): ".format(guesses))
        guess = get_color_input()
        guesses += 1
        if check_win(check_correct_count(guess, code),check_incorrect_count(guess, code),guess,code,guesses):
            break


if __name__ == '__main__':
    guess_loop(generate_code())
