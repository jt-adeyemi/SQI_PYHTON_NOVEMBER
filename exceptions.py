# Write a program that takes two numbers and divides the first by the second number  

number1 = float(input('Enter your first number: '))
number2 = float(input('Enter your second number: '))

division = number1 / number2

print(division)


# Write a program that has a dictionary {'uname': 'josh', 'pword': 'josh007', 'email': 'josh@josh.com'} and then accept a key from the user. Then delete that item from the dictonary and display the new data.

details = {'username': 'josh', 'password': 'jorshh', 'email': 'josh@sqi.com'}
print(details)

wrong_detail = input('Which detail is incorrect?: ').lower()

del details[wrong_detail]

new_details = details
print(new_details)


# Error and Exception Handling

# try:
#     # the code that may throw an error
# except # type of error:
#     # what to do after the error occurs


details = {'username': 'josh', 'password': 'jorshh', 'email': 'josh@sqi.com'}
print(details)

wrong_detail = input('Which detail is incorrect?: ').lower()

try:
    del details[wrong_detail]

    new_details = details
    print(new_details)
except KeyError:
    print('The detail you provided does not exists')
except Exception:
    print('An error has occured. Try again.')


try:
    num1 = int(input('First Num: ')) # ValueError
    num2 = int(input('Second num: '))

    print(num1 / num2)
except ValueError:
    print("The value you provided is not supported.")
except ZeroDivisionError:
    print("Second number must not be zero")
except KeyboardInterrupt:
    print("Program exited")
    exit()
except Exception:
    print("An error has occured... You can check later.")

print("Program finished.")


# Program rewritten with simpler try-except

try:
    num1 = int(input('First Num: ')) # ValueError
    num2 = int(input('Second num: '))

    print(num1 / num2)
except ZeroDivisionError:
    print("The second num must not be zero")
except Exception:
    print("An error has occured... You can check later.")


try:
    num1 = int(input('First Num: ')) # ValueError
    num2 = int(input('Second num: '))

    print(num1 / num2)
except (ZeroDivisionError, ValueError):
    print("Inputs must be integers and second number must not be zero")
except Exception:
    print("An error has occured... You can check later.")




users = ["Tobi", "Dada", "John", "Kevin", "Null"]

try:
    user_index = int(input(f'Choose an index from 0 - {len(users) -1}: '))
    print(users[user_index])
except ValueError:
    print("You must provide only numbers ")
except IndexError:
    print("The value provided is outside the range")
except Exception:
    print("An error occured. Please try again later.")



while True:
    try:
        age = int(input("Please enter your age: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for your age.")


try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to execute if ZeroDivisionError occurs
    print("Cannot divide by zero.")
except Exception as e:
    # Code to execute for any other exception
    print(f"An error occurred: {e}")
else:
    # Code to execute if no exception occurs
    print("Operation successful.")
finally:
    # Code that always executes, regardless of exceptions
    print("Execution completed.")






users = ["Tobi", "Dada", "John", "Kevin", "Null"]

class UserDoesNotExist(Exception):
    def __init__(self, message="This user does not exist"):
        self.message = message
        super().__init__(self.message)


print("********** GET USER AND DUPLICATE *********** ")
username = input('Provide user name: ')

try:
    if username not in users:
        raise UserDoesNotExist
except UserDoesNotExist as ex:
    print(ex)
    exit()

replication_times = int(input('Enter number of times to replicate: '))

print(username * replication_times)




class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds in the account"):
        self.message = message
        super().__init__(self.message)


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise InsufficientFundsError(f"Attempted to withdraw ${amount}, but only ${self.balance} available.")

        self.balance -= amount
        print(f"Withdrew ${amount}. New balance is ${self.balance}.")


josh = BankAccount(10_000_000)
try:
    josh.deposit(-344)
except ValueError as e:
    print(e)
except InsufficientFundsError as e:
    print(e)
except Exception as e:
    print(e)