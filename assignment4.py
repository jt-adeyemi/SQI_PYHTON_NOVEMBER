# Write a program that asks the user for their name and then greets them with their name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
user_name = input('Enter your name: ').title()
print(f'Hello, {user_name}!')

# Ask the user for their birth year and calculate their age. Print the user's age in the format “You are {age} years old.”.
birth_year = int(input('Enter your birth year: '))
age = 2025 - birth_year
print(f'You are {age} years old.')

# Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.
favorite_color = input('Enter you favorite color: ').capitalize()
print(f'Your favorite color is {favorite_color}.')

# Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`. Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.
word = input('Enter any word or phrase: ')
stripped_word = word.lower().replace(' ', '')
reversed_word = stripped_word[::-1]
is_palindrome = stripped_word == reversed_word
print(f'It is {is_palindrome} that {word} is a palindrome.')

# Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.
user_weight = float(input('Enter your weight (in kg): '))
user_height = float(input('Enter your height (in meters): '))
body_mass_index = user_weight / (user_height ** 2)
print(f'Your BMI is {body_mass_index:.2f}')