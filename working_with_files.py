# Opening a File
# open('filename', 'mode')
# file = open('data.txt', 'r') 

# print(dir(file))
# Returns all the content of the file in just one string
# print(file.read())

# Returns every single line of the read file as items in a list
# print(file.readlines())

# Returns a single line where the cursor is currently pointing to
# print(file.readline())
# print(file.readline())

# This prints out every line in the file using a for loop
# for line in file.readlines():
#     print(line.strip())


# Get every first letter of the text on each line
# for line in file.readlines():
#     print(line.strip()[0])


# Get every first, second and last letter of the text on each line
# for line in file.readlines():
#     print(line.strip()[0], line.strip()[1], line.strip()[-1])

# for line in file.readlines():
#     l = line.strip()
#     print(l[0], l[1], l[-1])
#     print(l[0:2], l[-1])


# Try to find out whether the word "tobi" exists in the text of data.txt
# print("tobi" in file.read())


# Trying to write to a file
# file.write("Hello to the world.")

# Tells us that whether the read operation is allowed on the opened file.
# print(file.readable())



# file = open('data.txt', 'w') # Mode

# Throws an error
# print(file.read())

# WRiting to a file
# file.write("I just INTENTIONALLY wrote my first line.\n")
# file.write("I just RELUCTANTLY wrote my second line.\n")
# print("Done with writing.")


# file = open('data.txt', 'r+') # Mode Read & Append
# # file.write("Should be at the end of the file.")
# print(file.read())

# file.write("Something written to file")

# file = open('data.txt', 'w+') # Mode Read & Append
# # file.write("Should be at the end of the file.")

# file.write("BAlablu\n")
# file.write("Something written to file\n")

# print(file.read())



# Password dump program
# file = open('password_dump.txt', 'w')

# # Bruteforcing
# for i in range(10000):
#     file.write(f"{str(i).zfill(4)}\n")
# print("Password dump generated")


# # Context manager
# with open('password_dump.txt', 'w') as myfile:
#     for i in range(10000):
#         myfile.write(f"{str(i).zfill(4)}\n")



persons = [
    {'name': "Tobi", "course": "Computer"},
    {'name': "Bryan", 'course': "Physics"},
    {'name': 'Bryce', 'course': "Economics"},
    {'name': 'Shola', 'course': "Law"}
]

# with open('person_details.txt', 'w') as file:

#     file.write("NAME\t\t\tCOURSE\n")
#     for person in persons:
#         file.write(f"{person['name']}\t\t\t{person['course']}\n")



# Create the person_details.txt file in a folder one step outside this current file.
# with open('../person_details.txt', 'w') as file:

#     file.write("NAME\t\t\tCOURSE\n")
#     for person in persons:
#         file.write(f"{person['name']}\t\t\t{person['course']}\n")



# # Create the person_details.txt file in a directory one step inside this current file.
# with open('modules/person_details.txt', 'w') as file:

#     file.write("NAME\t\t\tCOURSE\n")
#     for person in persons:
#         file.write(f"{person['name']}\t\t\t{person['course']}\n")