# Paradigm ---> Design pattern

# Bank Account
# Customer
# Employee
# Admin

# get owner, get balance, transfer, withdraw

# class BankAccount:

#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#         print(f"The first name you provided is: {fname} and the last name is: {lname}")
    
#     def display_user_details(self):
#         return f"""
#         ******************** USER INFO **************
#         First Name: {self.firstname}
#         Last Name: {self.lastname}

#         """
    




# tobisaccount = BankAccount("Tobi", "Dada")   
# deborahsaccount = BankAccount("Deborah", "Jeffrey")   
# print(tobisaccount.display_user_details())
# # johnsaccount = BankAccount()
# # print(tobisaccount)
# # print(johnsaccount)


# # print(tobisaccount.balance)
# # print(johnsaccount.balance)



# # class Customer:
# #     firstname = "Tobi" # Fields / Attributes
# #     lastname = "Dada"
# #     metadata = {}

# #     def get_details(self):
# #         x = 40 # local variable
        
# #         return f"""
# # Firstname: {self.firstname}
# # Lastname: {self.lastname}
# #         """

# #     def get_dummy_address(self):
# #         return f"{self.firstname}'s address is: 234, Ijanikin street, Lagos"
    

# # customer1 = Customer() # 1 person
# # customer2 = Customer() # 2nd person

# # Displays the address in memory where these two objects are stored
# # print(customer1)
# # print(customer2)

# # Accessing data from those objects
# # print(customer1.firstname)
# # # print(customer2.firstname)

# # print(customer2.get_dummy_address())

# # print(customer2.metadata)



# class Customer:
#     MAX_ALLOWED_BALANCE = 200000000

#     def __init__(self, fname, lname):
#         # print("Object has been created.")
#         self.firstname = fname
#         self.lastname = lname

#     def second_method(self):
#         print("This second one too has been called.")
#         print(f"The last name assigned to this customer is: {self.lastname}")
    


    



# # c = Customer("Tobi", "Dada")
# # c2 = Customer("Janet", "Jackson")
# # c3 = Customer("Toni", "Kroos")

# # c3.second_method()


# # print(f"{c.firstname}'s max allowed balance is {c.MAX_ALLOWED_BALANCE}")
# # print(f"{c2.firstname}'s max allowed balance is {c2.MAX_ALLOWED_BALANCE}")





# # # customer1 = Customer("Tobi", "Dada", "234, Ijanikin") # 1 person
# # # customer2 = Customer("Jane", "Doe", "392, Ibrahim street") # 2nd person




# # # Fill in the Line class methods to accept coordinates as a pair of tuples and 
# # # return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.


# class Line:
#     def __init__(self, coor1, coor2): 
#         self.coord1 = coor1
#         self.coord2 = coor2

#     def distance(self):
#         x1, y1 = self.coord1
#         x2, y2 = self.coord2

#         distance_result = (((x2 - x1) ** 2 ) + ((y2 - y1) ** 2)) ** 0.5
#         return distance_result

#     def slope(self):
#         x1, y1 = self.coord1
#         x2, y2 = self.coord2

#         slope_result =  (y2 - y1) / (x2 - x1) 
#         return slope_result





# class Line:
#     def __init__(self, coor1, coor2): 
#         self.x1, self.y1 = coor1
#         self.x2, self.y2 = coor2

#     def distance(self):
#         distance_result = (((self.x2 - self.x1) ** 2 ) + ((self.y2 - self.y1) ** 2)) ** 0.5
#         return distance_result

#     def slope(self):
#         slope_result =  (self.y2 - self.y1) / (self.x2 - self.x1) 
#         return slope_result



# graph_line = Line((23, 5), (75, 34))
# another_graph_line = Line((90, 85), (75, 71))
# # print(graph_line.distance())
# print(another_graph_line.distance())
# # # Have your full name turned to uppercase

# # x1, y1 = (34, 54)
# # x2, y2 = (4, 2)



# class Cylinder:
#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius

#     def volume(self):
#         volume = (22 / 7) * (self.radius ** 2) * self.height
#         return volume

#     def surface_area(self):
#         area = (2 * (22 / 7) * self.radius) * (self.height + self.radius)
#         return area
    
# cylinder = Cylinder(5, 3)
# print(round(cylinder.volume(), 2))
# print(round(cylinder.surface_area(), 2))


# class Employee:
#     def __init__(self, *args):
#         self.fullname = args[0]
#         self.age = args[1]
#         self.position = args[2]
#         self.year_employed = args[-1]

#     def years_of_service(self, current_year):
#         return current_year - self.year_employed

# adesina = Employee('Adesina Oluwafemi', 34, 'Captain', 2003)
# print(adesina.years_of_service(2026))



# # class Dog:
# #     species = "Canis familiaris"  # class attribute

# #     def __init__(self, name, age):

# # 	  # instance attributes:

# #         self.name = name 
# #         self.age = age


# # dog1 = Dog("Border Collie", 2)
# # dog2 = Dog("Rotweiller", 3)

# # print(f"The specie of {dog1.name} is {dog1.species}")
# # print(f"The specie of {dog2.name} is {dog2.species}")





# # ************************* BANK ACCOUNT APP *************************

# class BankAccount:
#     def __init__(self, owner, bal):
#         self.owner = owner
#         self.balance = bal
    
#     def withdraw(self, amt):
#         self.balance -= amt
#         print("Withdrawing...")
    
#     def deposit(self, amt):
#         self.balance += amt
#         print("Deposited")
    

# joshua = BankAccount("Joshua Adeyemi", 1783)
# print(f"{joshua.owner}'s balance before the deposit: {joshua.balance}")
# joshua.deposit(70000)
# print(f"{joshua.owner}'s balance after the deposit: {joshua.balance}")
# joshua.withdraw(8880)
# print(f"{joshua.owner}'s balance after the withdrawal: {joshua.balance}")



    
# # Replicating the bank account WITHOUT A CLASS.
# user = {
#     'name': "Tobi Dada",
#     "balance": 1200000
# }

# def deposit(user, amt):
#     user['balance'] += amt
#     print("Depositing")

# def withdraw(user, amt):
#     user['balance'] -= amt
#     print("Withdrawing")

# print(user['name'], user['balance'])

# deposit(user, 6000)
# print(user['name'], user['balance'])



# Inheritance, Polymorphism, Encapsulation, Abstraction

# INHERITANCE: Single level, Multi-level, Multiple 
from winsound import Beep

class Vehicle:  # Parent or Super Class
    def horn(self):
        Beep(400, 1000)

    def speed_up(self):
        print('Speedin up...')

    def slow_down(self):
        print('Slowing down...')


class Innoson(Vehicle):  # Child or Sub Class 
    location = 'Nigeria'
    slang = 'Pride of African Roads'

class InnosonTesla(Innoson):  # Multi-level Inheritance
    pass


vehicle1 = Vehicle()
vehicle1.horn()


innoson_model1 = Innoson()
innoson_model1.horn()
print(f'Innoson Model 1 is made in {innoson_model1.location}')



# POLYMORPHISM: Method Overriding, Method Overloading

class Innoson(Vehicle):  # Child or Sub Class 
    location = 'Nigeria'
    slang = 'Pride of African Roads'

    def horn(self):
        Beep(300, 1200)  # Personalized/Customized method (Polymorphism)



class Device:

    def operate(self):
        print("Operating the device!")

class Smartphone(Device):
    def operate(self):
        print("Using the smartphone!")

class Tablet(Device):
    def operate(self):
        print("Using the tablet!")

class Laptop(Device):
    def operate(self):
        print("Using the laptop!")