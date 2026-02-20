def calculator():
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    else:
        print("INVALID, TRY AGAIN")

print('--------------Calculator----------------')
number1 = int(input('Enter first number: '))
operator = input('Enter operator (+ - * /): ')
number2 = int(input('Enter second: '))

result = calculator()
print (result)