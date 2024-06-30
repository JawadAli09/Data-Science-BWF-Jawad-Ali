# Creating Sets
a_set = set([2, 2, 2, 1, 3, 3])  # Define a set with unique elements
b_set = {2, 2, 2, 1, 3, 3}  # Define a set using curly braces

# Adding Elements to Sets
a_set.add(4)  # Add an element to the set

# Removing Elements from Sets
a_set.remove(2)  # Remove an element from the set

# Set Operations
set1 = {1, 2, 3, 4}  # Define a set
set2 = {3, 4, 5, 6}  # Define another set

# Union
union_set = set1.union(set2)  # Get the union of two sets

# Intersection
intersection_set = set1.intersection(set2)  # Get the intersection of two sets

# Difference
difference_set = set1.difference(set2)  # Get the difference between two sets

# Symmetric Difference
sym_diff_set = set1.symmetric_difference(set2)  # Get the symmetric difference between two sets

# Checking Subset and Superset
is_subset = {1, 2}.issubset(set1)  # Check if a set is a subset
is_superset = set1.issuperset({1, 2})  # Check if a set is a superset

# Copying Sets
copied_set = a_set.copy()  # Create a copy of the set
