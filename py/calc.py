num1 = float(input('Enter a number! '))
operator = input('Enter an operator: ')
num2 = float(input("Enter a second Number: "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)   
else:
    print('Not available: ')


        