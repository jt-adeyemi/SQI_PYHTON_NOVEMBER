"""
This validators file is meant to give you the basic validators you need for your jamb registration program
"""

from string import ascii_letters, digits

def uses_valid_chars(string_of_text):
    all_valid_chars = ascii_letters + '._-' + digits  # A-Za-z0-9.-_
    for char in string_of_text:
        if char not in all_valid_chars:
            return False
    # return True


def username_is_valid(username:str):
    
    if username.isupper() or username.islower() or username.isdigit():
        return False
    
    if len(username) < 3 or len(username) > 24:
        return False
    
    return True
    




def is_email_valid(email: str):
    if len(email) > 254:
        return False
    
    if email.count('@') != 1:
        return False

    local, domain = email.split('@')

    if len(local) > 64 or len(local) < 1:
        return False
   
    if local[0] == '.' or local[-1] == '.' or '..' in local:
        return False
    
    uses_valid_chars(local)
    
    if len(domain) > 253 or len(domain) < 4:
        return False

    if domain[0] == '.' or domain[-1] == '.' or '..' in domain:
        return False
    
    if domain[0] == '-' or domain[-1] == '-' or '--' in domain:
        return False

    split_domain = domain.split('.')

    if len(split_domain) < 2:
        return False
    
    uses_valid_chars(domain)
   
    for subdomain in split_domain:
        if subdomain.startswith('-') or subdomain.endswith('-'):
            return False
        
    tld = split_domain[-1]

    if len(tld) < 2 or tld.isdigit():
        return False
    
    return True