number = int(input('First: '))
number1 = int(input('Second: '))
number2 = int(input('thirt: '))

if number == number1 == number2:
    print(3)
elif number == number1 or number == number2 or number1 == number2:
    print(2)
else:
    print(0)