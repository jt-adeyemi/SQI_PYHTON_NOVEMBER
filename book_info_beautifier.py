book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"
# Using the example above, the expected output is: 
# The book The Art Of Programming was written by John Doe and published in 2020.
# It has 350 pages and ISBN 978-3-16-148410-0 and costs ₦2500.00.

book_info_list = book_info.split(' ; ')
author, book_title, year, book_number, page_number, price = book_info_list

author = author.title()
book_title = book_title.title()
book_number = book_number.replace('ISN', 'ISBN')
price = float(price)

print(f'The book {book_title} was written by {author} and published in {year}. \nIt has {page_number} pages and {book_number} and costs ₦{price:.2f}.')