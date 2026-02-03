# Write a Python program named `sum_of_two_digits.py` that takes a string as input from the user. The string will consist of exactly two digits (e.g., "23", "98", "09"). Your program should calculate and output the sum of these two digits.

digits = (input('Enter two digits: '))
first_digit = int(digits[0])
second_digit = int(digits[1])
result = first_digit + second_digit
print(f'The sum of the two digits you provided is {result}.')

