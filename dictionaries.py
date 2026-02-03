names = {'firstname': 'Tobi', 'surname': 'Dada', 'middlename': 'John'}
print(names)
print(type(names))
print(len(names))
print(names['firstname'])

full_name = f'{names["firstname"]} {names["middlename"]} {names["surname"]}'
print(f'Hi there, my name is {full_name}')

# A contact book demo
contacts = {
    'Johnson': '080488598893',
    'Alice': '090874738953',
    'Bruno': '081734848093'
}
print(contacts['Alice'])

# Adding a  new contact (item) to the contact book (dictionary)
contacts['Khalid'] = '070646734678'
print(contacts)

# Deleting an item from the contact
del contacts['Alice']
print(contacts)

# Allowing a user to specify the contact they want to delete
# print(contacts)
# contact_name = input('Enter the contact name: ').capitalize()
# del contacts[contact_name]
# print(f'{contact_name} deleted successfully')

# Dictionary with different key data types
cities_zip  = {
    101410: 'Ikorodu',
    200323: 'Ibadan',
    '200323': 'Ibadan',
    120.457: 'Lagos'
}
print(cities_zip['200323'])
print(cities_zip[200323])

car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1994
}
# FORD      MUSTANG     1994
print(f'{car["brand"]}\t\t{car["model"]}\t\t{car["year"]}'.upper())

# Dictionary Methods
# Get
continent_population = {
    'africa': '3b',
    'asia': '2b',
    'europe': '1b',
    'antartica': '1k'
}
print(continent_population.get('asia'))
print(continent_population.get('asians', 'continent not found'))

# Adding a new continent (key) and population (value)
continent_name = input('Enter continent name: ').strip().lower()
population = input('Enter continent population: ').strip()
continent_population[continent_name] = population
print(continent_population)


print(continent_population.setdefault('south_america'))
print(continent_population.setdefault('north_america', '2b'))
print(continent_population)

# Getting all keys in a dict
print(continent_population.keys())

# Getting all values in a dict
print(continent_population.values())

# Updating a dictionary
other_continent_data = {
    'south_america': '4b',
    'north_america': '2m'
}
continent_population.update(other_continent_data)
print(continent_population)

# Removes a specific item in a dict using its key
car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1994
}
print(car.pop('year'))

# Removes a random item in the dict
print(car.popitem()) # returns a tuple of the dict


cars = {
    "Toyota": {
        "Sedan": ["Camry", "Corolla", "Avalon"],
        "SUV": ["RAV4", "Highlander", "4Runner"]
    },
    "Ford": {
        "Sedan": ["Fusion", "Taurus"],
        "SUV": ["Escape", "Explorer", "Expedition"]
    },
    "BMW": {
        "Sedan": ["3 Series", "5 Series", "7 Series"],
        "SUV": ["X1", "X3", "X5"]
    }
}

print(cars["Toyota"]['SUV'])
print(cars["Toyota"]['SUV'][-1])

# Access the "Expedition" in "Ford"
print(cars["Ford"]['SUV'][-1])

# "X1", "X5" in BMW
print(cars["BMW"]['SUV'][0])
print(cars["BMW"]['SUV'][-1])

# Concatenate the Highlander with "7 series"
print( cars["Toyota"]["SUV"][1] + ' ' +  cars['BMW']['Sedan'][-1])



# Movie Recommendation Program
import random

netflix_movies = ['Peppermint', 'The Agent', 'Game of Thrones', 'The Witcher', 'Interstellar', 'Alita: battle angel', 'The Recruit', 'RobinHood']
print(f'Hi, we have {len(netflix_movies)} movies you can choose from today.')

recommended_movie = random.choice(netflix_movies)
print(f'Would you like to watch: {recommended_movie}?')


# Using the randint() function to choose the movie
random_index = random.randint(0, len(netflix_movies) - 1)  # 0 - 6
recommended_movie = netflix_movies[random_index]
print(recommended_movie)
                    # OR
random_index = random.randint(1, len(netflix_movies))  # 1 - 7
recommended_movie = netflix_movies[random_index - 1]
print(recommended_movie)



# Movie recommendation with categories

netflix_movies = {
    "action": ['Agent 47', "Fast X", "Blade", "The Avengers"],
    'emotional': ["Miracle in Cell number 7", "War Room", "The Hate you Give"],
    'sci_fi': ["The 100", "Interstellar", "Tenet" ], 
    
}

print("You can select any of these categories: ")
print(list(netflix_movies.keys()))

category = input('Choose a category: ').strip().lower()
selected_category = netflix_movies[category]
recommended_from_category = random.choice(selected_category)

print(recommended_from_category)