# Creating Lists
a_list = [2, 3, 7, None]  # Define a list with multiple elements
tup = ("foo", "bar", "baz")  # Define a tuple
b_list = list(tup)  # Convert a tuple to a list

# Modifying Lists
b_list[1] = "peekaboo"  # Modify an element in the list

# Adding Elements
b_list.append("dwarf")  # Append an element to the end of the list

# Inserting Elements
b_list.insert(1, "red")  # Insert an element at a specific position

# Removing Elements
b_list.pop(2)  # Remove and return an element at a specific position
b_list.remove("foo")  # Remove the first occurrence of an element

# Checking Membership
is_in_list = "dwarf" in b_list  # Check if an element is in the list

# Concatenating Lists
concatenated_list = [4, None, "foo"] + [7, 8, (2, 3)]  # Concatenate two lists

# Extending Lists
x = [4, None, "foo"]  # Define a list
x.extend([7, 8, (2, 3)])  # Extend the list with elements from another list

# Sorting Lists
a = [7, 2, 5, 1, 3]  # Define a list
a.sort()  # Sort the list in ascending order

# Slicing Lists
seq = [7, 2, 3, 7, 5, 6, 0, 1]  # Define a list
slice1 = seq[1:5]  # Get a slice of the list
slice2 = seq[:5]  # Get a slice from the beginning
slice3 = seq[3:]  # Get a slice to the end

# List with Step
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Define a list
even_elements = seq[::2]  # Get every second element
reversed_list = seq[::-1]  # Reverse the list
