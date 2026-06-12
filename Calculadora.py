
i = 0
# THE AZTEC CALCULATOR
while i < 1:

 quest = input('| addition (+) \n'
               '| subtraction (-) \n'
               '| multiplication (*) \n'
               '| division (/) \n'
               'Choose an arithmetic operator to use: ')

 if quest == "*":
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    calc3 = (num1 * num2)
    print(calc3)
    i = int(input('0 : continue \n'
                  '1 : stop \n '))

 elif quest == "/":
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    calc4 = (num1 / num2)
    print(calc4)
    i = int(input('0 : continue \n'
                  '1 : stop \n '))

 elif quest == "-":
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    calc5 = (num1 - num2)
    print(calc5)
    i = int(input('0 : continue \n'
                  '1 : stop \n '))

 elif quest == "+":
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    calc6 = (num1 + num2)
    print(calc6)
    i = int(input('0 : continue \n'
                  '1 : stop \n '))

else:
    print('Stopped!')

