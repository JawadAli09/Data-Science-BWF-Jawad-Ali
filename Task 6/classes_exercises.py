# Exercise 9-1: Restaurant
class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
       
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")
    
    def open_restaurant(self):
        
        print(f"{self.restaurant_name} is now open.")

# Creating an instance of Restaurant
restaurant = Restaurant('The Food Place', 'Italian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Exercise 9-2: Three Restaurants
restaurant1 = Restaurant('The Food Place', 'Italian')
restaurant2 = Restaurant('Sushi World', 'Japanese')
restaurant3 = Restaurant('Burger Town', 'American')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Exercise 9-3: Users
class User:
    def __init__(self, first_name, last_name, username, email):
       
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
    
    def describe_user(self):
        print(f"User: {self.username}")
        print(f"Full Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
    
    def greet_user(self):
        
        print(f"Hello, {self.first_name}! Welcome back.")


user1 = User('John', 'Doe', 'jdoe', 'jdoe@example.com')
user2 = User('Jane', 'Smith', 'jsmith', 'jsmith@example.com')
user3 = User('Alice', 'Johnson', 'ajohnson', 'ajohnson@example.com')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()


# Exercise 9-4: Number Served
# solution
class Restaurant:
    """A simple attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Print the name and cuisine type of the restaurant."""
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        
        print(f"{self.restaurant_name.title()} is now open!")
    
    def set_number_served(self, number):
        
        self.number_served = number
    
    def increment_number_served(self, additional_customers):
        
        self.number_served += additional_customers


restaurant = Restaurant('happy cafe', 'continental')

# the number served and change it
print(f"Number served: {restaurant.number_served}")
restaurant.number_served = 10
print(f"Number served: {restaurant.number_served}")


restaurant.set_number_served(20)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(30)
print(f"Number served: {restaurant.number_served}")

# Exercise 9-5: Login Attempts
# solution
class User:
    """A simple attempt to model a user."""
    
    def __init__(self, first_name, last_name, age, email):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
       
        print(f"User: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
    
    def greet_user(self):
        
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('john', 'doe', 28, 'john.doe@example.com')

# Increment login attempts
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")

# Reset login attempts
user1.reset_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
