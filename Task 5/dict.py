# Creating Dictionaries
empty_dict = {}  # Define an empty dictionary
d1 = {"a": "some value", "b": [1, 2, 3, 4]}  # Define a dictionary with key-value pairs

# Accessing and Modifying Elements
d1[7] = "an integer"  # Add a new key-value pair
value = d1["b"]  # Access a value by its key

# Checking Membership
is_key_in_dict = "b" in d1  # Check if a key is in the dictionary

# Deleting Elements
del d1[7]  # Delete a key-value pair
value = d1.pop("b")  # Remove a key and return its value

# Iterating Over Keys and Values
keys = list(d1.keys())  # Get a list of keys
values = list(d1.values())  # Get a list of values
items = list(d1.items())  # Get a list of key-value pairs

# Merging Dictionaries
d1.update({"b": "foo", "c": 12})  # Update the dictionary with another dictionary

# Creating Dictionaries from Sequences
key_list = ["a", "b", "c"]  # Define a list of keys
value_list = [1, 2, 3]  # Define a list of values
mapping = {key: value for key, value in zip(key_list, value_list)}  # Create a dictionary from key-value pairs

# Default Values
value = d1.get("nonexistent_key", "default_value")  # Get a value with a default if the key doesn't exist
