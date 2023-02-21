#Mastermind game in console

import random

colors = ['W','R','O','G','B','Y'] # White, Red, Orange, Green, Blue, Yellow

#Generate code to guess
def generate_code():
    code = []
    for i in range(4):
        x = random.choice(colors)
        code.append(x)
    print("{}".format(code))
    return code

#Check if correct guess entered
def check_input_validity(guess):
    for i in range(4):
        if guess[i] not in colors:
            print("{} is not a correct choice, correct choices are: {}".format(guess[i],colors))
            return False
    return True

#Fix input
def input_fix(guess):
    guess = guess.upper()
    guess = guess.split()
    guess = guess[0]
    guess = [*guess]
    return guess

#Check amount of correct colors guessed
def check_correct(guess,code):
    correct = 0
    for i in range(4):
        if guess[i] == code[i]:
            correct += 1
    return correct

#Check amount of incorrect colors guessed
def check_incorrect(guess,code):
    incorrect = 0
    for i in range(4):
        if guess[i] != code[i]:
            incorrect += 1
    return incorrect

#Check if the guess is correct
def check_win(correct,incorrect,guess,code,guesses):
    if correct == 4:
        print("Congratulations! It took you {} guesses, you win!".format(guesses))
        return True
    else:
        print("{} Correct | {} Incorrect".format(check_correct(guess, code), check_incorrect(guess, code)))
        return False

#Game loop
def guess_loop(code):
    guesses = 1
    while (guesses < 10):
        print("Enter your guess({}): ".format(guesses))
        guess = input()
        guess = input_fix(guess)
        while (len(guess) != 4 or check_input_validity(guess) is False):
            print("Bad input, please re-enter: ")
            guess = input()
            guess = input_fix(guess)
        guesses += 1
        if check_win(check_correct(guess, code),check_incorrect(guess, code),guess,code,guesses):
            break


if __name__ == '__main__':
    guess_loop(generate_code())
