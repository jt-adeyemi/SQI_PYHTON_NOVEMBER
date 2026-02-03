# Define a pattern
# Use that pattern on the text or string to get your result

import re as regex

text = "Lorem, ipsum dolor sit amet consecteur adipiscing elit. Asperiores quod quasi, autem eveniet deleniti harum veritatis reprehenderit consecteur numquam! Preferendis soluta exercitationem necessitatibus rerum error? Iste quasi excepturi quam quae. tobi tibi tobi @tobi.com tobi"

pattern = r'\btobi\b' 

matched_pattern = regex.search(pattern, text)
print(matched_pattern)
print(matched_pattern.group())


matched_pattern = regex.findall(pattern, text)
print(matched_pattern)



story = "On the 1st day of January, I started learning to code and by 31st of January, I wrapped up. 22 boys live in the same estate where I stay"

pattern = r'\d'

matched_pattern = regex.findall(pattern, story)
print(matched_pattern)


pattern = r'\d+'

matched_pattern = regex.findall(pattern, story)
print(matched_pattern)


