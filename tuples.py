# Creating an empty tuple
animes = ()

animes = ('demon slayer', 'jujutsu kaisen')
print(type(animes))

# Creating a tuple with one item
animes = (3000)
print(type(animes))
animes = (3000,)
print(type(animes))

# Swapping values using tuple
firstname = 'Tobi'
lastname = 'Dada'
firstname, lastname = (lastname, firstname)
print(firstname)
print(lastname)

# Tuple containing different data types
random_data = ('demon slayer', 107.5, None, 200, False, 388 > 94)
print(random_data)

# Tuple immutability
# new_programming_languages = ('Rust', 'Golang', 'Dart')
# new_programming_languages[0] = 'Nodejs'

# Converting a tuple to a list for mutability
new_programming_languages = ('Rust', 'Golang', 'Dart')
new_programming_languages = list(new_programming_languages)
new_programming_languages[0] = 'Nodejs'
new_programming_languages = tuple(new_programming_languages)
print(new_programming_languages)

# A program that accepts 3 items from the user, stores it in a tuple and then asks them how many times they want those items to be replicated in their tuple.
# tvshow1 = input('Enter a tv show: ')
# tvshow2 = input('Enter another tv show: ')
# tvshow3 = input('Enter another tv show: ')
# replica_no = int(input('How many times do you want to replicate them?: '))
# tvshows = (tvshow1, tvshow2, tvshow3)
# print(tvshows * replica_no)

# print('Would you like to add more tvshows?')
# tvshow4 = input('Enter a tv show: ')
# tvshow5 = input('Enter another tv show: ')
# tvshows = tvshows + (tvshow4, tvshow5)
# print(tvshows)

# Unpacking a tuple
shows = ('Suits', 'Vampire Dairies', 'Legacies')
series1, series2, series3 = shows
print(f"""
1. {series1}
2. {series2}
3. {series3}
""")

movies = [
    ['The Accountant 2', 2025, '1hr40mins'],
    ['Interstellar', 2019, '2hr30mins'],
    ['The Mechanic', 2015, '1hr02mins'],
    ['John Wick 4', 2012, '2hr35mins']
]
number_of_movies = len(movies)
print(f'We have {number_of_movies} movies available. Choose a number between 1 - {number_of_movies} and you will get the movie details.')

option = int(input('Enter a number: '))
selected_movie = movies[option - 1]

movie_name, year, duration = selected_movie

print(f'Movie Name: {movie_name}\tYear: {year}\tDuration: {duration}')

# Unpacking selected items in a tuple
languages = ('Spanish', 'English', "Yoruba", 'Portuguese', 'Swahili')
spanish, engish, *others = languages
print(spanish)
print(engish)
print(others)
_, _, yoruba, *others = languages

fruits = ('apple', 'mango', 'pawpaw', 'pineapple', 'cherry')
green, *tropic, yellow, red = fruits

data = (('Alice', 'Bob'), ('Math', 'Physics'), (90, 85))
students, *_ = data
student1, student2 = students
print(student2)

# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.
record = ('Jane', (32, 'Manager'), ['HR', 'Finance'])
name, (age, position), (dept1, dept2) = record
print(age, dept1)

# Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.
inventory = (('apples', 50), ('bananas', 100), ('cherries', 75))
(fruit_one, quantity1), (fruit_two, quantity2), (fruit_three, quantity3) = inventory
print(f'The quantity of {fruit_two} in the inventory is {quantity2}.')
