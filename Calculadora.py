# calculator variables
quest = input('Choose an arithmetic operator to use: ')

# THE AZTEC CALCULATOR

if quest == "*":
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    calc3 = (num1 * num2)
    print(calc3)

elif quest == "/":
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    calc4 = (num1 / num2)
    print(calc4)

elif quest == "-":
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    calc5 = (num1 - num2)
    print(calc5)

elif quest == "+":
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    calc6 = (num1 + num2)
    print(calc6)

else:
    arg = input('Are you really going to do this to me? ')

    while arg != 'no':
        print('nooooooooooooooooooooooooooooooooooooo')
        break

