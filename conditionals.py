# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5

"""
# Comparison Operators ( ==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

y = 15

# If/Else 
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

x = y

# elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'Both variables are equal.')
else:
    print(f'{y} is greater than {x}')

x = 10

# Nested if
if x > 2:
    if x <=10: # not a great way to do this use a logical operator
        print('X is greater than 2 and less than or equal to 10')
# Logical Operators (and, or, not) - Used to combine conditional statements

# and
if x > 2 and x <= 10:
    print(f'X, {x} is greater than 2 and less than or equal to 10')

x = 20

# or
if x > 2 or x <= 10:
    print(f'X, {x} is either greater than 2 or less than or equal to 10')

if not(x == y):
    print(f'X, {x} is not equal to Y, {y}') """

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object
x = 3
numbers = [1, 2, 3, 4, 5, 6]

# in
if x in numbers:
    print(x in numbers)

x = 12
# not in
if x not in numbers:
    print(x not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

x = y
# is
if x is y:
    print(x is y)

x = 12
# is not
if x is not y:
    print(f'It is {x is not y} that X, {x} is not Y, {y}')



