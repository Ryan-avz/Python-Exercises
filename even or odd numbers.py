def evenOdd_check(x: int):
    if x % 2 == 0:
        return True
    if x % 2 == 1:
        return False
choice = 0

while choice != 1:
    num = int(input('Number: '))

    if evenOdd_check(num):
        print("Even!")
    else:
        print("Odd!")

    choice = int(input('1 to stop, 0 to continue: '))

print("Stopped!")
