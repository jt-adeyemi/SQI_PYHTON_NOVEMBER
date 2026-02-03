# 5. Create a function called total_age that returns the sum of all the ages given.

# Test Data:
# print(total_age(12, 30, 18))
# print(total_age(40, 25))

# Expected Output:
# 60
# 65

def total_age(*args):
    age_total = sum(args)
    return age_total

print(total_age(12, 30, 18))
print(total_age(40, 25))


# 6. Create a function called list_countries that prints out each country passed in.

# Test Data:
# list_countries("Nigeria", "Ghana", "Kenya")
# list_countries("Canada", "Mexico")

# Expected Output:
# Nigeria
# Ghana
# Kenya
# Canada
# Mexico

def list_countries(*args):
    for country in args:
        print(country)
    
list_countries("Nigeria", "Ghana", "Kenya")
list_countries("Canada", "Mexico")


# 7. Create a function called student_details that prints each student’s name and score.

# Test Data:
# student_details(Fola=78, Muna=88, Kola=65)
# student_details(Sandra=91, Alex=85)

# Expected Output:
# Fola scored 78
# Muna scored 88
# Kola scored 65
# Sandra scored 91
# Alex scored 85

def student_details(**kwargs):

    for name, score in kwargs.items():
        print(f'{name} scored {score}')

student_details(Fola=78, Muna=88, Kola=65) 
student_details(Sandra=91, Alex=85)


# 8. Create a function called average_score that returns the average of all scores passed in.

# Test Data:
# print(average_score(50, 60, 70))
# print(average_score(80, 90))

# Expected Output:
# 60.0
# 85.0

def average_score(*args):
    return sum(args) / len(args)

print(average_score(50, 60, 70))
print(average_score(80, 90))


# 9. Create a function called total_price that adds up the prices of all items passed as keyword arguments.

# Test Data:
# print(total_price(bread=500, milk=1200, eggs=700))
# print(total_price(book=1500, pen=200))

# Expected Output:
# 2400
# 1700

def total_price(**kwargs):
    return sum(kwargs.values())

print(total_price(bread=500, milk=1200, eggs=700))
print(total_price(book=1500, pen=200))


# 10. Create a function called first_and_last that prints the first and last values passed in.

# Test Data:
# first_and_last(4, 10, 6, 9, 12)
# first_and_last("a", "b", "c", "d")

# Expected Output:
# First: 4, Last: 12
# First: a, Last: d

def first_and_last(*args):
    print(f'First: {args[0]}, Last: {args[-1]}')

first_and_last(4, 10, 6, 9, 12)
first_and_last("a", "b", "c", "d")


# 11. Create a function called describe_animals that prints out animal and their sound.

# Test Data:
# describe_animals(cat="meow", dog="bark", cow="moo")
# describe_animals(lion="roar", snake="hiss")

# Expected Output:
# cat makes the sound meow
# dog makes the sound bark
# cow makes the sound moo
# lion makes the sound roar
# snake makes the sound hiss

def describe_animals(**kwargs):
    for animal, sound in kwargs.items():
        print(f'{animal} makes the sound {sound}')
    
describe_animals(cat="meow", dog="bark", cow="moo")
describe_animals(lion="roar", snake="hiss")


# 12. Create a function called total_characters that returns how many characters in total exist in all keyword values.

# Test Data:
# print(total_characters(a="banana", b="mango", c="kiwi"))
# print(total_characters(x="hi", y="there"))

# Expected Output:
# 15
# 7

def total_characters(**kwargs):
    return len(''.join(kwargs.values()))

print(total_characters(a="banana", b="mango", c="kiwi"))
print(total_characters(x="hi", y="there"))


# 13. Create a function called find_minimum that returns the smallest number from all the values passed in.

# Test Data:
# print(find_minimum(99, 45, 12, 88))
# print(find_minimum(8, 3, 7))

# Expected Output:
# 12
# 3

# def find_minimum(*args):
#     return min(args)

# print(find_minimum(99, 45, 12, 88))
# print(find_minimum(8, 3, 7))
        # OR
def find_minimum(*args):
    min_value = args[0]

    for value in args:
        # print(value)
        if value < min_value: 
            # print(value > min_value)
            min_value = value
    return min_value

print(find_minimum(99, 45, 12, 88))
print(find_minimum(8, 3, 7))


# 14. Create a function called sum_scores_and_bonuses that returns the total of all numbers passed, including keyword values.

# Test Data:
# print(sum_scores_and_bonuses(10, 20, bonus1=5, bonus2=15))
# print(sum_scores_and_bonuses(100, bonus=50))

# Expected Output:
# 50
# 150

def sum_scores_and_bonuses(*args, **kwargs):
    return sum(args) + sum (kwargs.values())

print(sum_scores_and_bonuses(10, 20, bonus1=5, bonus2=15))
print(sum_scores_and_bonuses(100, bonus=50))


# 15. Create a function called longest_word that returns the longest string from all the values passed in (args + kwargs).

# Test Data:
# print(longest_word("cat", "hippopotamus", animal="giraffe", bird="eagle"))
# print(longest_word("short", name="exaggeration", tool="pen"))

# Expected Output:
# hippopotamus
# exaggeration

def longest_word(*args, **kwargs):
    all_words = list(args) + list(kwargs.values())
    print(all_words)
    longest = all_words[0]

    for word in all_words:
        if len(word) > len(longest):
            longest = word
    
    return longest

print(longest_word("cat", "hippopotamus", animal="giraffe", bird="eagle"))
print(longest_word("short", name="exaggeration", tool="pen"))
