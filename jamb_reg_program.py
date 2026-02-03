# from modules import utils
# from modules import validators
# from modules.utils import get_profile_code
import validators
from utils import get_profile_code

print("*************** WELCOME TO JAMB REGISTRATION PAGE ***************")


while True:
    username = input('* Username: ')
    if not validators.username_is_valid(username):
        print("Username is not valid")
    else:
        break


while True:
    email = input('* Email: ')
    if not validators.is_email_valid(email):
        print("Your email is not valid")
    else:
        break

phone = input('* Phone: ')
password = input('* Password: ')


print(f"Hi, {username}, your profile code is: {get_profile_code()}")