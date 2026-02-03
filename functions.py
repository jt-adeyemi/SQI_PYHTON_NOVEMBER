# def add(num1, num2):
#     print(f'The sum of {num1} and {num2} is {num1 + num2}')

# add(5, 12)


# Write a function 'to_upper' that accepts a string called text and returns the upper case version of the text

# def to_upper(text):
#     return text.upper()

# print(to_upper('name\'s josh'))


# Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

# Output:
# ***
# ***
# ***

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****


# 1. Write 5 stars horizontally 5 times vertically

# length = int(input("Enter the length of the square: "))

# def square(length):
#     for _ in range(length):
#         print("*" * length)


# # square(7)
# # square(3)
# # square(9)



# square(int(input("Enter the length of the square: ")))
# square(int(input("Enter the length of the square: ")))
# square(int(input("Enter the length of the square: ")))

# DRY - Don't Repeat Yourself



# def greet_someone():
#     print("Hello someone! 👋")

# greet_someone()

# import time

# def greet_someone(name):
#     print(f"Hello {name}")
#     time.sleep(1)

# greet_someone("Winnie")
# greet_someone("Joshua")
# greet_someone("Racheal")


# def greet_someone(name, emoji):
#     print(f"Hello {name} {emoji}!")


# greet_someone("Winnie", "👀")
# greet_someone("Joshua", "👍🏾")
# greet_someone("Racheal", "👌🏽")




# def add_two_nums(number1, number2):
#     print(f"The sum of {number1} and {number2} is {number1 + number2}")

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# add_two_nums(num1, num2)


# # # add_two_nums(6, 7)

# def add_two_nums(number1, number2):
#     print("hello")
#     return f"The sum of {number1} and {number2} is {number1 + number2}"

# result = add_two_nums(6, 7)
# print(result)


# def greet():
#     print("Good afternoon, SQI Oct Python Gurus")  # 1
#     print("inside function")  # 2


# print(greet())


# def greet():
#     return "Good afternoon, SQI Oct Python Gurus", "inside function" 


# result1, result2 = greet()
# print(result1)
# print(result2)





# def greet():
#     print('Hello World!') # 1

# greet()
# print('Outside function')  # 2





# print("Lorem ipsum dolor")  # 1

# def greet():
#     print("sit amet")  # 3, 6
#     print('Hello World!')  # 4, 7

# print('tempor incididunt ut labore')  # 2
# greet()
# print("consectetur adipiscing elit")  # 5
# greet()
# print("Nemo enim ipsam voluptatem")  # 8




# print("The sun rises in the east")  # 1


# def greet():
#     print("How's it going?")  # 2, 5, 7, 10
#     print("Stay curious, stay kind.")  # 3, 6, 8, 11


# greet()

# print("Midnight thoughts and coffee sips")  # 4
# greet()
# greet()
# print("Learning never exhausts the mind")  # 9
# greet()
# print("Wander often, wonder always")  # 12








#----------------------------------------FUNCTIONS CONTD----------------------------------------------

def cube(a, b=1, c=4):  # Non-default, Default arguments
    return a ** 3

print(cube(2))  # Positional arguments
print(cube(2, b=4, c=10))  # Keyword arguments


# Arbitrary (vary in number) Arguments / Arbitrary Keyword Arguments

def sum_of_int(*args, **kwargs):
    print(sum(args))
    print(kwargs)

sum_of_int(2, 5, 3, 7, 7, 2, 2, 3, 5 ,7, 8, name='Ola', city='Los Angeles')


def format_user_data(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
            # OR
    for item in kwargs:
        print(f'{item} => {kwargs[item]}')

format_user_data(name='Joshua', middlename='Temi', lname='Adeyemi', course='MME', city='Changzou')


def random(a, b, *args):
    return a + b + sum(args)

print(random(4, 6, 4, 6, 7, 8, 5))
print(random(4, 6))


# Recursion
def power(base, exponent):
    if exponent == 0:  # Base case
        return 1
    else:
        return base * power(base, exponent - 1)  # Recursive call

print(power(5, 3))


# Scopes
local_var = 30
def my_function():
    local_var = 10  # Local scope
    print(local_var)

my_function()
print(local_var)


local_var = 30
def my_function():
    global local_var
    local_var = 10  # Local scope
    print(local_var)

my_function()
print(local_var)
# A variable defined in a function can only be accessed inside the function except using a global variable



# name = "Oluwatobi"
# course = "CSC"

# def get_user_info():
#     global name
#     global course

#     name = input('Enter a name: ')
#     course = input('Enter a course: ')


# print("************ User information ***********")

# print("Options: \n1. View data\n2. Change data")
# option = input('')

# if option == '1':
#     print(f"Name: {name}")
#     print(f"Course: {course}")
# elif option == '2':
#     get_user_info()

# print(f"Name: {name}")
# print(f"Course: {course}")








# user_data = {
#     'name': "Oluwatobi",
#     'course': "Computer Science"
# }

# def get_user_info(data):

#     name = input('Enter a name: ')
#     course = input('Enter a course: ')
#     data['name'] = name
#     data['course'] = course


# print("************ User information ***********")

# print("Options: \n1. View data\n2. Change data")
# option = input('')

# if option == '1':
#     print(f"Name: {user_data['name']}")
#     print(f"Course: {user_data['course']}")
# elif option == '2':
#     get_user_info(user_data)

# print(f"Name: {user_data['name']}")
# print(f"Course: {user_data['course']}")





# bank_account = {
#     'name': "Oluwatobi",
#     'bank_name': "Access",
#     'acct_no': 190988823,
#     'pin': "2222",
#     'balance': 23000
# }

# def transfer(user):
#     amt = float(input('How much do you want to transfer? '))
#     user['balance'] -= amt
#     print(f"{amt} transferred successfully. Your new balance is: {user['balance']}")



# print("************ UBA BANK **********")
# option = input("What do you want to do? withdraw, transfer: ")

# if option == 'transfer':
#     transfer(bank_account)

    




# 1. Create a function called get_total_length that returns the total number of characters in all the words passed in.

# Test Data:
# print(get_total_length("hi", "hello"))
# print(get_total_length("apple", "banana", "car"))

# def get_total_length(*args):
#     all_chars_joined = ''.join(args)
#     return len(all_chars_joined)

# print(get_total_length("apple", "banana", "car"))



# 2. Create a function called highest_score that returns the name of the student with the highest score.

# Test Data:
# print(highest_score(Ada=72, Bisi=89, Charles=67))
# print(highest_score(Emeka=90, Tolu=91, Zainab=88))
# [2, 4, 2, 1, 1, 12, 4, 34, 54, 43, 65]
# Expected Output:
# Bisi
# Tolu

# def highest_score(**kwargs):
#     # assuming that the first item in the dictionary is the highest
#     highest_score_data = list(kwargs.items())[0]
    
#     for key, value in kwargs.items():
#         if value > highest_score_data[1]:
#             highest_score_data = (key, value)
    
#     return highest_score_data

# print(highest_score(Ada=72, Bisi=89, Charles=67))



# Function to get the highest score from the dictionary WITHOUT the person's name
# def highest_score_without_name(**kwargs):
#     list_of_scores = list(kwargs.values())
#     highest = list_of_scores[0]
    
#     for score in list_of_scores:
#         if score > highest:
#             highest = score
    
#     return highest

# print(highest_score(Ada=72, Bisi=89, Charles=67))



# 3. Create a function called multiply_first_two that returns the product of the first two numbers passed in.

# Test Data:
# print(multiply_first_two(3, 5, 9, 2))
# print(multiply_first_two(10, 2, 7))

# Expected Output:
# 15
# 20

def multiply_first_two(*args):
    return args[0] * args[1]
print(multiply_first_two(3, 5, 9, 2, 7))


# 4. Create a function called describe_books that prints out each book title and its author.

# Test Data:
# describe_books(Hamlet="Shakespeare", ThingsFallApart="Chinua Achebe", Dune="Frank Herbert")
# describe_books(Matilda="Roald Dahl", 1984="George Orwell")

# Expected Output:
# Hamlet is written by Shakespeare
# ThingsFallApart is written by Chinua Achebe
# Dune is written by Frank Herbert
# Matilda is written by Roald Dahl
# 1984 is written by George Orwell

def describe_books(**kwargs):
    # Get both keys and values at once
    for book, author in kwargs.items():
        print(f"{book} is written by {author}")
    
    # Loop through only the keys first
    # for book in kwargs:
    #     print(f"{book} is written by {kwargs[book]}")

describe_books(Hamlet="Shakespeare", ThingsFallApart="Chinua Achebe", Dune="Frank Herbert")

    

