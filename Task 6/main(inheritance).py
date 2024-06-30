# Example usage in a main script

from inheritance_exercises import *

# Using Restaurant and IceCreamStand
ice_cream_stand = IceCreamStand("Cool Cones")
ice_cream_stand.set_flavors(["vanilla", "chocolate", "strawberry", "mint"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()

# Using User and Admin
admin = Admin("John", "Doe", "admin_john", "admin@example.com")
admin.describe_user()
admin.privileges.show_privileges()

# Using ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.describe_restaurant()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
