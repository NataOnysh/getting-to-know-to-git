def calculate(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    return result


num1 = float(input('Enter first number: '))
operator = input('Enter operator (+,-,*): ')
num2 = float(input('Enter second number: '))

print(f"{num1} {operator} {num2} = {calculate(num1, operator, num2)}")
