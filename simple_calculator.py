# ======================= CALCULATOR PROGRAM =======================

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error: Zero cannot be denominator"


print(f'''
Welcome to the Simple Calculator
Select Operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
''')

choice = int(input('Enter your choice from 1 to 5: '))

if choice not in range(1, 6):
    print('Operation not recognized')
    exit()

num1 = float(input('Enter first number:'))
num2 = float(input('Enter second number:'))

if choice == 1:
    print(add(num1, num2))
elif choice == 2:
    print(subtract(num1, num2))
elif choice == 3:
    print(multiply(num1, num2))
elif choice == 4:
    print(divide(num1, num2))
elif choice == 5:
    print('Exiting Calculator')
    exit()
else:
    print('Operation not recognized')
    exit()