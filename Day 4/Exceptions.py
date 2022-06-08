try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)

except ZeroDivisionError:
    print("Age cannot be 0")
    
except ValueError:
    print('Invalid value')

# Exception Handling is to handle exceptions which would normally crash the algo