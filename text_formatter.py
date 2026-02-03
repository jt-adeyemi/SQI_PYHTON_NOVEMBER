text = ' lorem ipsum dolor sit '
new_text = text.strip().capitalize()
print(f'{new_text}.')




state = 'Oyo'
capital = 'Nigeria'
country = 'Ibadan'

capital, country = country, capital
print(f'In the country, {country}, we have a state called {state}, and a capital city called {capital}')
