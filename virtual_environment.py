# Virtual Environment
# -making a virtual environment: python3 -m venv .venv
# -activating a virtual environment: source .venv/bin/activate
# -deactivating a virtual environment: deactivate
# -installing a library: pip3 install numpy
# -uninstalling a library: pip3 uninstall numpy



import requests

response = requests.get('https://google.com')
print(response.content)


# Creating a bot to keep visiting a website
# while True:
#     response = requests.get('https://google.com') 



user_search = input('Enter word to search: ').lower()

try:
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{user_search}').json()
except requests.exceptions.ConnectionError:
    print('No internet connection. Please try again later.')
    exit()

if type(response) == dict and response.get('title'):
    print('The word you searched for was not found. Please check the spelling and try again.')
    exit()

meanings = response[0]['meanings']

for meaning in meanings:
    for definition in meaning['definitions']:
        print(definition['definition'])
        if definition.get('example'):
            print('Example:', definition['example'])
        print()


import requests
from bs4 import BeautifulSoup

# Fetch the website content using requests
url = 'https://www.example.com'  # You can change this to a URL of your choice
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the header
    header = soup.find('h1')

    if header:
        print('Header:', header.get_text())

    # Extract the main content (assuming main content is within <main> tag or similar)
    main_content = soup.find('main')
    if main_content: # If a <main> tag exists
        print('Main Content:', main_content.get_text())
    else:
        # Fallback: Extract all paragraphs as main content
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            print('Paragraph:', p.get_text())
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)




# Retrieving all the usernames of every user from the list of dictionaries
import requests as req

try:
    user_data = req.get('https://jsonplaceholder.typicode.com/users').json()
except req.exceptions.ConnectionError:
    print('No internet connection')
    exit()

for user in user_data:
    print(f'Username: {user['username']} \t {user['email']} \t {user['address']['zipcode']}')