# A program that takes a number from a user and tells if it is an even or odd number
number = int(input('Enter an integer: '))

if number % 2 == 0:
    print(f'{number} is an EVEN number.')
else:
    print(f'{number} is an ODD number.')

# Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle"
angle1 = float(input('Enter Hypotenuse angle: '))
angle2 = float(input('Enter Opposite angle: '))
angle3 = float(input('Enter Adjacent angle: '))
valid_triangle = angle1 + angle2 + angle3

if valid_triangle == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print('Valid triangle')
else:
    print('Invalid triangle')

# An airport boarding system:
# The user enters boarding pass ("yes"/"no") and passport ("yes"/"no").
# - If both are "yes", print "Proceed to boarding".
# - If boarding pass is missing, print "No boarding pass".
# - If passport is missing, print "No passport".
# - If both missing, print "Denied entry".

boarding_pass = input('Do you have a Boarding pass?: ').lower()
passport = input('Do you have a Passport?: ').lower()

if boarding_pass == 'yes' and passport == 'yes':
    print('Proceed to boarding')
elif boarding_pass == 'no':
    print('No Boarding pass')
elif passport == 'no':
    print('No Passport')
else:
    print('Denied entry')


# A program that checks if the last character of a string from a user is a vowel or consonant 
from string import ascii_lowercase
sentence = input('Enter a word: ')
last_char = sentence[-1].lower()

if last_char in ascii_lowercase:
    if last_char in 'aeiou':
        print('This letter is a Vowel')
    else:
        print('This letter is a Consonant')
else:
    print(f'{last_char} is not an English alphabet')


# Write a program that tells us if a string is in uppercase form
string = input('Enter a string: ')
if string.isupper():
    print("It is all in uppercase")
else:
    print("It is NOT ALL in uppercase")


# A program that tells us if the last five letters of a string are palindromic

phrase = input("Enter a phrase: ").strip()
last_5_letters = phrase[-5:]
last_5_letters_reversed = last_5_letters[::-1]
if last_5_letters_reversed == last_5_letters:
    print(last_5_letters, 'is a palindrome')
else:
    print(last_5_letters, 'is not a palindrome')