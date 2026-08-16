def shopping_list():
    purchases = []
    prices = []

    print('Type "-" to stop')
    i = 0

    while i == 0:
        purchased = str(input('What was purchased?: '))

        if purchased == '-':
            i += 1
            continue

        price = float(input('Enter the price: '))

        purchases.append(purchased)
        prices.append(price)

    return purchases, prices


def show_purchases(result):
    print('_' * 30)
    print(f'Item Purchased:               Price:')

    for j in range(0, len(result[0])):
        print(f'{result[0][j]:<30} $ {result[1][j]:.2f}')

    print('_' * 30)


def calculate_total(balance, prices):
    total_spent = sum(prices)
    remaining_balance = balance - total_spent

    return total_spent, remaining_balance


def menu():
    i = 0

    purchases = ([], [])
    prices = []

    print('=' * 30)
    print('EXPENSE CONTROL')
    print('=' * 30)

    while i == 0:

        choice = int(input(
            '[1] Add Items\n'
            '[2] Show Items\n'
            '[3] Balance\n'
            '[4] Exit\n'
        ))

        if choice == 1:
            purchases = shopping_list()
            prices = purchases[1]

        elif choice == 2:
            show_purchases(purchases)

        elif choice == 3:
            result = calculate_total(x, prices)

            print(f'Total spent: $ {result[0]:.2f}')
            print(f'Remaining balance: $ {result[1]:.2f}')

        elif choice == 4:
            print('Program closed!')
            i += 1


x = float(input('Enter your current balance: '))
menu()
