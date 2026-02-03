import requests
from bs4 import BeautifulSoup

quote_data = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(quote_data.text, 'html.parser')

all_quotes = soup.find_all('div', class_='quote')
all_quotes_list = []

for quote in all_quotes:
    quote_text = quote.find('span', class_='text').get_text()
    quote_author = quote.find('small', class_='author').get_text()
    quote_tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
    
    quote_dict = {
        'text': quote_text,
        'author': quote_author,
        'tags': quote_tags
    }
    
    all_quotes_list.append(quote_dict)


print(all_quotes_list)

# Count total number of quotes
print("Total number of quotes:", len(all_quotes_list))
# Count the number of unique authors
unique_authors = set(quote['author'] for quote in all_quotes_list)
print("Number of unique authors:", len(unique_authors))

# Find the author with the most quotes on the page
author_quote_count = {}
for quote in all_quotes_list:
    author = quote['author']
    if author in author_quote_count:
        author_quote_count[author] += 1
    else:
        author_quote_count[author] = 1
most_prolific_author = max(author_quote_count, key=author_quote_count.get)
print(most_prolific_author)

# Count how many quotes contain the word “is” (case-insensitive)
count = 0
for quote in all_quotes_list:
    if 'is' in quote['text'].lower():
        count += 1
print("Number of quotes containing the word 'is':", count)

# List all tags that appear and how many times each appears

tag_count = {}
for quote in all_quotes_list:   
    for tag in quote['tags']:
        if tag in tag_count:
            tag_count[tag] += 1
        else:
            tag_count[tag] = 1