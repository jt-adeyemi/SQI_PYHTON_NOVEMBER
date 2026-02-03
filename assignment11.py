# Collect two numbers as input from the user and assign as variables, a and b, write an if statement that prints "a and b are both positive" if both a and b are positive, prints "Only one is positive" if one of them is positive, and prints "Neither is positive" if neither is positive.
a = float(input('Enter first number: '))
b = float(input('Enter second number: '))

if a > 0 and b > 0:
    print('a and b are both positive')
elif a > 0 or b > 0:
    print('Only one is positive')
else:
    print('Neither is positive')


# Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.
numbers = input('Enter three numbers separated by comma: ').strip().replace(' ', '').split(',')
x = int(numbers[0])
y = int(numbers[1])
z = int(numbers[-1])

if x == y == z:
    print('All same')
elif x <= y <= z:
    print('Increasing order')
elif z >= y >= x:
    print('Decreasing order')
else:
    print('Neither')


# Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
palindrome = input('Enter a word: ').lower().replace(' ', '')
reversed_palindrome = palindrome[::-1]

if palindrome == reversed_palindrome:
    print('Is a palindrome')
else: 
    print('Not a palindrome')

# You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.
x = int(input('Enter a number: '))
y = int(input('Enter a number: '))
z = int(input('Enter a number: '))

if x == y == z:
    print('All same')
elif x == y or x == z or y == z:
    print('Two are equal')
else:
    print('All different')


# You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.
from string import ascii_lowercase
ch = input('Enter an alphabet: ').lower()
vowel = ('a', 'e', 'i', 'o', 'u')

if ch in ascii_lowercase and ch in vowel:
    print('Vowel')
elif ch in ascii_lowercase and ch not in vowel:
    print('Consonant')
else:
    print('Not an alphabet')


# Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".
colors = input('Enter the three primary colors separated by comma: ').lower().replace(' ', '').split(',')
colors = set(colors)
primary_colors = {'red', 'blue', 'yellow'}

if colors == primary_colors:
    print('All primary colors')
else:
    print('Not all primary colors') 


# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".
print('Modes available: manual, automatic, off')
mode = input('Select mode: ').lower()

if mode == 'manual':
    print('Manual mode activated')
elif mode == 'automatic':
    print('Automatic mode activated')
elif mode == 'off':
    print('System is off')
else:
    print('Wrong mode. Try again')


# Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".
# sentence = "Hi, Tobi, please, we urgently need you to deal with something for us at the Church."
# if "urgent" in sentence or "important" in sentence
message = input('Enter your message here: ')

if 'urgent' in message or 'important' in message or 'immediate' in message:
    print('High priority message')
else:
    print('Normal message')


# You have two variables, status1 and status2, provided through user input, each of  which can be "active", “inactive", or "pending". Write an if statement to print  "Both active" if both statuses are "active", "One active" if exactly one is "active", and "None active" if neither is "active".
print('Available status: active, inactive, pending')
status1 = input('Enter your stage one status: ').lower()
status2 = input('Enter your stage two status: ').lower()

if status1 == 'active' and status2 == 'active':
    print('Both active')
elif status1 == 'active' or status2 == 'active':
    print('One active')
else:
    print('None active')


# Given a string `filename` supplied by the user, write an if statement to check if the filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise print "Not an image file".
filename = input('Enter your file name with its format: ').lower()
file_formats = ('.jpg', '.png', '.gif')
if filename.endswith(file_formats):
    print('Image file')
else:
    print('Not an image file')


# You have a variable `access_level` provided through user input which can be "admin", "user", or "guest". Write an if statement that prints "Full access" if access_level is "admin", "Limited access" if it is "user", and "No access" if it is "guest".
access_level = input('Enter your access level: ').lower()

if access_level == 'admin':
    print('Full access granted')
elif access_level == 'user':
    print('Limited access granted')
else:
    print('No access granted')


# Given a string `email` collected from the user, write an if statement to check if the email contains both "@" and "." characters. Print "Valid email" if it does, otherwise print "Invalid email".
email = input('Please enter your email address: ')

if '@' in email and '.' in email:
    print('Valid email')
else:
    print('Invalid email')