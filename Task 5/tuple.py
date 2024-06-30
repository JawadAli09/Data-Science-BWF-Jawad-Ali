# Creating Tuples
tup = (4, 5, 6)  # Define a tuple with three elements

# Converting to Tuple
tup = tuple([4, 0, 2])  # Convert a list to a tuple
tup = tuple('string')  # Convert a string to a tuple

# Accessing Elements
first_element = tup[0]  # Access the first element of the tuple

# Nested Tuples
nested_tup = ((4, 5, 6), (7, 8))  # Define a nested tuple
first_nested = nested_tup[0]  # Access the first nested tuple
second_nested = nested_tup[1]  # Access the second nested tuple

# Mutability
tup = (4, [1, 2], True)  # Tuples can contain mutable objects like lists
tup[1].append(3)  # Modify the list inside the tuple

# Concatenating Tuples
concatenated_tup = (4, None, 'foo') + (6, 0) + ('bar',)  # Concatenate multiple tuples

# Multiplying Tuples
multiplied_tup = ('foo', 'bar') * 4  # Repeat the tuple elements

# Unpacking Tuples
tup = (4, 5, 6)  # Define a tuple
a, b, c = tup  # Unpack the tuple elements into variables

# Tuple Methods
tup = (1, 2, 2, 2, 3, 4, 2)  # Define a tuple
count_of_twos = tup.count(2)  # Count occurrences of an element
