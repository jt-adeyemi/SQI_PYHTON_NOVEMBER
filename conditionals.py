
# If statements [if..elif..else]
# Match-case statements

# if 30 > 1 * 35: # then
#     print('30 is actually greater than 0')

# else:
#     print('What is in the \'if\' block is not true. So we have this.')
# print('Program finished')


# num = int(input('Enter a number: '))
# if num > 10:
#     print(f'{num} is greater than 10')
# else:
#     print(f'{num} is less than 10')


# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))

# if num1 != 0 and num2 != 0:
#     print('Both numbers are not zero')
# else:
#     print('Both or one of them is zero')


# A program that takes an age from the user and then tells them if they are eligible to vote or not.
# age = int(input('Please enter your age: '))
# if age >= 18:
#     print(f'You are eligible to vote.')
# else:
#     print(f'Sorry, you are not eligible to vote.')


# wild_animals = ['cheetah', 'rhino', 'lion', 'jaguar', 'crocodile']
# animal = input('Enter your favourite animal: ')

# if animal in wild_animals:
#     print(f'Your favourite animal is a wild animal')
# else:
#     print(f'Your favourite animal is a domestic animal')


# Write a program that asks the user to provide a password and then tell if the password is valid or not, depending on whether it has at least 8 characters or not.
# password = input('Enter password: ').strip()
# if len(password) >= 8:
#     print(f'Password is valid.')
# else:
#     print(f'Invalid password! Try again.')
#     input('Enter password: ').strip()


# Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".

# word = input('Enter a word: ').lower().replace(' ', '')
# reversed_word = word[::-1]

# if word == reversed_word:
#     print('Is a palindrome')
# else: 
#     print('Not a palindrome')


# Salary System
# level = int(input('Enter your level: '))
# if level >= 1 and level <= 7:
#     print(f'Your salary is: {chr(8358)}80,000')
# elif level >= 8 <= 10:
#     print(f'Your salary is: {chr(8358)}100,000')
# elif level in range(11, 17):
#     print(f'Your salary is: {chr(8358)}250,000')
# elif level >= 17:
#     print(f'Your salary is: {chr(8358)}400,000')
# else:
#     print('Not a valid level.')


# A program that checks if the range of a number is between 1 and 20
number = float(input('Enter a number: '))
if number in range(1, 21):
    print(f'{number} is within the range of 1-20')
else:
    print('Not in range')


# A program that tells if a number is a multiple of 5 and 2
# num = int(input('Enter a number: '))
# if num % 5 == 0 and num % 2 == 0:
#     print(f'{num} is a multiple of both 5 and 2')
# else:
#     print(f'{num} is NOT multiple of both 5 and 2')




# Number guessing game program
# import random
# computer_number = random.randint(1, 10)
# if computer_number % 2 == 0:
#     print('HINT: The number is an EVEN number from 1 to 10')
# else:
#     print('HINT: The number is an ODD number from 1 to 10')
# user_guess = int(input('Guess the number: '))

# if computer_number == user_guess:
#     print('Congratulations! You have won the game.')
# else:
#     print('Sorry, you can try again later. Anyways, computer\'s number was:', computer_number)


# Guess the Color game
import random
colors = [
    "Red", "Blue", "Green", "Yellow", "Black",
    "White", "Orange", "Purple", "Pink", "Brown",
    "Gray", "Cyan", "Magenta", "Lime", "Navy",
    "Teal", "Olive", "Maroon", "Silver", "Gold",
    "Beige", "Coral", "Indigo", "Violet", "Turquoise",
    "Chocolate", "Ivory", "Lavender", "Peach", "Mint",
    "SkyBlue", "DarkBlue", "LightBlue", "DarkRed", "LightGreen",
    "ForestGreen", "SeaGreen", "HotPink", "Salmon", "Crimson",
    "Tan", "Aqua", "Amber", "Rose", "Plum",
    "Khaki", "Bronze", "Copper", "Mustard", "Burgundy",
    "Sand", "Charcoal", "Lilac", "Cream", "JetBlack",
    "RoyalBlue", "BabyBlue", "SunsetOrange", "MidnightBlue", "SlateGray",
    "AppleGreen", "ArmyGreen", "WineRed", "SkyGray", "PastelPink",
    "PastelGreen", "PastelBlue", "Marigold", "Jade", "Ruby"
]

computer_color = random.choice(colors).lower()
# Choose two random letters from the randomly selected colors to show as HINT
two_letter_hint = random.sample(computer_color, 2) 

print("HINT: ", two_letter_hint, 'are two letters in that color')
user_guess = input('Guess the color: ').lower()

if computer_color == user_guess:
    print('Wow!!! That is correct!!!')
else:
    print("Incorrect guess. Try again. The answer was:", computer_color)




# Building a simple user login system in Python
from getpass import getpass
from time import sleep
user = {
    'username' : "tobi",
    'password': 'password'
}

print('*********** ACCESS BANK LOGIN *************')

username = input('Username: ')
password = getpass("Password: ", echo_char = '*')

if username == user['username'] and password == user['password']:
    print("Login successful")
    print("Redirecting to dashboard...")
    sleep(2)
    print('WELCOME, ', user['username'])
elif username == user['username'] and password != user['password']:
    print("Password is incorrect")
else:
    print("Sorry, invalid details")





# Quiz app with questions, options, and answers

from random import choice
from time import sleep
quiz_questions = [
    {"question": "Who created the Python Language?", "options": "a. Guido Van Rossum, b. James Gosling, c. Dennis Ritchie", "answer": "c"},

    {"question": "An empty string converted to a an int in python results in?", "options": "a. 0, b. -1, c. Error", "answer": "c"}
]

selected_quiz_question = choice(quiz_questions)

print(selected_quiz_question['question'])
print(selected_quiz_question['options'].replace(', ', '\n'))

# ORRRRR

splited_question_answers = selected_quiz_question['options'].split(', ')
print('\n'.join(splited_question_answers))

user_answer = input("Your answer: ")

if user_answer == selected_quiz_question['answer']:
    sleep(1)
    print("Wow! You are correct")
else:
    sleep(1)
    print("Wrong answer. The correct answer is:", selected_quiz_question['answer'])




# The pass keyword in python says "do nothing"
if 300 > 883:
    # I will do this later
    pass # Do nothing




# A user provides a continent and a country in that continent. Then you tell them the population of that country

# continent = input('Enter continent: ').lower()
# country = input('Enter country: ').lower()

# if continent == 'africa' and country == 'nigeria':
#     print("Nigerian Population: 200million")
# elif continent == 'africa' and country == 'ghana':
#     print("Ghanian population is: 40million")
# elif continent == 'africa' and country == 'cameroon':
#     print("Cameroon population is: 50million")
# elif continent == 'asia' and country == 'japan':
#     print("Japan's population is: 70million")
# elif continent == 'asia' and country == 'china':
#     print("China's population is: 1.3billion")
# elif continent == 'asia' and country == 'india':
#     print("India's population is: 1.2billion")
# elif continent == 'oceania' and country == 'australia':
#     print("Australia's population is 30million")
# elif continent == 'oceania' and country == 'new zealand':
#     print("New Zealand population is: 10million")
# elif continent == 'europe' and country == 'uk':
#     print("UK's population is: 100million")
# elif continent == 'europe' and country == 'italy':
#     print("Italy's population is: 100million")
# elif continent == 'europe' and country == 'ukraine':
#     print("Ukraine's population is: 200million")
# elif continent == 'europe' and country == 'belgium':
#     print("Belgium's population is: 700million")
# elif continent == 'europe' and country == 'austria':
#     print("Austria's population is: 10million")
# elif continent == 'europe' and country == 'germany':
#     print("Germany's population is: 10million")
# elif continent == 'europe' and country == 'france':
#     print("France's population is: 300million")
# else:
#     print("Sorry, this data is not available.")




# USING NESTED IF STATEMENTS

continent = input('Enter continent: ').lower()
country = input('Enter country: ').lower()

if continent == 'africa': 
    if country == 'nigeria':
        print("Nigerian Population: 200million")
    elif country == 'ghana':
        print("Ghanian population is: 40million")
    elif country == 'cameroon':
        print("Cameroon population is: 50million")
    
elif continent == 'asia':
    if country == 'japan':
        print("Japan's population is: 70million")
    elif country == 'china':
        print("China's population is: 1.3billion")
    elif  country == 'india':
        print("India's population is: 1.2billion")

elif continent == 'oceania':
    if country == 'australia':
        print("Australia's population is 30million")
    elif country == 'new zealand':
        print("New Zealand population is: 10million")

elif continent == 'europe':
    if country == 'uk':
        print("UK's population is: 100million")
    elif country == 'italy':
        print("Italy's population is: 100million")
    elif country == 'ukraine':
        print("Ukraine's population is: 200million")
    elif country == 'belgium':
        print("Belgium's population is: 700million")
    elif country == 'austria':
        print("Austria's population is: 10million")
    elif country == 'germany':
        print("Germany's population is: 10million")
    elif country == 'france':
        print("France's population is: 300million")
else:
    print("Sorry, this data is not available.")


