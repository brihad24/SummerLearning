# Anything with sqaure brackets
list1 = [] # One way  of declaring a list
list2 = list() # Another way of declaring list
# list() is an inbuilt function

# Use of ',' separated values to add items to list
NewList = ['Math', 'Chem', 1 , 2, 3, 4]
print(NewList)
print(len(NewList))

# Indexing starts from 0 and so on till n-1
print(NewList[1])
 
# Append func adds an item to the list
NewList.append('Me')
print(NewList)

# :(colon) specifies how many items from which side have to displayed
print(NewList[:]) 

# print(NewList[a:b]), Here a and b specify indexes of the items in list
# this command displays all the items from a to b-1
# default of a is 0, default of b is n-1
print(NewList[1:5]) 

# Nested list is when one list contains another list
NewList.append(['where', 'when']) 
# Here, [where, when] is a new list, and we appended this list to NewList
print(NewList)

# Insert function helps add or append items to a certain index in a list
# We first specify the index where we want to add the item, then specify what we want to add
NewList.insert(1,"Hello")
print(NewList)

DiffList = [1, 2, 3, 4, 5, 6]

# Extend function adds the elements inside a list to the og list, instead of creating a nested list like append
DiffList.extend([8, 9])
print(DiffList)

