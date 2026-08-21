def calculations(operator: str, a: float, b: float):
    if operator == '1':
        return a + b
    elif operator == '2':
        return a - b
    elif operator == '3':
        return a * b
    elif operator == '4':
        return a / b
    elif operator == '5':
        return a ** b


def menu():
    print('=' * 30)
    print()

    i = 0

    while i == 0:
        ask = input(
            'Mathematical Operator to be used:\n'
            '[1] - Addition\n'
            '[2] - Subtraction\n'
            '[3] - Multiplication\n'
            '[4] - Division\n'
            '[5] - Exponentiation\n'
            '[6] - Exit\n'
            '>>| '
        )

        if ask == '6':
            i += 1
            print('Calculation ended!')

        else:
            a = float(input('Enter a number: '))
            b = float(input('Enter another number: '))

            result = calculations(ask, a, b)

            print(f'Result: {result}')


menu()
