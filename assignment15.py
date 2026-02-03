# Write a function sum_numbers(a, b) that returns the sum of two numbers.

def sum_numbers(a: int | float, b: int | float) -> int | float:
    return a + b

print(sum_numbers(7.2, 5))


# Write a function is_even(n) that returns True if n is even and False if n is odd.

def is_even(n: int) -> bool:
    return n % 2 == 0

print(is_even(15))
print(is_even(12))

# def is_even(n: int) -> bool:
#     if n % 2 == 0:
#         return True
#     return False

# print(is_even(7))


# Write a function is_prime(n) that returns True if n is a prime number and False otherwise.

def is_prime(n: int) -> bool:
    if n <= 1:
       return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(29)) 


# Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.

def all_n_prime(n: int) -> list[int]:
    all_prime = [n for n in range(2, n + 1) if is_prime(n)]
    return all_prime

print(all_n_prime(int(input('Enter a whole number: '))))


# Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.

def lesser_of_two_evens(a: int | float, b: int | float) -> int | float:
    if a % 2 == 0 and b % 2 == 0:
        if a >= b:
            return b
        return a
    if a % 2 != 0 or b % 2 != 0:
        if a >= b:
            return a
        return b
    
print(lesser_of_two_evens(8, 90))


def lesser_of_two_evens(a: int | float, b: int | float) -> int | float:
    if a % 2 == 0 and b % 2 == 0:
        return min([a, b])
    return max([a, b])


# Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False

def is_alliteration(two_word_string: str) -> bool:
    splitted_str = two_word_string.split()
    return splitted_str[0][0].lower() == splitted_str[-1][0].lower()

print(is_alliteration('King Kong'))
print(is_alliteration('Scare crow'))


# Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.

def old_macdonald(name: str) -> str:
    mac = name[:3].capitalize()
    donald = name[3:].capitalize()
    return mac + donald

print(old_macdonald('macdonald'))


# Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False

def spy_game(list_of_ints: list[int]) -> bool:
    real_spy = [0, 0, 7, 'x']
    
    for _int in list_of_ints:
        if real_spy[0] == _int:
            real_spy.pop(0)
    return len(real_spy) == 1


def spy_game(list_of_ints: list[int]) -> bool:
    real_spy = [0, 0, 7]

    for _int in list_of_ints:
        if len(real_spy) != 0 and real_spy[0] == _int:
            real_spy.pop(0)
    return len(real_spy) == 0


# Write a function vol(radius) that computes the volume of a sphere given its radius.

def vol(radius: int | float) -> float:
    volume = (4 / 3) * (22 / 7) * (radius ** 3)  
    return f'{volume:.2f}cm3'

print(vol(4.2))


# Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).

def range_check(num: int, low: int, high: int) -> str:
    if num in range(low, high + 1):
        return f'{num} is within the range of {low}-{high}'
    return f'{num} is not in the given range'

print(range_check(3, 5, 10))


def range_check(num: int, low: int, high: int) -> str:
    return low <= num <= high

print(range_check(324, 243, 526))


# Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.

def upper_lower(text: str) -> str:
    upper_char_count = 0
    lower_char_count = 0

    for char in text:
        if char.isupper():
            upper_char_count += 1
        elif char.islower():
            lower_char_count += 1
    return f'There are {upper_char_count} uppercase and {lower_char_count} lowercase letters in {text}'

print(upper_lower('FiDDLe'))


# Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.

def unique_list(list_items: list[int]) -> list[int]:
    unique_elements = []
    for item in list_items:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements

print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# Write a function multiply(list_items) to multiply all the numbers in a list.
# 	Sample List: [1, 2, 3, -4]
# 	Expected output: -24

def multiply(list_items: list[int]) -> int:
    multiplied_list = 1
    for number in list_items:
        multiplied_list *= number
    return multiplied_list
        
print(multiply([1, 2, 3, -4]))   


from math import prod

def multiply(list_items: list[int]) -> int:
    return prod(list_items)

print(multiply([1, 2, 3, -4]))


#  14. 	Write a function is_pangram(text) to check whether a string is a pangram or not. 
# 	Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# 	least once. For example: “The quick brown fox jumps over the lazy dog”.
# 	Hint: Import and use the string module.

from string import ascii_lowercase

def is_pangram(text: str) -> bool:
    alphabets = set(ascii_lowercase)
    text_set = set(text.lower())
    return alphabets.issubset(text_set)

print(is_pangram('The quick brown fox jumps over the lazy dog'))

def is_pangram(text: str) -> bool:
    alphabets = ascii_lowercase

    for alphabet in alphabets:
        if alphabet not in text.lower():
            return False
    return True

print(is_pangram('The quick brown fox jumps over the lazy dog'))



#  15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# 	other. a word, phrase, or name formed by rearranging the letters of another, such as
# 	spar, formed from rasp.

def are_anagrams(s1: str, s2: str) -> bool:
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)

print(are_anagrams('rescue', 'secure'))
print(are_anagrams('silent', 'listen'))
print(are_anagrams('love', 'vile'))


#  16. 	Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# 	(BMI) given weight in kilograms and height in meters.

def calculate_bmi(weight: float, height: float) -> str:
    bmi = weight / (height ** 2)
    return f'Your Body Mass Index is {bmi:.2f}'

print(calculate_bmi(48.4, 1.66))


#  17. 	Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# 	simple interest given principal amount, interest rate, and time (in years).

def calculate_simple_interest(principal: int | float, rate: float, time: int) -> float:
    simple_interest = principal * (rate / 100) * time
    return simple_interest

print(calculate_simple_interest(3000, 7.5, 6))