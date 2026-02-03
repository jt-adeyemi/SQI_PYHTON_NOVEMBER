def replicate(user):
    return user * 10


import random
from string import ascii_uppercase

def get_profile_code():
    six_digit_otp = random.randint(100000, 999999)
    three_random_letters = ''.join(random.sample(ascii_uppercase, 2))
    full_profile_code = three_random_letters + str(six_digit_otp)

    return full_profile_code


# ___name__ can store two values: __main__

# If this utils.py file is executed directly, then execute the code below, too.
if __name__ == '__main__':
    print("We want to print 0 to 114")
    for i in range(115):
        print(i)

    print("Done printing")



def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Alice")) 