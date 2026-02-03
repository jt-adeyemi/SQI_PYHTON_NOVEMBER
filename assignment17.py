# Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.

class NegativeNumberError(Exception):
    def __init__(self, message="Input is less than zero"):
        self.message = message
        super().__init__(self.message)


def check_positive(num):
    if num < 0:
        raise NegativeNumberError
   

try:
    number = int(input('Enter a number: '))
    check_positive(number)

except ValueError:
    print("Value should be an integer")
except NegativeNumberError as ex:
    print(ex)
except Exception as ex:
    print(ex)


# Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.

def safe_divide(a, b):
    return a / b


try:
    a = float(input('Enter your Numerator: '))
    b = float(input('Enter your Denominator: '))
    print(safe_divide(a, b))
except ZeroDivisionError:
    print('Error! Cannot divide numerator by zero')
except (TypeError, ValueError):
    print('Error! Enter a valid number')
except Exception as e:
    print(e)

       # OR

def safe_divide(a, b):

    try:
        a = float(input('Enter your Numerator: '))
        b = float(input('Enter your Denominator: '))
        return a / b
    except ZeroDivisionError:
        print('Error! Cannot divide numerator by zero')
    except (TypeError, ValueError):
        print('Error! Enter a valid number')
    except Exception as e:
        print(e)
    return 0

print(safe_divide(a, b))