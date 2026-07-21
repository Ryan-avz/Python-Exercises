import random

options = ['Rock', 'Paper', 'Scissors']
matches = int(input('How many matches do you want to play? '))

red = "\033[31m"
end = "\033[m"

for i in range(matches):

    choice = int(input(
        'Choose your move:\n'
        '[0] Rock\n'
        '[1] Paper\n'
        '[2] Scissors\n'
        '--> '
    ))

    player_move = options[choice]
    computer_move = random.choice(options)

    print(f'I choose {computer_move}!!!!!!')

    if player_move == computer_move:
        print(f'{red}Draw{end}')
    elif player_move == options[0] and computer_move == options[1]:
        print(f'{red}Computer wins{end}')
    elif player_move == options[0] and computer_move == options[2]:
        print(f'{red}Player wins{end}')
    elif player_move == options[1] and computer_move == options[0]:
        print(f'{red}Player wins{end}')
    elif player_move == options[1] and computer_move == options[2]:
        print(f'{red}Computer wins{end}')
    elif player_move == options[2] and computer_move == options[0]:
        print(f'{red}Computer wins{end}')
    elif player_move == options[2] and computer_move == options[1]:
        print(f'{red}Player wins{end}')
