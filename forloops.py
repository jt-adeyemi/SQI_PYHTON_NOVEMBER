# A for loops that gives us numbers from 1-10
# for i in range(1, 11):
#     print(i)

# for i in range(6): # range(start, end, step)
#     print(i)

# A for loop that prints numbers with a step(3)
# for i in range(1, 101, 3):
#     print(i)

# A for loop program that prints even numbers from 4 to 80
# for i in range(4, 81, 2):
#     print(i)

# A for loop program that prints even numbers from 5 to 80
# for i in range(5, 81):
#     if i % 2 == 0:
#         print(i)


# A program that asks the user for value of a and b 12 times and always print the addition of both values
# for i in range(12):

#     a = float(input('Enter value of a: '))
#     b = float(input('Enter value of b: '))
#     print(f'{a} + {b} = {a + b}')


# 2x multiplication table using for loop
# for i in range(1, 12):
#     print(f'2 x {i} = {i * 2}')

# A for loop that goes in descending order
# for i in range(20, 0, -1):
#     print(i)


# fruit = 'Avocado'
# for i in range(len(fruit)):
#     print(fruit[i] * 2, end='')
# print()


# country = 'Hungary'
# for i in range(len(country)):
#     print(country[-1])


# FOR EACH LOOP IN PYTHON

# country = 'Hungary'
# for letter in country:
#     print(letter)


# student_names = ['Tolu', 'Tobi', 'Tayi', 'Tade', 'Tife']
# student_names_in_uppercase = []
# for name in student_names:
#     student_names_in_uppercase.append(name.upper())
# print(student_names_in_uppercase)


countries = ['USA', 'Canada', 'Brazil', 'China', 'Finland', 'Switzerland', 'England', 'Australia']
for index, country in enumerate(countries, start=1):
    print(index, country)


# employees = ['Leroy Sane', 'Rico Lewis', 'John Stones', 'David Luiz', 'Josh King']
# for index, employee in enumerate(employees, start=101):
#     print(f'ID{index}: {employee}')



# A for loop program that creates a list of only cities with 'a' from an existing list
# cities = ['Lagos', 'Abuja', 'Kano', 'Ibadan', 'Benin City']
# cities_with_a = []
# for city in cities:
#     if 'a' in city:
#         cities_with_a.append(city)
# print(cities_with_a)


# A for loop program that creates a list of only cities with even number of chars from an existing list
# cities = ['Lagos', 'Abuja', 'Kano', 'Ibadan', 'Benin City']
# cities_with_even = []
# for city in cities:
#     if len(city) % 2 == 0:
#         cities_with_even.append(city)
# print(cities_with_even)
        


# Collect a phrase from the user and use a loop to generate an acronym by taking the first
# 	letter of each word. Print the acronym. Example:
# 	Input: "Portable Network Graphics"
# 	Output: "PNG"
# print('********************* ACRONYM GENERATOR *********************')
# sentence = input('Enter a sentence: ').split()
# acronym = []

# for word in sentence:
#     acronym.append(word[0].upper())
# print('.'.join(acronym))



# capitals = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'Australia': 'Canberra', 'Egypt': 'Cairo'}
# for country in capitals:
#     print(f"Country: {country}")

# for capital in capitals.values():
#     print(f"Capital: {capital}")



# name = input('Enter your name: ')
# for letter in name:
#     print(letter * len(name), end='')
# print()
    


# actions = ['walk', 'run', 'stop', 'jump']
# for x in actions:
#     print(x)
#     if x == 'stop':
#         break


# from time import sleep
# actions = ['on your marks', 'set', 'ready', 'go!!']

# for action in actions:
#     print(action)
#     sleep(2)