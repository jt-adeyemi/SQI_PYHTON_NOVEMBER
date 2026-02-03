# Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters). Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`. Bonus point if you can hide the password input from displaying on the screen as clear text.
import getpass
password = getpass.getpass('Enter your password: ', echo_char = '*')
has_8_characters_min = len(password) >= 8
has_30_characters_max = len(password) <= 30
is_valid = has_8_characters_min and has_30_characters_max
print(f'It is {is_valid} that the password fulfills the criteria.')

# Write a program for a mad libs game. You can find the printable version at https://bit.ly/mad-libs-president.
name = input('Enter your full name: ').title()
age = int(input('Enter your age: '))
adjective1 = input('Enter an adjective: ')
color = input('Enter a color: ')
noun1 = input('Enter a noun: ')
food_type = input('Enter a type of food: ')
noun2 = input('Enter a noun: ')
verb = input('Enter a verb: ')
clothing_item = input('Enter a clothing headwear: ')
adjective2 = input('Enter an adjective: ')
celebrity = input('Enter the name of a celebrity: ')
number = int(input('Enter a number: '))
friend_name1 = input('Enter a friend\'s name: ')
noun3 = input('Enter a noun: ')
friend_name2 = input('Enter a friend\'s name: ')
occupation = input('Enter an occupation: ')

print('         IF I WERE PRESIDENT...          ')
print(f'''My name is {name} and I am {age} years old. If I were
president, I'd do a whole bunch of {adjective1} things:
1.  I would drive the biggest {color} car in the country. And that
    car would go faster than any other {noun1} in the world!
2.  Everyone would eat pepperoni {food_type}s for dinner.
3.  I would live in the Statue of {noun2} and build a 
    {verb} pool at her feet.
4.  I would wear a/an {clothing_item} on my head, and
    everyone would say I look {adjective2} like {celebrity}.
5.  School would be open only {number} days a year.
6.  I would give my friends the best jobs. I would nominate
    {friend_name1} to be secretary of (the) {noun3}, and 
    {friend_name2} could be vice {occupation}!''')

# Write a program for a mad libs game. You can find the printable version at https://bit.ly/mad-libs-asking-someone-out.
endearment_term = input('Enter an endearment term: ')
first_name = input('Enter a first name: ').capitalize()
last_name = input('Enter a surname: ').title()
place = input('Enter a location: ')
day_of_the_week = input('Enter any day of the week: ')
adjective = input('Enter an adjective: ')
color = input('Enter a color: ')
clothing_item = input('Enter a cloth item: ')
number = int(input('Enter a number: '))
verb1 = input('Enter a verb: ')
verb2 = input('Enter another verb: ')
verb3 = input('Enter another verb: ')
verb4 = input('Enter another verb: ')

print('         ASKING SOMEONE OUT          ')
print(f'''Hey, {endearment_term}. It's me. What's up? You know,
{first_name}. {first_name} {last_name}. From the
{place}. Two {day_of_the_week}s ago. I was the {adjective} guy
in the {color} parachute {clothing_item}. I paid the bus boy
{number} dollars to {verb1} me your information. I was
wondering if maybe you'd like to {verb2} out with me. Please don't
call the {verb3} department. Alright, I'll {verb4}. So, that's a
no, right?''')

# A program that accepts three values for a, b, c and solves it as a quadratic equation.
#PEMDAS
coefficient_a = float(input('Enter the value for a: '))
a = coefficient_a
coefficient_b = float(input('Enter the value for b: '))
b = coefficient_b
coefficient_c = float(input('Enter the value for c: '))
c = coefficient_c

x1 = ((- b) + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
x2 = ((- b) - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)

print(f'x = {x1:.2f} or x = {x2:.2f}')