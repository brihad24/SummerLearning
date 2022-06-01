# Unordered items that are indexed
# Useful in DBMS since most of the databases have pairs of data indexed with keys 

dic1 = {"Car1" : "Audi", "Car2" : "BMW", "Car3" : "Benz"}
# Here, the elements are paired, where first element is the index for that element

# We use indexing in dictionary, not with numbers, but with the keys assigned to the elements
print(dic1['Car1'])

# To print keys
for x in dic1:
    print(x)

# To print values
for x in dic1.values():
    print(x)

# To print entire data items
for x in dic1.items():
    print(x)

# To add items to a dictionary
dic1['Car4'] = 'MS'
print(dic1)

# To replace existing value
dic1['Car1'] = 'Toyota'
print(dic1)

# Nested Dictionaries
car1_model = {'Benz' : 1960}
car2_model = {'Audi' : 1970}
car3_model = {'Ambassador' : 1980}

car_type = {'car1' : car1_model, 'car2' : car2_model, 'car3' : car3_model}
print(car_type)

# To access a specific value, such as 1970 here, we use 2 indexes to retrieve the value
print(car_type['car2']['Audi'])