# Escape characters: \b(backspace), \r, \n(newline), \t(tab), \', \"
print('Folake is saying \n Titi')
print('Folake is saying \t Titi')
print('Folake\'s dog is running away')
print("we love writing \"python\" code")

# Indexing
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[10])
print(alphabet[0] + alphabet[5])

sentence = 'Python is Powerful'
print(sentence[0] + sentence[1] + sentence[-2] + sentence[-1])

# Slicing
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[5:])
print(alphabet[:7])
print(alphabet[2:10])
print(alphabet[-5:])
print(alphabet[:-6])
print(alphabet[::-1])
print(alphabet[4::2])
print(alphabet[1:12:3])
print(alphabet[:][-7])

car = 'Ferrari'
print(car + car[::-1])
car = car[1:]
print(car + car[::-1])