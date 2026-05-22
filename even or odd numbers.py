num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
result = int(((num1+num2)**4)/2)
if result % 2 == 0:
    print(f'O número {result} é par!')
else:
    print(f'o número {result} é impar!')
