# Strings in python are surrounded by either single or double quotation marks.

name = 'Kevin'
age = 32

# Concatenate
# print('Hello my name is '+ name + ' and I am '+ str(age))

# String Formatting

# Arguments by Position
# print('My name is {name} and I am {age} years old.'.format(name=name, age=age))
# print('My name is {} and I am {} years old.'.format(name, age))

# F-Strings (3.6+), it formats strings
# print(f'Hello my name is {name} and I am {age}')

# String Methods
s = 'hello world'

# Capitalize
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# Swap Case
print(s.swapcase())

# Is alphanumeric
print(s.isalnum())

# Is alpha only
print(s.isalpha())

# And many more