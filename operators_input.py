num1 = 7777
num2 = 5225

print('{} + {} = {}'.format(num1, num2, num1 + num2))
print('{} * {} = {}'.format(num1, num2, num1 * num2))
print('{} - {} = {}'.format(num1, num2, num1 - num2))

name = input('Enter your name: ')
state = input('Enter your state: ')
age = input('Enter your age: ')
print(f'Your name is {name}, you are {age} years old and you are from {state}.')


first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
address = input('Enter your address: ')
print(f'My name is {first_name} {last_name} and I live at {address}.')

## Kilogram to pounds converter
kilogram = float(input('Enter weight in kg: '))
kg_to_lbs = 2.2

pounds_result = kilogram * kg_to_lbs
print(f'{kilogram}kg = {pounds_result:.3f}lbs')

# # Arithmetic operators: +, -, *, /, %, **, //
num1 = 10
num2 = 2
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2) # Float division
print(num1 % num2) # Modulus operator (remainder operator)
print(num1 ** num2) # Exponent operator (raised to power)
print(num1 // num2) # Floor division

## Assignment operators: =, +=, -=, *=, /=, %=, //=
current_year = 2025
age = int(input('Enter year of birth: '))
current_year -= age
print(f'You are {current_year} years old.')

## Age predictor
birth_year = int(input('Enter your birth year: '))
age = 2025 - birth_year
print(f'You are {age} years old.')

## Comparison operators: >, <, >=, <=, ==, !=
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
is_equal = num1 == num2
print(f'It is {is_equal} that {num1} = {num2}')

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
is_greater = num1 > num2
print(f'It is {is_greater} that {num1} is greater than {num2}')

word = input('Enter a word: ').lower()
reversed_word = word[::-1]
is_palindrome = reversed_word == word ## Checking for palindrome
print(f'It is {is_palindrome} that \'{word}\' is a palindrome')


# # Logical operators: and, or, not
# A program that tells us if a number is divisible by 3 and 5
num = int(input('Enter a number: '))
is_divisible_by_3 = num % 3 == 0
is_divisible_by_5 = num % 5 == 0
print(is_divisible_by_3 and is_divisible_by_5)

is_multiple_of_3_and_5 = num % (3 * 5) == 0
print(is_multiple_of_3_and_5)

string = input('Enter a word: ')
string_length = len(string)
has_even_length = string_length % 2 == 0
starts_with_b = string[0] == 'b'
print(has_even_length or starts_with_b)

# Password validator
# has valid length (min 8 and max 32)
# cannot all be letters or numbers

password = input('Enter your password: ')
has_valid_length = len(password) >= 8 and len(password) <= 32
not_all_lower = not password.islower()
not_all_upper = not password.isupper()
print(has_valid_length)
print(not_all_lower)
print(not_all_upper)
print(has_valid_length and not_all_lower and not_all_upper)

# # Membership operators: in, not in
church = 'Mountain of fire'.lower()
print('of' in church)
print('z' not in church)

phrase1 = input('Enter a word or phrase: ')
phrase2 = input('Enter a word or phrase: ')
phrase3 = input('Enter a word or phrase: ')

has_phrase1_last_letter = phrase1[-1] in phrase2
has_phrase2_last_letter = phrase2[-1] in phrase3

all_valid_phrase_patterns = has_phrase1_last_letter and has_phrase2_last_letter
print(f'It is {all_valid_phrase_patterns} that all three phrases has the last letter of the previous phrase in them.')

# # Identity operators: is, is not
name = None
print(name is not None)
print(name is None)

# A program that converts seconds to minutes and seconds
seconds = int(input('Enter number of seconds: '))
minutes = seconds // 60
remaining_seconds = seconds % 60
print(f'{seconds}s = {minutes}minutes {remaining_seconds}seconds')


# PEMDAS - Parenthesis, Exponent, Multiplication, Division, Addition, Subtraction