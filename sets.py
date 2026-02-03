numbers = {2, 4, 6, 8, 10}
print(numbers) # A set is unordered

numbers = {2, 4, 6, 8, 10, 4, 10, 12}
print(numbers) # Removes duplicates

fruits = {'Apple', 'Mango', 'Pawpaw', 'Watermelon', 'Guava'}
# print(fruits[-1]) # cannot be indexed or sliced due to its unpredictability

random_data = {'Nigeria', 2000, 22.47, '123', True, False, 0, 1}
print(random_data)

unique_countries = set() # Creating an empty set
print(type(unique_countries))

all_countries = ['Nigeria', 'Portugal', 'England', 'Argentina', 'China', 'England', 'Nigeria']
unique_countries = list(set(all_countries))
print(unique_countries)

# A simple program that accepts a sentence from the user, and the returns only the unique words in the sentence
sentence = input('Enter your sentence: ').strip().lower()
sentence_list = sentence.split()
unique_words_sentence = set(sentence_list)
print(unique_words_sentence)

# A program that takes a phrase and then returns all the UNIQUE LETTERS in that phrase
words = input('Enter a phrase: ').lower().replace(' ', '')
unique_letters = set(words)
print(unique_letters)

wild_animals = {'lion', 'jaguar', 'snake', 'crocodile'}
favorite_animal = input('Enter your favourite animal: ').lower().strip()

is_dangerous = favorite_animal in wild_animals
print(f'It is {is_dangerous} that your favourite animal is dangerous.')

# Set Methods
# Adding an item to a set
football_clubs = {'Arsenal', 'Brentford', 'Chelsea', 'Everton', 'Wolves', 'Aston Villa'}
football_clubs.add('Burnley')
print(football_clubs)

# Removing an item from a set
football_clubs.remove('Wolves')
print(football_clubs)

# Remove an item that exists from a set otherwise ignore
football_clubs.discard('chelsea')

# Removes a random item from a set
random_club = football_clubs.pop()
print(football_clubs)
print(random_club)

# Clears a set collection
football_clubs.clear()
print(football_clubs)


even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
multiple_of_20 = {2, 4, 10, 20}

union = even_numbers.union(multiple_of_20)
print(union)

common_numbers = even_numbers.intersection(multiple_of_20)
print(common_numbers)

numbers_in_only_set1 = even_numbers.difference(multiple_of_20)
print(numbers_in_only_set1)
numbers_in_only_set2 = multiple_of_20.difference(even_numbers)
print(numbers_in_only_set2)

unique_numbers_in_both_set = even_numbers.symmetric_difference(multiple_of_20)
print(unique_numbers_in_both_set)

# Inserting items from another set into a set using update()
cold_countries = {'australia', 'russia', 'canada', 'finland', 'ukraine'}
other_cold_countries = {'iceland', 'antartica', 'germany', 'belgium'}

cold_countries.update(other_cold_countries)
print(cold_countries)

set1 = {'apple', 'banana', 'cherry', 'mango'}
set2 = {'apple', 'microsoft', 'google', 'tesla'}

set1.difference_update(set2)
print(set1)

set1.symmetric_difference_update(set2)
print(set1)


primary_colors = {'red', 'green', 'blue'}
user_primary_colors = input('Provide 3 primary colors: ').lower().replace(' ', '')
user_primary_colors_list = user_primary_colors.split(',')
user_primary_colors_set = set(user_primary_colors_list)

is_all_primary_colors = user_primary_colors_set == primary_colors
print(is_all_primary_colors)

setA = {'jupiter', 'saturn', 'pluto'}
setB = {'pluto', 'saturn', 'uranus', 'neptune'}

difference = setA - setB
print(difference)

intersection = setA & setB
print(intersection)

union = setA | setB
print(union)
# note: both must be sets to use the symbols




# **************************** a simple microfinance scenario **************************
borrowers = ["Tunde", "Amaka", "Sola", "Kemi", "Grace", "Ayo", "Kolade", "Matt"]
lenders = ["Ayo", "Bisi", "Tunde", "Kunle", "Matt", "James"]

borrowers_set= set(borrowers)
lenders_set= set(lenders)

# List all customers of the bank (anyone who is either a borrower or a lender).
all_customers = borrowers_set.union(lenders_set)

# OR

all_customers = borrowers_set | lenders_set
print(f"All customers in db: {all_customers}")

# List people who are both borrowers and lenders.
both_borrowers_and_lenders = borrowers_set.intersection(lenders_set)
print("All customers who both borrowed and lended: ", both_borrowers_and_lenders )

# List people who borrowed only.
borrowers_only = borrowers_set.difference(lenders_set)
print("Those who only borrowed: ", borrowers_only)


# List people who lent money only.
lenders_only = lenders_set.difference(borrowers_set)
print("Those who only lended: ", lenders_only)

# List people who either borrowed or lent but not both.
users_with_only_one_action = lenders_set.symmetric_difference(borrowers_set)
print("All who either ONLY borrowed or lended: ", users_with_only_one_action)


# Add a new borrower "Chika" and remove "Grace" from borrowers.
borrowers_set.add("Chika")
borrowers_set.discard("Grace")
print(borrowers_set)
print(lenders_set)

# Check if "Sola" is a lender.
sola_exists = "Sola" in lenders_set
print(f"It is {sola_exists} that Sola is a lender")

# Randomly remove 2 people from borrowers because their loan was fully repaid.
borrower1 = borrowers_set.pop()
borrower2 = borrowers_set.pop()

print(f"{borrower1}'s loan has been successfully waived by our gracious LAPO company")
print(f"{borrower2}'s loan has been successfully waived by our gracious LAPO company")
updated_borrowers_formatted = ', '.join(borrowers_set)
print(f"All remaining borrowers are: {updated_borrowers_formatted}.")

