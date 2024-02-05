from random import randint
from art import logo

easy_level = 10
hard_level = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too hight!")
        return turns -1
    elif guess < answer:
        print("Too low!")
        return turns -1
    else:
        print(f"U got it! THe answer was {answer}")


def set_difficultlly():
    level = input("Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return easy_level
    else:
        return hard_level

def game():
    print(logo)
    print("Welcome to the game!")
    print("I'm thinking about 1 and 100: ")
    answer = randint(1, 100)
    turns = set_difficultlly()
    guess = 0
    while guess != answer:
        print(f"{turns} turns u have!")
        guess = int(input("Make a guess: !"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("U lose!")
            return
        else:
            print("Guess again!")
game()

