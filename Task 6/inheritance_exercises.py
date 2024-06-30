# combined_modules.py

# Exercise 9-10: restaurant.py content
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is now open.")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def set_flavors(self, flavors):
        self.flavors = flavors

    def display_flavors(self):
        print("The available flavors are:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Exercise 9-11: user.py content
class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User {self.username}:")
        print(f"  Name: {self.first_name} {self.last_name}")
        print(f"  Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Exercise 9-11: admin.py content
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()


# Exercise 9-12: electric_car.py content
class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = f"This car can go approximately {range} miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
            print("The battery has been upgraded to 85 kWh.")
        else:
            print("The battery is already 85 kWh.")

class ElectricCar(Restaurant):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
