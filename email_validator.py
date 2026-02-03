from string import ascii_letters, punctuation, digits
def is_email_valid(email: str):
    '''This is a function that validates an email address'''  # Doc string

    if len(email) > 254:
        return False
    
    if email.count('@') != 1 or email.startswith('@') or email.endswith('@'):
        return False
    
    local, domain = email.split('@')

    # Local Validation

    if len(local) > 64:
        return False
    
    all_valid_chars = ascii_letters + '.-_' + digits

    if local.startswith('.') or local.endswith('.') or '..' in local:
        return False

    for char in local:
        if char not in all_valid_chars:
            return False
    
    # Domain Validation

    if len(domain) > 253 or len(domain) < 4:
        return False
     
    if domain[0] in '.-' or domain[-1] in '.-' or '..' in domain or '--' in domain:
        return False
    
    subdomains = domain.split('.')

    if len(subdomains) < 2:
        return False
    
    for char in domain:
        if char not in all_valid_chars:
            return False
        
    for subdomain in subdomains:
        if subdomain.startswith('-') or subdomain.endswith('-'):
            return False
        
    tld = subdomains[-1]

    if len(tld) < 2 or tld.isdigit():
        return False
    
    return True

email = input('Enter an email address: ')

print(is_email_valid(email))