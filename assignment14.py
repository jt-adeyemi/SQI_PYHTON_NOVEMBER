# # -----------------------------------------ASSIGNMENT 1-----------------------------------------------

# # 6. Is there any name that contains the letter 'a'?
# # Input: ["John", "Sara", "Mike", "Amanda"]
# # Expected Output: True
# names = ["John", "Sara", "Mike", "Amanda"]

# any_has_a = any('a' in name.lower() for name in names)
# print(any_has_a)


# # 7. Are all the words made up of only uppercase letters?
# # Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# # Expected Output: False
# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]

# is_all_upper = all(word.isupper() for word in greetings)
# print(is_all_upper)


# # 8. Is there any word that starts with 'z'?
# # Input: ["apple", "zebra", "mango", "lemon"]
# # Expected Output: True
# words = ["apple", "zebra", "mango", "lemon"]

# is_any_first_char_z = any(word.lower().startswith('z') for word in words)
# print(is_any_first_char_z)


# # 9. Is there any email address that contains ".org"?
# # Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# # Expected Output: True
# emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]

# any_has_dot_org = any('.org' in email.lower() for email in emails)
# any_has_dot_org = any(email.lower().endswith('.org') for email in emails)
# print(any_has_dot_org)


# # 10. Are all numbers odd?
# # Input: [1, 3, 5, 7, 9]
# # Expected Output: True
# values = [1, 3, 5, 7, 9]

# is_all_odd = all(value % 2 != 0 for value in values)
# print(is_all_odd)


# # 11. Are all words longer than 2 characters?
# # Input: ["hi", "dog", "go", "sun"]
# # Expected Output: False
# words = ["hi", "dog", "go", "sun"]

# is_all_len_over_2 = all(len(word) > 2 for word in words)
# print(is_all_len_over_2)


# # 12. Create a list of triple the value of each number
# # Input: [2, 4, 6, 8]
# # Expected Output: [6, 12, 18, 24]
# nums = [2, 4, 6, 8]

# num_by_3 = [num * 3 for num in nums]
# print(num_by_3)


# # 13. Are all temperatures above 0°C?
# # Input: [12, 7, 3, -1, 5]
# # Expected Output: False
# temperatures = [12, 7, 3, -1, 5]

# is_all_temp_over_0 = all(temp > 0 for temp in temperatures)
# print(is_all_temp_over_0)


# # 14. Do all words end with a vowel?
# # Input: ["banana", "mango", "kiwi", "grape"]
# # Expected Output: True
# fruits = ["banana", "mango", "kiwi", "grape"]
# vowels = ('a', 'e', 'i', 'o', 'u')

# is_all_last_char_vowel = all(fruit[-1].lower() in vowels for fruit in fruits)
# print(is_all_last_char_vowel)


# # 15. Create a list of words in lowercase
# # Input: ["HELLO", "WORLD", "PYTHON"]
# # Expected Output: ["hello", "world", "python"]
# greetings = ["HELLO", "WORLD", "PYTHON"]

# words_in_lower = [word.lower() for word in greetings]
# print(words_in_lower)


# # 16. Is there any number less than 0?
# # Input: [5, -2, 3, 0, 8]
# # Expected Output: True
# numbers = [5, -2, 3, 0, 8]

# is_any_less_than_0 = any(number < 0 for number in numbers)
# print(is_any_less_than_0)


# # 17. Create a list of words that contain the letter 'e'
# # Input: ["sky", "tree", "rock", "stone"]
# # Expected Output: ["tree", "stone"]
# items = ["sky", "tree", "rock", "stone"]

# e_in_word = [item for item in items if 'e' in item.lower()]
# print(e_in_word)


# # 18. Are all names starting with uppercase letters?
# # Input: ["Alice", "Bob", "charlie", "David"]
# # Expected Output: False
# names = ["Alice", "Bob", "charlie", "David"]

# is_all_first_char_upper = all(name[0].isupper() for name in names)
# print(is_all_first_char_upper)


# # 19. Is there any sentence longer than 20 characters?
# # Input: ["Short one", "This is a much longer sentence", "Okay"]
# # Expected Output: True
# sentences = ["Short one", "This is a much longer sentence", "Okay"]

# is_any_len_over_20 = any(len(phrase) > 20 for phrase in sentences)
# print(is_any_len_over_20)






# # -----------------------------------------ASSIGNMENT 2-----------------------------------------------
# # 1. Create a function called turn_to_upper(names) that takes in a list of names, and returns a list of names uppercased
# # after, print the result of the function.
# # For example, if names is ["Winifred", "Wilfred", "Justin", "Augusta"], the result would be [ "WINIFRED", "WILFRED", "JUSTIN", "AUGUSTA"]
# def turn_to_upper(names):
#     names = 
   
# print(turn_to_upper(["Winifred", "Wilfred", "Justin", "Augusta"]))


# # 2. Create a function called get_middle_name that accepts one paramter `name_dict` that takes in a dictionary with keys "first", "middle", and "last".
# # The function should return only the middle name.
# # For example, if name_dict is {"first": "Tola", "middle": "James", "last": "Akin"}, then the result would be "James". Another example is if name_dict is {"middle": "Chioma", "first": "Ada", "last": "Okeke"}, the result would be "Chioma".
# def get_middle_name(name_dict):
#     name_dict = {"first": "Tola", "middle": "James", "last": "Akin"}
#     return name_dict["middle"]

# print(get_middle_name('middle'))

# # 3. Create a function called reverse_string that accepts a string as input and returns the string reversed.
# # For example, if the string is "Python", the result would be "nohtyP".
# def reverse_string(string):
#     return string[::-1]

# print(reverse_string('word'))

# # 4. Create a function called count_vowels that accepts a string and returns the number of vowels (a, e, i, o, u) in it.
# # For example, if the string is "beautiful", the result would be 5.
# def count_vowels(string):
#     vowels = ('a', 'e', 'i', 'o', 'u')
#     vowel_count = 0
#     for char in string:
#         if char.lower() in vowels:
#             vowel_count += 1
#     return vowel_count

# print(count_vowels('beautiful'))

# 5. Create a function called even_numbers that takes in a list of integers and returns a new list containing only the even numbers.
# For example, if the list is [1, 2, 3, 4, 5, 6], the result would be [2, 4, 6].
def even_numbers(integers):
    even_numbers = [number for number in integers if number % 2 == 0]
    return even_numbers

print(even_numbers([1, 2, 3, 4, 5, 6]))

# 6. Create a function called find_max that takes in a list of numbers and returns the maximum number in the list.
# For example, if the list is [12, 45, 3, 67, 23], the result would be 67.
def find_max(numbers):
    return max(numbers)

print(find_max([12, 45, 3, 67, 23]))


# 7. Create a function called sum_dict_values that takes in a dictionary with numeric values and returns the sum of all the values.
# For example, if the dictionary is {"a": 10, "b": 20, "c": 5}, the result would be 35.
def sum_dict_values(value_sum):
    return sum(value_sum.values())

print(sum_dict_values({"a": 10, "b": 20, "c": 5}))  


# 8. Create a function called word_lengths that takes in a list of words and returns a dictionary where each word is a key and its length is the value.
# For example, if the list is ["apple", "banana", "cherry"], the result would be {"apple": 5, "banana": 6, "cherry": 6}.
# def word_lengths(words):


# print(word_lengths(["apple", "banana", "cherry"]))

# 9. Create a function called is_palindrome that takes in a string and returns True if the string is a palindrome (same forwards and backwards), otherwise False.
# For example, if the string is "level", the result would be True. If the string is "hello", the result would be False.
def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(is_palindrome('hello'))


# 10. Create a function called merge_lists that takes in two lists and returns one combined list without duplicates.
# For example, if list1 = [1, 2, 3] and list2 = [3, 4, 5], the result would be [1, 2, 3, 4, 5].
def merge_lists(list_1, list_2):
    unique_list = list(set(list_1 + list_2))
    return unique_list

print(merge_lists([1, 2, 3], [3, 4, 5]))


# 11. Create a function called multiply_numbers(a, b=2) that multiplies two numbers.
# If the second number is not provided, it should default to 2.
# Example 1: multiply_numbers(5) → 10
# Example 2: multiply_numbers(5, 3) → 15
def multiply_numbers(a, b=2):
    return a * b

print(multiply_numbers(5, 3))


# 12. Create a function called greet_user(first_name, last_name="") that returns a greeting string.
# If last_name is not provided, it should only greet with the first name.
# Example 1: greet_user("Ada") → "Hello, Ada!"
# Example 2: greet_user("Tola", "Akin") → "Hello, Tola Akin!"
def greet_user(first_name, last_name=""):
    return f'Hello, {first_name} {last_name}!'

print(greet_user('Tola', 'Akin'))
print(greet_user('Ada'))


# 13. Create a function called power(base, exponent=2) that raises the base to the power of the exponent.
# The exponent should default to 2 (square).
# Example 1: power(4) → 16
# Example 2: power(2, 3) → 8
def power(base, exponent=2):
    return base ** exponent

print(power(4))
print(power(2, 3))


# 14. Create a function called format_full_name(first, middle="", last="") that returns the full name as a single string.
# If middle or last is not provided, it should still work correctly.
# Example 1: format_full_name("John", "Paul", "Smith") → "John Paul Smith"
# Example 2: format_full_name("Ada", last="Okeke") → "Ada Okeke"
# def format_full_name(first, middle="", last=""):
#     return f'{first} {middle} {last}'

# print(format_full_name("John", "Paul", "Smith"))
# print(format_full_name(middle="Paul", last="Smith"))
# print(format_full_name("Ada", last="Okeke"))


# 15. Create a function called calculate_discount(price, discount=10, tax=0) that calculates the final price after applying
# a discount (percentage) and then adding tax (percentage).
# Example 1: calculate_discount(100) → 90.0   (10% discount, no tax)
# Example 2: calculate_discount(200, discount=20, tax=5) → 168.0
# def calculate_discount(price, discount=10, tax=0):

def calculate_discount(price, discount=10, tax=0):
    discounted_price = price - (price * (discount / 100))
    price_total = discounted_price + (discounted_price * (tax / 100))
    return price_total

print(calculate_discount(100))
print(calculate_discount(200, discount=20, tax=5))
