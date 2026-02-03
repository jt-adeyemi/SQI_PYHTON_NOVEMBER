# Create a string variable sentence with the value "the quick brown fox jumps over the lazy dog". Capitalize the first letter of the string and print the result.
sentence = "the quick brown fox jumps over the lazy dog"
print(sentence.capitalize())

# Create a string variable book_title with the value "to kill a mockingbird". Capitalize the first letter of each word and print the result.
book_title = "to kill a mockingbird"
print(book_title.title())

# Create a string variable text with the value "hello world". Count the number of occurrences of the letter 'o' and print the result.
text = "hello world"
print(text.count('o'))

# Create a string variable filename with the value "document.txt". Check if the string starts with "doc" and print the result.
filename = "document.txt"
print(filename.startswith('doc'))

# Create a string variable url with the value "https://www.example.com". Check if the string ends with ".com" and print the result.
url = "https://www.example.com"
print(url.endswith('.com'))

# Create a string variable phrase with the value "find the needle in the haystack". Find the position of the word "needle" and print the result.
phrase = "find the needle in the haystack"
print(phrase.find('needle'))

# Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the format() method to replace the placeholders with "Alice" and "Wonderland" and print the Result. Bonus point if you can do it with the f-string and concatenation methods also.
template = "Hello, {}. Welcome to {}."
print(template.format('Alice', 'Wonderland'))

# Create a string variable word with the value "hello". Check if all characters in the string are lowercase and print the result.
word = "hello"
print(word.islower())

# Create a string variable shout with the value "HELLO". Check if all characters in the string are uppercase and print the result.
shout = "HELLO"
print(shout.isupper())

# Create a string variable mixed_case with the value "PyThOn". Convert all characters to lowercase and print the result.
mixed_case = "PyThOn"
print(mixed_case.lower())

# Create a string variable mixed_case with the value "PyThOn". Convert all characters to uppercase and print the result.
print(mixed_case.upper())

# Create a string variable padded_text with the value " hello ". Remove leading whitespace and print the result.
padded_text = " hello "
print(padded_text.lstrip())

# Create a string variable padded_text with the value " hello ". Remove trailing whitespace and print the result.
print(padded_text.rstrip())

# Create a string variable padded_text with the value " hello ". Remove both leading and trailing whitespace and print the result.
print(padded_text.strip())

# Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" and print the result.
greeting = "Hello, World!"
print(greeting.replace('World', 'Alice'))

# Given the string course_name = "Introduction to Python", use slicing to print: The word "Introduction". The word "Python".
course_name = "Introduction to Python"
print(course_name.find('n', 2))
print(course_name[:12])
print(course_name[-6:])

# Given the string quote = "To be or not to be, that is the question.", use slicing to print: The substring "To be or not to be". The substring "that is the question".
quote = "To be or not to be, that is the question."
print(quote.find('be,'))
print(quote[:18])
print(quote[20:-1])

# Given the string phrase = "A journey of a thousand miles begins with a single step", use slicing to print: The last 5 characters. All characters except the last 7.
phrase = "A journey of a thousand miles begins with a single step"
print(phrase[-5:])
print(phrase[:-7])