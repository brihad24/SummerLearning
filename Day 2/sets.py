# Sets are unordered, and cannot have duplicate values

# set() is a function that helps create a set
demo_set = set() # An empty set is created here
print(demo_set)

# We declare set using '{}'
set1 = {1, 2, 3, 3, 4} 
print(set1) # Prints only one '3' since set cannot have duplicate values

set2 = {"a", "b", "c"}
# Indexing does not exist in sets

# Functions in sets

# Adds another element in the set
set2.add("ok") 
print(set2)

set3 = {"a", "b", "c", "d", "e"}

# Difference removes all the common elements from the initial set
print(set3.difference(set2))