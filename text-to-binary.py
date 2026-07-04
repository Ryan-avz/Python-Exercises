text = input("Enter a sentence: ")
text = text.replace(" ", "")

for letter in text:
    x = ord(letter)
    result = ""

    while x > 0:
        remainder = x % 2
        x = x // 2
        result = str(remainder) + result

    print(result)
