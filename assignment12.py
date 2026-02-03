# Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# n = int(input('What number would you like to stop?: '))
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1
# Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# base = int(input('Enter the base number: '))
# exponent = int(input('Enter the exponent number: '))
# result = 1
# i = 1
# while i <= exponent:
#     result = result * base
#     i += 1
# print(f'{base} raised to the power of {exponent} is {result}')
    

# Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.
# string = input('Enter a word: ').lower()

# i = 0
# vowel_count = 0
# while i < len(string):
#     if string[i] in 'aeiou':
#         vowel_count += 1
#     i += 1
# print(vowel_count)

# Write a program that takes a string input from the user and uses a while loop to reverse the string.
# Do not use slicing or reversed().
# string = input('Enter a word or phrase: ')
# rev_string = []
# i = len(string) - 1
# while i >= 0:
#     rev_string.append(string[i])
#     i -= 1
# print(''.join(rev_string))

# 	Write a program that takes comma-separated integers from the user, converts that to a tuple and uses a while loop to find the minimum value in the tuple. Do not Use the min() function.
# numbers = tuple(input('Enter your numbers separated by commas: ').strip().replace(' ', '').split(','))

# i = 0
# lowest = int(numbers[0])
# while i < len(numbers):
#     if int(numbers[i]) < lowest:
#         lowest = int(numbers[i])
#     i += 1
# print(f'min value is {lowest}')
    

#  Write a program that takes a string input from the user and uses a while loop to count the occurrences of each character, storing the counts in a dictionary.
# 	Sample Input:
# 	Enter a string: Hello
# 	Sample Output:
# 	{‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}
# user_word = input('Enter your statement: ').lower().replace(' ', '')
# set_of_letters = list(set(user_word))
# letter_count = {}
# i = 0
# while i < len(set_of_letters):
#     letter_count[set_of_letters[i]] = user_word.count(set_of_letters[i])
#     i += 1
# print(letter_count)


# Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.
while True:
    password = input("Password: ").strip()

    if len(password) < 8 or len(password) > 25:
        print("Password must be at least 8 characters long and have a maximum of 25 characters")
        continue
    else:
        print('Password accepted')
        break



# Write a program that asks for the user's age and keeps prompting them until they enter a valid age (greater than or equal to 0).

while True:
    age = int(input('Please enter your age: '))
    if age < 0:
        print('Invalid age. Please enter a valid age.')
        continue
    else:
        print('Age accepted.')
        break


# Write a program that tracks the inventory of items in a store. The user should be able to add or remove items and the program should display the current inventory after each operation. The program stops when the user decides to exit.
# The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# 	Sample Input and Output:
# 	Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit

inventory = {}

while True:
    operation = input('Enter operation (add/remove/exit): ')
    if operation == 'exit':
        print('Thank you for your patronage')
        break
    elif operation == 'add':
        item_name = input('Enter item: ')
        item_qty = int(input('Enter quantity: '))
        
        inventory[item_name] = item_qty
        print(f'Current inventory: {inventory}')
    elif operation == 'remove':
        item_name = input('Enter item: ')
        if item_name in inventory:
            inventory.pop(item_name)
            print(f'{item_name} removed successfully')
        else:
            print(f'{item_name} does not exist')
    else:
        print('Option must be either add, remove or exit')
        
# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:

base = int(input('Enter a number to see the multiplication table: '))
i = 1
while i <= 12:
    print(f'{base} * {i} = {base * i}')
    i += 1