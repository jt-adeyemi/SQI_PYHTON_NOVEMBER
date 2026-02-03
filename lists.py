students = ['John', 'Tobi', 'Shade', 'Blessing', 'Bola', 'Janet', 'Timi']
students.append('Florence')
print(students) # A list is ordered

# Replacing an item from a list
students[1] = 'Francis'
print(students)

# Reversing a list using slicing
reversed_list = students[::-1]
print(reversed_list)

# Replacing multiple items from a list
fruits = ['apple', 'banana', 'oranges', 'kiwi', 'mango']
fruits[1:3] = ['watermelon', 'cherry']
print(fruits)

students_set = {'John', 'Tobi', 'Shade', 'Blessing', 'Bola', 'Janet', 'Timi'}
print(students_set)  # A set is unordered

# LIST METHODS
# Appending an item to a list
animals = ['dog', 'cat', 'fish', 'snake', 'turkey']
animal1 = input('Enter your favorite animal: ').lower()
animal2 = input('Enter another favorite animal: ')
animals.append(animal1)
animals.append(animal2)
print(animals)

# Clearing a list
animals.clear()
print(animals)

# Duplicating a list
animals = ['dog', 'cat', 'fish', 'snake', 'turkey', 'donkey', 'porcuppine']
duplicate_animals = animals # affects the original variable
duplicate_animals = animals.copy() # shallow copy (does not affect the original variable except a nested list)
duplicate_animals.append('koala')
print(animals)
print(duplicate_animals)


from copy import deepcopy

deepcopy(animals)  # Creates a deep copy of the original list that suits a collection of nested lists
print(animals)


# Counting an item in a list
animals = ['dog', 'cat', 'fish', 'snake', 'turkey', 'cat']
print(animals.count('cat'))

# Appending multiple items to a list
programming_languages = ['C', 'C++', 'Java', 'R']
more_languages = ['Python', 'Rust', 'Dart', 'Go']
programming_languages.extend(more_languages)
print(programming_languages)

# Inserting an item in-between a list
programming_languages.insert(2, 'Rust')
print(programming_languages)

# Removing an item from a list
programming_languages = ['C', 'C++', 'Java', 'R']
print(programming_languages)
lang_to_remove = input('Enter a language to remove: ')
programming_languages.remove(lang_to_remove)
print(programming_languages)

# Reversing a list
programming_languages.reverse()
print(programming_languages)

# Sorting a list
fruits = ['apple', 'banana', 'oranges', 'kiwi', 'mango', 'lemon']
fruits.sort() # Ascending order
print(fruits)
fruits.sort(reverse=True) # Descending order
print(fruits)

name_of_things = ['dog', 'Cup', 'Ball', 'Aeoplane', 'Duck', 'rabbit']
name_of_things.sort(key=str.lower) # Case insensitive sorting
print(name_of_things)


footballers = ['Messi', 'Saka', 'Martinez', 'Rice', 'Raya', 'Ronaldo']
disliked_baller = footballers.pop(2)
print(footballers)

footballers.pop()  # removes the last item in a list
print(footballers)

print(footballers.index('Saka'))


wild_animals = list('lion', 'tiger', 'wolf', 'cheetah', 'snake')
sorted_wild_animals = sorted(wild_animals)  # gives you a sorted list while retaining the orginal list
print(wild_animals)
print(sorted_wild_animals)

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2  # Joining two lists while retaining the original list
list4 = list2 * 3  # Replicates the items in a list
print(list3)
print(list4)


# Nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])
print(sum(matrix[-1]))

# len(), sum(), max(), min()



