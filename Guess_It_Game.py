import random

green = "\033[32m"
red = "\033[31m"
reset = "\033[0m"
purple = "\033[38;5;141m"
cyan = "\033[36m"


def guessing_game(rounds):
    i = 0
    wins = 0
    losses = 0

    while i == 0:
        numbers = list(range(0, rounds + 1))
        random_number = random.choice(numbers)

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


def game_settings():
    difficulty = input(
        "Choose the difficulty:\n"
        "A - Easy\n"
        "B - Medium\n"
        "C - Hard\n"
        ">> "
    ).upper()

    gamemode = input(
        "Choose the game mode:\n"
        "A | One Round\n"
        "B | Best of Three\n"
        "C | Custom\n"
        ">> "
    ).upper()

    if gamemode == "A":
        rounds = 1
    elif gamemode == "B":
        rounds = 3
    elif gamemode == "C":
        rounds = int(input(f"Choose the {purple}number of rounds{reset}: "))

    if difficulty == "A":
        guessing_game(rounds)  # 20% chance of guessing correctly
    elif difficulty == "B":
        guessing_game(rounds)  # 10% chance
    elif difficulty == "C":
        guessing_game(rounds)  # 5% chance


game_settings()
