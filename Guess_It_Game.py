import random

green = "\033[32m"
red = "\033[31m"
reset = "\033[0m"
purple = "\033[38;5;141m"
cyan = "\033[36m"

def game_settings():


    difficulty = input(
        "Choose the difficulty:\n"
        "A - Easy\n"
        "B - Medium\n"
        "C - Hard\n"
        ">>"
    ).upper()

    if difficulty == "A":
        limit = 5
        return limit  #20% chance of guessing correctly
    elif difficulty == "B":
        limit = 10
        return limit # 10% chance
    elif difficulty == "C":
        limit = 20
        return limit  # 5% chance
limit = game_settings()

def guessing_game(limit):
    i = 0
    wins = 0
    losses = 0

    while i == 0:

        random_number = random.randint(1, limit)
        guess = int(input("Which number did the computer choose? "))

        if guess == random_number:
            wins += 1
            print(f"{green}Correct!{reset} {cyan}[{wins}/3]{reset}")
        else:
            losses += 1
            print(f"{red}Wrong!{reset} {cyan}[{losses}/3]{reset}")

        if wins == 3:
            print("You Win!!")
            i += 1
        elif losses == 3:
            print("You Lose!!")
            i += 1

guessing_game(limit)
