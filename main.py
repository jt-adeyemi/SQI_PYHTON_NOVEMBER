# Create a module called utils.py that has a function called replicate_user() that takes a user's name and then replicates it 10 times. Use that function in another file called main.py where you accept the user's name.

from utils import replicate

try:
    username = input('Enter your username to duplicate: ')
    print(replicate(username))
except KeyboardInterrupt:
        exit()
except Exception as e:
        print(e)







