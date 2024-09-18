# # Exercise 9: Classes

# Please work through as many of the following exercises as you’re able to in the allotted time and upload the results of the last task you were able to complete

# ### 1.
# Make a class called, “Restaurant”. The `__init__()` method for Restaurant should store two attributes: `Restaurant_name` & `Cuisine_type`.
# - Make a method called `describe_restaurant()` that prints these two pieces of information, and a method called `open_restaurant()` that prints a message indicating that the restaurant is open.
# - Make an instance called, `restaurant1` from your class. Print the two attributes individually, and then call both methods.
# - Create three different instances from the class with different names, and call `describe_restaurant()` for each instance.
# - Add an attribute called `number_served` with a default value of `0`, create an instance called `restaurant2`. Print the number of customers the restaurant has served, and then update this value and print it again. 
# - Add a method called set_number_served() that lets you update the `number_served` attribute. Call this method with a new number and print the value to confirm the change. 
# - Add a method called `increment_number_served()` that lets you increment `number_served`. Call this method with a number representing how many customers were served in a day of business.
class Restaurant():
    def __init__(self, Restaurant_name, Cuisine_type, number_served):
           self.name = Restaurant_name
           self.type = Cuisine_type
           self.number_served = number_served

    def describe_restaurant(self):
        print(f'Restaurant name: {self.name}, Cuisine type: {self.type}, number of customers: {self.number_served}')

    def open_restaurant(self):
        print(f'The restaurant {self.name} is open.')

    def number_served_customer(self):
         print(f'Number of customers: {self.number_served}')

    def set_number_served(self, new_number):
         self.number_served = new_number
         print(f'Set number served {self.number_served}, new number: {new_number}')

    def increment_number_served(self, increament_number):
         total_number = self.number_served + increament_number
         print(f'Increased number is: {increament_number}, total increased number is {self.number_served} + {increament_number} = {total_number} ')

restaurant1 = Restaurant('Roma','Arakanese',0)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

instance1 = Restaurant('JOOOO', 'MMMMMMM',2)
instance1.describe_restaurant()

instance2 = Restaurant('BA','WWWWWWW',4)
instance2.describe_restaurant()

instance3 = Restaurant('CCC', 'LLLLLLLLL',6)
instance3.describe_restaurant()

restaurant2 = Restaurant('Rakhine', 'Arakan', 1)
restaurant2.number_served_customer()
restaurant2.set_number_served(5)
restaurant2.increment_number_served(3)

# ### 2.
# Make a class called `User` and give it two attributes called `first_name` and `last_name`. Create several other attributes that are typically stored in a user profile. 
# - Make a method called `describe_user()` that prints a summary of the user’s information. 
# - Make a method called `greet_user()` that prints a personalized greeting.
# - Create several instances representing different users, and call both methods for each user.

class User():
     def __init__(self,first_name, last_name, age, nationality, hobby, favourite_food, login_attempts):
          self.first_name = first_name
          self.last_name = last_name
          self.age = age
          self.nationality = nationality
          self.hobby = hobby
          self.favourite_food = favourite_food
          self.login_attempts = login_attempts
          
     def describe_user(self):
        print(f'first name: {self.first_name} \nlast name: {self.last_name} \nage: {self.age} \nnationality: {self.nationality} \nhobby: {self.hobby} \nfavourite food: {self.favourite_food}')

     def greet_user(self):
         print(f'Hello {self.first_name}, How are you?')

     def increment_login_attempts(self):
         self.login_attempts += 1
         print(f'log in attempt: {self.login_attempts}')
         print(f'Increased log in attempt is : {self.login_attempts}')

     def reset_login_attempts(self):
         self.login_attempts = 0
         print(f'Resetting login attempts from to {self.login_attempts}')

        
user = User('Won', 'Thein', 20, 'British', 'Reading', 'Vegetarian',1)

user.describe_user()
user.greet_user()

userJohn = User('John', 'White', 40, 'British', 'Eating and Reading', 'Vegan', 1)
userJohn.describe_user()
userJohn.greet_user()

userJohn.increment_login_attempts()
userJohn.increment_login_attempts()
userJohn.increment_login_attempts()
userJohn.increment_login_attempts()
userJohn.increment_login_attempts()
userJohn.increment_login_attempts()
userJohn.increment_login_attempts()
userJohn.increment_login_attempts()
userJohn.increment_login_attempts()
userJohn.increment_login_attempts()

userJohn.reset_login_attempts()

# **Advanced**: Add an attribute called `login_attempts` to your User class. 
# - Write a method called `increment_ login_attempts()` that increments the value of login_attempts by 1. 
# - Write another method called `reset_login_attempts()` that resets the value of `login_attempts` to 0. 
# - Make an instance of the User class and call `increment_login_attempts()` several times. Print the value of login_attempts to make sure it was incremented properly, and then call `reset_login_attempts()`. Print `login_attempts` again to make sure it was reset to 0.
# **Consider**: Although the full implementation would be very complex, consider how this functionality might be incorporated into a real user-management app. 

# ### 3.
# Create a class called "Car" with attributes for make, model, and year. 
# Implement a method called get_info() to print out the details of the car. 
# Create instances representing different cars and call the get_info() method for each instance.
# - Stretch and Challenge: Add an attribute called "mileage" to the Car class and implement methods to set and update the mileage of the car.
class Car():
    def __init__(self, make, model, year,mileage):
        self.make = make 
        self.model = model
        self.year = year
        self.mileage = mileage

    def get_info(self):
        print(f'Make: {self.make} \nModel: {self.model} \nYear: {self.year} \nMileage: {self.mileage}')

    def set_mileage(self):
        add_2_miles = self.mileage =+ 2
        print(f'Mileage is {add_2_miles}')

    def update_mileage(self, new_miles):
        new_mileage = self.mileage + new_miles
        print(f'New mileage is {new_mileage}')

hyundai = Car('Hyundai','i10', 2020, 0)

hyundai.get_info()
hyundai.set_mileage()
hyundai.update_mileage(5)

# ### 4.
# Define a class called "Book" with attributes for title, author, and genre. Implement a method called display_info() to print out the details of the book. 
# Create instances representing different books and call the display_info() method for each instance.
class Book():
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        
    def display_info(self):
        print(f'Title: {self.title} \nAuthor: {self.author} \nGnere: {self.genre}')
    
    def set_pages(self):
        print(f'Self pages: {self.pages}')
        set_page = self.pages + 2
        self.pages = set_page
        print(f'Pages: {set_page}')

    def update_pages(self, new_page):
        updated_pages = self.pages + new_page
        print(f'Updated pages: {updated_pages}')


peace = Book('Peaceful', 'Won', 'Spiritual', 20)

peace.display_info()
peace.set_pages()
peace.update_pages(5)

# **Advanced**: Add an attribute called "pages" to the Book class and implement methods to set and update the number of pages in the book.

# ### 5.
# Create a class called "BankAccount" with attributes for account number, account holder, and balance. 
# Implement methods for depositing and withdrawing money from the account, as well as checking the balance. 
# Create instances representing different bank accounts and perform transactions on them.
class BankAccount():
    def __init__(self, account_number, account_holder, account_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_balance = account_balance
        
    def depositing(self, deposit):
        final_balance = self.account_balance + deposit
        self.account_balance = final_balance
        print(f'Depositing: {deposit} \nFinal balance: {self.account_balance}')

    def withdrawing(self, amount):
        new_balance = self.account_balance - amount
        self.account_balance = new_balance
        print(f'Withdrawing: {amount} \nAccount balance: {self.account_balance}')

wonAccount = BankAccount('28282', 'Won', 20)

wonAccount.depositing(2)
wonAccount.withdrawing(1)
# **Advanced**: Add an attribute called "interest_rate" to the BankAccount class and implement methods to calculate and apply interest to the account balance.

