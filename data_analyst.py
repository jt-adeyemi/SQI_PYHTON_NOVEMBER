import re

with open('reviews.txt', 'r') as file:
    content = file.read()

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"\+234\s[0-9]{3}\s[0-9]{3}\s[0-9]{4}"

    emails_found = re.findall(email_pattern, content)
    print(emails_found)

    phone_numbers_found = re.findall(phone_pattern, content)
    print(phone_numbers_found)

    with open('emails.txt', 'w') as email_file:
        for email in emails_found:
            email_file.write(f'{email}\n')
        print('All emails extracted')

    with open('phone_numbers.txt', 'w') as contact_file:
        for phone in phone_numbers_found:
            contact_file.write(f'{phone}\n')
        print('All contacts extracted')

print('Files Execution Completed')
