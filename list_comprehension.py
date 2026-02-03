# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# for adj in adjectives:
#     for animal in animals:
#         print(adj, animal)


# LIST COMPREHENSIONS

# adjectives = ["fierce", "majestic", "playful"]
# adjectives_copy = []

# for adjective in adjectives:
#     adjectives_copy.append(adjective)

# print(adjectives)
# print(adjectives_copy)


# adjectives = ["fierce", "majestic", "playful"]
# adjectives_copy = [adjective for adjective in adjectives]

# print(adjectives)
# print(adjectives_copy)


# TRANSFORMATION
# verbs = ['play', 'sit', 'dance', 'jump', 'sleep']
# verb_upper = [verb.upper() for verb in verbs]

# print(verbs)
# print(verb_upper)


# objects = ['television', 'radio', 'violin', 'bottle', 'fan']

# for obj in objects:
#     print(len(obj))

# objects_count = [len(obj) for obj in objects]
# print(objects_count)


# animals = ['Elephant', 'Ant', 'Zebra', 'Kangaroo', 'Duck', 'Aardvark', 'Koala']

# no_of_as = [animal.lower().count('a') for animal in animals]
# print(no_of_as)
# starts_with_a = [animal for animal in animals if animal[0].lower() == 'a']
# print(starts_with_a)


# FILTERING
# car_brands = ['Toyota', 'Suzuki', 'Elemental', 'Nissan', 'Mercedes', 'Aston', 'Ferrari', 'Infiniti', 'Honda', 'Bugatti', 'Hyundai']
# vowels = ('a', 'e', 'i', 'o', 'u')

# has_vowel_start = [brand.lower().startswith(vowels) for brand in car_brands]
# print(has_vowel_start)

# starts_with_consonant = [brand for brand in car_brands if not brand.lower().startswith(vowels)]
# print(starts_with_consonant)


# # Dictionary Comprehension
# brands = {brand: brand.lower().startswith(vowels) for brand in car_brands}
# print(brands)


# cities = ['Lagos', 'Abuja', 'Kano', 'Ibadan', 'Benin City']
# new_cities = [city for city in cities if city != 'Lagos']

# print(new_cities)

# countries = ['Japan', 'Nigeria', 'Australia', 'Canada', 'U.S.A', 'United Kingdom', 'Ireland', 'Ghana', 'Togo']
# developing_countries = ['Nigeria', 'Togo', 'Ghana']

# developed_countries = [country for country in countries if country not in developing_countries]
# print(developed_countries)


# Get all the numbers that are multiples of both 3 and 5 between 1 and 100
# multiples_of_3_and_5 = [num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0]

# print(multiples_of_3_and_5)


# GENERATORS 

# 7. Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False
greetings = ["HELLO", "world", "pyTHon", "ROCKS"]

is_all_upper = any(word.isupper() for word in greetings)
is_all_upper = all(word.isupper() for word in greetings)
print(is_all_upper)


# 8. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
words = ["apple", "zebra", "mango", "lemon"]

any_starts_with_z = all(word.lower().startswith('z') for word in words)
# any_starts_with_z = any([False, True, False, False])
# any_starts_with_z = [word.lower().startswith('z') for word in words]
print(any_starts_with_z)
