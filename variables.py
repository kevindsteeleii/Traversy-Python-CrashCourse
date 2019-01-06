# A variabe is a container for a value, it is memory storage, can has dynamic typing

""" 
    This is a multiline comment
    or docstring (used to define a function's purpose)
    can be single or double quotes
"""

'''
    VARIABLE RULES:
    - Variables are also case sensitive ( Name != name)
    - Variables can start with only an alphanumeric character or and underscore "_"
    - Cannot have numbers at the start
'''

""" x = 1 # int
y = 2.5 # float
name = 'Bob' #str -> string in python
job = "Carpenter" #str as well can have single or double quotes
is_cool = True # bool -> boolean True and False not true and false """

# Multiple assignment
x, y, name, job, is_cool = (1, 2.5, 'Bob', "plumber", True)
print("Hi my name is, {}. I've been working as a {} for {} years. I have a family, my son is {}".format(name, job, y, x))

# Basic math 
a = x + y

# Casting
x = str(x)
y = int(y)
z = float(y)

print(type(z),z)
