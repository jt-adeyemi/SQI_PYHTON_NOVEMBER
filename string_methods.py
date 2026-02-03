
name = 'jane doe neuer'
# print(name.capitalize())
# print(name.title())
# print(name.count('ne'))
# print(name.startswith(('Ja', 'ja')))
# print(name.endswith(''))
# print(name.find('e', 9))
# print('Her full name is {}'.format(name.title()))
# print(name.isupper())
# print(name.islower())
# print(name.replace('jane', 'John'))
print(name.split())
# print(len(name))
# print(len(name.split()))

email = 'adeyemimme187013@futa.edu.ng'.lower()
domains = ('gmail.com', 'yahoo.co.uk', '.com.ng')
print(f'It is {email.endswith(domains)} that the email ends with {domains}')

print(email.split('e', 3))


countries_list = ['Japan', 'Belgium', 'Canada', 'Korea', 'England']
print(' | '.join(countries_list))
print(len(countries_list))

# Unpacking
user_data = ['Tobi', 'Dada', 'Computer Science', '28']
first_name, last_name, course_name, age = user_data
