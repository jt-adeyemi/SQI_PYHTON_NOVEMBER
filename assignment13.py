# --------------------------------LIST COMPREHENSION & GENERATORS EXERCISES--------------------------------
# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
digits = [1, 2, 3, 4, 5]

digits_squared = [digit ** 2 for digit in digits]
print(digits_squared)

# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]
names = ["John", "Sara", "Mike", "Amanda"]

names_with_a = [name for name in names if 'a' in name.lower()]
print(names_with_a)


# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
values = [5, 12, 3, 18, 7]

is_greater_than_10 = [value > 10 for value in values]
print(is_greater_than_10)


# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
animals = ["dog", "cat", "lion", "tiger"]

animals_last_char = [animal[-1] for animal in animals]
print(animals_last_char)


# 5. Create a list of triple the value of each number
# Input: [2, 4, 6, 8]
# Expected Output: [6, 12, 18, 24]
nums = [2, 4, 6, 8]

nums_tripled = [num * 3 for num in nums]
print(nums_tripled)


# 6. Create a list of numbers doubled only if they are even
# Input: [1, 2, 3, 4, 5, 6]
# Expected Output: [4, 8, 12]
numbers = [1, 2, 3, 4, 5, 6]

doubled_even_num = [number * 2 for number in numbers if number % 2 == 0]
print(doubled_even_num)


# 7. Create a list of the lengths of each word
# Input: ["apple", "banana", "cherry"]
# Expected Output: [5, 6, 6]
fruits = ["apple", "banana", "cherry"]

fruits_length = [len(fruit) for fruit in fruits]
print(fruits_length)


# 8. Create a list of numbers converted to strings
# Input: [10, 20, 30]
# Expected Output: ["10", "20", "30"]
scores = [10, 20, 30]

num_strings = [str(score) for score in scores]
print(num_strings)


# 9. Create a list of words converted to uppercase
# Input: ["python", "java", "go"]
# Expected Output: ["PYTHON", "JAVA", "GO"]
languages = ["python", "java", "go"]

upper_lang = [language.upper() for language in languages]
print(upper_lang)


# 10. Create a list of numbers greater than the average of the list
# Input: [2, 4, 6, 8, 10]
# Expected Output: [8, 10]
from statistics import mean
values = [2, 4, 6, 8, 10]

num_greater_than_avg = [number for number in values if number > mean(values)]
num_greater_than_avg = [number for number in values if number > (sum(values) / len(values))]
print(num_greater_than_avg)


# 11. Create a list of the first characters of each name
# Input: ["Alice", "Bob", "Charlie"]
# Expected Output: ["A", "B", "C"]
people = ["Alice", "Bob", "Charlie"]

name_first_char = [name[0] for name in people]
print(name_first_char)


# 12. Create a list of numbers multiplied by their index
# Input: [3, 5, 7]
# Expected Output: [0, 5, 14]
nums = [3, 5, 7, 2, 3]

# for i, number in enumerate(nums):
#     print(i, number)

num_x_index = [number * i for i, number in enumerate(nums)]
print(num_x_index)


# 13. Create a list of words that have more than 4 characters
# Input: ["car", "house", "tree", "mountain"]
# Expected Output: ["house", "mountain"]
objects = ["car", "house", "tree", "mountain"]

char_greater_than_4 = [_object for _object in objects if len(_object) > 4]
print(char_greater_than_4)


# 14. Create a list of Booleans indicating if each word starts with a vowel
# Input: ["apple", "banana", "orange", "pear"]
# Expected Output: [True, False, True, False]
words = ["apple", "banana", "orange", "pear"]
vowel = ('a', 'e', 'i', 'o', 'u')

is_first_char_vowel = [fruit.startswith(vowel) for fruit in words]
print(is_first_char_vowel)


# 15. Create a list of squares of numbers that are odd
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 9, 25]
digits = [1, 2, 3, 4, 5]

odd_squared = [digit ** 2 for digit in digits if digit % 2 == 1]
print(odd_squared)


# 16. Create a list of the reversed version of each word
# Input: ["dog", "cat", "bat"]
# Expected Output: ["god", "tac", "tab"]
animals = ["dog", "cat", "bat"]

reversed_animal = [animal[::-1] for animal in animals]
print(reversed_animal)


# 17. Create a list of numbers that are divisible by both 2 and 3
# Input: [3, 4, 6, 8, 9, 12]
# Expected Output: [6, 12]
nums = [3, 4, 6, 8, 9, 12]

divisible_by_2_and_3 = [number for number in nums if number % 2 == 0 and number % 3 == 0]
divisible_by_2_and_3 = [number for number in nums if number % 6 == 0]
print(divisible_by_2_and_3)


# 18. Create a list of words with their lengths as tuples
# Input: ["pen", "notebook", "eraser"]
# Expected Output: [("pen", 3), ("notebook", 8), ("eraser", 6)]
items = ["pen", "notebook", "eraser"]

items_with_length = [(item, len(item)) for item in items]
print(items_with_length)


# 19. Create a list that flattens a list of lists
# Input: [[1, 2], [3, 4], [5]]
# Expected Output: [1, 2, 3, 4, 5]
matrix = [[1, 2], [3, 4], [5]]

# for list in matrix:
#     for list in list:
#         print(list)

matrix_list = [_list for _list in matrix for _list in _list]
print(matrix_list)


# 20. Create a generator that yields the square of each number one at a time
# Input: [2, 3, 4]
# Expected Output when iterated: 4, 9, 16
nums = [2, 3, 4]

num_squared = (number ** 2 for number in nums)
# print(num_squared)
for number in num_squared:
    print(number)