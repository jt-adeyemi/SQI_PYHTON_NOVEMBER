# Go to https://www.scrapethissite.com/pages/simple/.
# Count how many countries are listed on the page.
# Print the country with the largest and smallest population.
# Calculate the average population of all countries.
# For each country, compute its population density (people per km²): density = population / area. List the top 3 countries with the highest density.
# Find all countries whose capital city starts with the letter "A". Return a list of those countries and their capitals.
# Find countries with an area greater than 1,000,000 km²
# Find countries with an area less than 500 km²
# Get the country that has 0 population.



import requests
from bs4 import BeautifulSoup

countries_data = requests.get('https://www.scrapethissite.com/pages/simple/')
soup = BeautifulSoup(countries_data.text, 'html.parser')

all_countries = soup.find_all('div', class_='country-info')
print(all_countries)
countries_list = []

for country in all_countries:
    capital = capital.find('span', class_='country-capital').get_text()
    population = population.find('span', class_='country-population').get_text()
    area = area.find('span', class_='country-area').get_text()
 