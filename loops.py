# Using While Loops
# Using For Loops

# While loop is basically an IF statement on steroids


# while 13 < 88:
#     print("It works")



# Write a program that asks a user to type their password and confirm their password and if they are not the same, ask them again.

password = input("Enter password: ")
cpassword = input('Confirm password: ')

while password != cpassword:
    print("Incorrect password. \nTry again.")
    
    password = input("Enter password: ")
    cpassword = input('Confirm password: ')
else:
    print("Password accepted.")



name = input('Enter your name (min 4 chars): ')

while len(name) < 4:
    print("You entered a name less than 4 chars")
    name = input('Enter your name (min 4 chars): ')



# A while loop program that prints hello world 10 times
i = 0 
while i < 10: 
    print("Hello World!")
    i += 1


# A program that accepts somebody's name 12 times and replicates that name 2 times each
i = 0 

while i < 12: 
    name = input("Enter your name here: ")
    print(name * 2)
    i += 1



# A simple program that asks for 5 students names and stores them in a list
i = 0
students = []

while i < 5:
    student_name = input('Enter student name: ')
    students.append(student_name)
    i += 1

print(students)


# Write a program that accepts number ten times and stores each number into a list
i = 0
number_list = []

while i < 10:
    user_number = int(input('Enter your lucky number: '))
    number_list.append(user_number)
    i += 1
print(number_list)
print(f'Sum of your lucky numbers is {sum(number_list)}')


# A while loop that just counts from 1 - 50
i = 1 # initialization
while i <= 50:
    print(i)
    i += 1


# A program that asks the user to enter a number and then we generate numbers from 1 to that number
stop = int(input("Enter where to stop: "))
i = 1 # initialization
while i <= stop:
    print(i)
    i += 1


# A program that numbers 100 names 
i = 1
name = input('Enter student name: ')

while i <= 100:
    print(f'{i}. {name}')
    i += 1

# Print "Hello World" 3 times using a while loop
# i = 0
# while i < 3:
#     print('Hello World!')
#     i += 1

# 6x multiplication table
i = 1
while i <= 12:
    print(f'6 * {i} = {6 * i}')
    i += 1


# Print only even numbers from 2 to 10 (do not use += 2)
i = 2
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1


# Repeating processes using while True in python: break / continue
# Ask a user for their information: name, email, phone number, password/confirm password

# ***** Break keyword is used to STOP THE LOOP
# ***** Continue keyword is used to TAKE US BACK TO THE TOP OF THE LOOP


print("**************** USER REGISTRATION *****************")
while True:
    name = input("Name: ").strip()
    if len(name) >= 5:
        break

while True:
    name = input("Name: ").strip() 
    if len(name) < 5:
        print("Name is not up to 5 chars")
        continue
    else:
        break

while True:
    name = input("Name: ").strip() 
    if len(name) >= 5:
        break
    else:
        print("Name is not up to 5 chars")
        continue


while True:
    email = input("Email: ")
    if '@' not in email or '.' not in email:
        print("Email must contain both an @ and .")
        continue
    else:
        break


while True:
    phone = input("Phone Number: ").strip()
    if not phone.startswith(('+234', '0')) and (not len(phone) == 11 or not len(phone) == 15):
        print("Phone must start with +234 or 0 and must be either 11 digits or 15 digits")
        continue
    else:
        break



while True:
    password = input("Password: ").strip()

    if len(password) < 8:
        print("Password must be at least 8 chars")
        continue

    cpassword = input("Confirm Password: ").strip()


    if password != cpassword:
        print("Passwords do not match")
        continue

    else:
        break

print("Registration succesful")



# LOOPS CLASS 2

# Print numbers in reverse from 5 to 1 using a while loop.
i = 5
while i > 0:
    print(i)
    i -= 1

# Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
i = 1
while i <= 10:
    if i != 5:
        print(i)
    i += 1

# Print a square of stars
# Ask the user to enter a number
user_input = int(input('Enter a number: '))
i = 1
while i <= user_input:
    print('*' * user_input)
    i += 1


# Print a right angle triangle of stars
# Ask the user to enter a number
user_num = int(input('Enter a number: '))
i = 1
while i <= user_num:
    print('*' * i)
    i += 1


i = 5
while i >= 1:
    print('*' * i)
    i -= 1


# Print a countdown
# Ask the user to enter a number where they want to start the countdown from.
from time import sleep
countdown = int(input('Start countdown: '))
while countdown > 0:
    print(countdown)
    countdown -= 1
    sleep(1)
print('Go!')


# Print "1" ten times on the same line using a while loop
# Expected Output:
# 1111111111
i = 1
list_of_ones = []
while i < 11:
    list_of_ones.append('1')
    i += 1
print(''.join(list_of_ones))


# Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.
password = input('Enter the secret password: ')

while password != 'secret':
    print('Incorrect Password')
    password = input('Enter the secret password: ')
print('Password correct')

# OR

while True:
    password = input('Enter the secret password: ')
    if password == 'secret':
        print('Password correct')
        break
    else:
        print('Incorrect Password')
        continue



# ELSE block with while loop
# will only execute when the loop completes successfully
# executes ONLY WHEN THE LOOP DOES NOT EXECUTE ANY BREAK KEYWORD THROUGHOUT.
i = 6
while i >= -6:
    print(i)
    i -= 1
else:
    print('All done')


# Prime number program (divisible by 1 and itself)
prime_number = 15

i = 2
while i < prime_number:
    if prime_number % i == 0:
        print(f'{prime_number} is not a prime number')
        break
    i += 1
else:
    print(f'{prime_number} is a prime number')


# Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.
sentence = input('Enter a word: ').lower()

i = 0
vowel_count = 0
while i < len(sentence):
    if sentence[i] in 'aeiou':
        vowel_count += 1
    i += 1
print(vowel_count)


# Write a program that takes a string input from the user and uses a while loop to count the number of unique vowels (a, e, i, o, u) in the string.
sentence = input('Enter a word: ').lower()
unique_string = list(set(sentence))

i = 0
vowel_count = 0
while i < len(sentence):
    if sentence[i] in 'aeiou':
        vowel_count += 1
    i += 1
print(vowel_count)



# Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.

bank_balance = float(input('Enter your balance: '))

while True:
    withdrawal = float(input('Enter withdrawal amount: '))
    if withdrawal > bank_balance:
        print('Insufficient balance')
        continue
    else:
        bank_balance -= withdrawal
        print('Withdrawal succesful')
        print(f'Your new balance is {chr(8358)}{bank_balance:.2f}')

        retry_option = input('Would you like to make another withdrawal? (yes/no): ').lower()
        if retry_option == 'yes':
            continue
        elif retry_option == 'no':
            print('Thank you for banking with us.')
            break
        else:
            break



# Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.

total_cost = 0
while True:
    price = float(input('Enter item price: '))
    total_cost += price

    retry_option = input('Do you want to add another item? (yes/no): ').lower()
    if retry_option == 'yes':
        continue
    elif retry_option == 'no':
        print(f'Your total cost is {chr(8358)}{total_cost:.2f}')
        break

while True:
    fname = input('Enter your first name: ')
    lname = input('Enter your last name: ') 
    print(f'You full name is {fname} {lname}.')

    break

