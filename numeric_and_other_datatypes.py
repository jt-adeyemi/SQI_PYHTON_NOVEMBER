print(type(4/3))
num1 = 300
num2 = 100_000_000_000
num3 = 107.5

# There are two boolean values: True and False

print(10 > 9)
print(10 == 9)
print(10 < 9)

first_num = 400
second_num = 88.2

first_is_greater = first_num >= second_num
print(first_is_greater)

num1 = 400
num2 = 400.0
print(num2 == num1)

print(first_num + 20 > 190 and second_num * 13 > 40)
print(first_num + 20 <= 190 and second_num * 13 > 40)
print(first_num + 20 > 190 or second_num * 13 < 40)

is_raining = True
has_umbrella = True
user_is_safe = is_raining and has_umbrella
print(user_is_safe)

# Type Casting: Implicit casting and Explicit casting
# Explicit casting: int(), float(), str(), bool()
num1 = '500'
num2 = '600'

num1 = int(num1)
num2 = float(num2)

print(num1 + num2)

first_num = 3.142
second_num = '3.142'
print(int(first_num))
# print(int(second_num))
print(float(second_num))

print(bool(0))
print(bool(0.0))
print(bool(0.00001))
print(bool(578))

print(bool(''))
print(bool(' '))
print(bool('hey'))
print(bool('False'))

print(bool(None))
print(bool(True))
print(bool(False))

name = '     '
print(bool(name.strip()))