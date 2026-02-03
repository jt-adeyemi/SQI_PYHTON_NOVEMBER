# Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.
numbers = [10, 20, 30, 40]
del numbers[2]
print(numbers)

# Create a list called original with items "one", "two", "three". Create a copy of the list.
original = ['one', 'two', 'three']
duplicate = original.copy()

# Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and list2 together.
list1 = ['a', 'b']
list2 = ['c', 'd']
list_merge = list1 + list2
print(list_merge)

# Access and print the second subject of the first person in the list.
# data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]
data = [
    ["Alice", 25, ["Math", "Physics"]],
    ["Bob", 30, ["Chemistry", "Biology"]],
    ["Charlie", 35, ["History", "Geography"]]
]
print(data[0][-1][-1])

# Access and print the first value in the list of numbers associated with "San Francisco".
# 	records = [
#     ["New York", [10, 20, 30]],
#     ["San Francisco", [40, 50, 60]],
#     ["Austin", [70, 80, 90]]
# ]
records = [
    ["New York", [10, 20, 30]],
    ["San Francisco", [40, 50, 60]],
    ["Austin", [70, 80, 90]]
]
print(records[1][1][0])

# Get the first e in Ayo’s gender and Get Ben’s age.
#  	group = [
#     ["Ayo", ["Female", 12]],
#     ["Ben", ["Male", 9]]
# ]
group = [
    ["Ayo", ["Female", 12]],
    ["Ben", ["Male", 9]]
]
print(group[0][1][0][1])
print(group[-1][-1][-1])

# Get the l in Nina’s gender and Get Tobi’s age records = [
#     ["Tobi", ["Male", [6]]],
#     ["Nina", ["Female", [7]]]
# ]
records = [
    ["Tobi", ["Male", [6]]],
    ["Nina", ["Female", [7]]]
]
print(records[-1][-1][0][-2])
print(records[0][-1][-1][-1])

# Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the battery percentage of R2
# robot_grid = [
#     ["R2", ["battery", [98]]],
#     ["R5", ["status", "active"]],
#     ["X1", [["joint", "loose"], "error"]]
# ]
robot_grid = [
    ["R2", ["battery", [98]]],
    ["R5", ["status", "active"]],
    ["X1", [["joint", "loose"], "error"]]
]
print(robot_grid[-1][-1][0][-1][1:3])
print(robot_grid[0][-1][-1][-1])

# Get the Five in the Jazz song title and Get the duration of the Jazz song
# playlist = [
#     ["Jazz", ["Take Five", 5.24]],
#     ["Pop", ["Blinding Lights", 3.20]],
#     ["Rock", ["Bohemian Rhapsody", 5.55]]
# ]
playlist = [
    ["Jazz", ["Take Five", 5.24]],
    ["Pop", ["Blinding Lights", 3.20]],
    ["Rock", ["Bohemian Rhapsody", 5.55]]
]
print(playlist[0][-1][0][-4:])
print(playlist[0][-1][-1])

# Get the letter v in Tiger’s category and Get the first letter of the Frog’s type
# animals = [
#     ["Elephant", ["Herbivore"]],
#     ["Tiger", ["Carnivore"]],
#     ["Frog", ["Amphibian"]]
# ]
animals = [
    ["Elephant", ["Herbivore"]],
    ["Tiger", ["Carnivore"]],
    ["Frog", ["Amphibian"]]
]
print(animals[1][-1][0][-4])
print(animals[-1][-1][0][0])