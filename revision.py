# Write a program that accepts 5 numbers as keys in a dictionary and then the word version of that number as value. E.g. 25: "twenty-five". Display what yo have in the dictionary when done.
# numbers_with_spelling = {}
# for i in range(5):
#     number = int(input(f'Enter number {i + 1}: '))
#     number_spelling = input(f'Enter number {i + 1} in word: ')

#     numbers_with_spelling[number] = number_spelling
# print(numbers_with_spelling)


# Write a program that randomly creates a food combination from these three lists:
from random import choice

food_lists1 = ['Pizza', 'Jollof rice', 'Sushi', 'Shawarma', 'Fried chicken']
food_lists2 = ['Ice cream', 'Chocolate cake', 'Doughnuts', 'Brownies']
food_lists3 = ['Mango', 'Apple', 'Banana', 'Pineapple', 'Watermelon']

food_combination1 = choice(food_lists1)
food_combination2 = choice(food_lists2)
food_combination3 = choice(food_lists3)

print(f'You should take {food_combination1} in the morning, {food_combination2} in the afternoon, and top it with {food_combination3} in the evening.')

# A program that prints every number between 10 and 200 using a for loop

# for i in range(10, 201):
#     print(i)

# A program that prints every even number between 10 and 200

# for i in range(10, 201):
#     if i % 2 == 0:
#         print(i)

# A program that prints every multiple of 8 between 1 and 300

# for i in range(1, 301):
#     if i % 8 == 0:
#         print(i)


# names = ['Aliko', 'James', 'Mighty', 'Benny', 'Raven', 'Tobi']
# names_without_a = []
# names_with_o = []

# for name in names:
#     if 'a' not in name.lower():
#         names_without_a.append(name)
#     if 'o' in name.lower():
#         names_with_o.append(name)

# print(names_without_a)
# print(names_with_o)


# A program that takes 10 numbers from the user and then stores them as keys and their values will be the cube of each number. E.g. 10: 1000, 2: 8
# numbers_with_cube = {}

# for i in range(10):
#     number = int(input('Enter a number: '))
#     number_cube = number ** 3
#     numbers_with_cube[number] = number_cube

# print(numbers_with_cube)


# A program that stores a list of random animals and then gives us a list of only animals that have a name that has even-length.

# animals = ['Lion', 'Mosquito', 'Cheetah', 'Leopard', 'Tiger', 'Hippopotamus', 'Octopus', 'Shark', 'Elephant', 'Liger']
# animals_with_even_length = []

# for animal in animals:
#     if len(animal) % 2 == 0:
#         animals_with_even_length.append(animal)

# print(animals_with_even_length)


# words = ['refer', 'bale', 'errant', 'mom', 'fan', 'null', 'nun', 'none', 'deed', 'feel']
# palindromic_words = []

# for word in words:
#     is_palindrome = word == word[::-1]

#     if is_palindrome:
#         palindromic_words.append(word)

# print(palindromic_words)


programming_languages = [
    {'question': 'What is the result of True + True in Python?', 'options': 'a. Error b. False c. 2 d. True', 'answer': 'c'},
    {'question': 'Who is the Author of Python Language?', 'options': 'a. Elon Musk b. Guido Van Rossum c. Dennis Ritchie d. Donald Trump', 'answer': 'b'}
]

for question in programming_languages:
    print(question['question'])
    print(question['options'])

    user_answer = input('Enter your answer: ')

    if user_answer == question['answer']:
        print('Correct answer!!')
    else:
        print('Wrong answer.')
    


# data = {
#     'games': ['Deadpool 3', 'Devil May Cry', 'Mortal kombat', 'Assassin Creed', 'Real Football'],
#     'films': ['Game of Thrones', 'Creed II', 'Fallout', 'Lone Wolf', 'The Incredibles'],
#     'sports': ['Football', 'Hockey', 'Racing', 'Basketball', 'Tennis', 'Hiking']
# }

# print(list(data.keys()))
# user_choice = input('Enter your preference: ').lower()

# if user_choice not in data:
#     print(f'{user_choice} is not a valid category')
#     exit()

# selected_category = data[user_choice]

# for item in selected_category:
#     print(item)