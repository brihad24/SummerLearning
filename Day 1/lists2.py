List1 = [1, 2, 3]

# Other functions with lists

print(sum(List1)) # Adds all the numbers inside list 

print(List1.pop(0)) # Picks out or removes an item at that index, default is set to last element
print(List1) # Here 1 is removed from the list

List2 = [1, 2, 1, 1, 2, 2, 2, 3]

print(List2.count(1)) # Prints the number of times '1' has been repeated

List3 = ['a', 'b', 'a', 'c', 'b']

print(List3.index('b')) # Prints the index of the first occurence of 'b' in the list

print(min(List2)) # Prints min element
print(max(List2)) # Prints max element

List4 = [1, 2, 3]

# Operations on lists

print(List4*3) # Appends the list 3 times