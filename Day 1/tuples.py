# Elements of a tuple cannot be changed once defined

tuple1 = ("a", "b", "c")
print(tuple1[1])
# Indexing works normally in tuple 

# Tuple has only a few inbuilt functions

# First is count, retrieves the number of times an element repeates itself in a tuple
print(tuple1.count('b')) 

# Index retrieves the first occurence index of that element
print(tuple1.index("c"))