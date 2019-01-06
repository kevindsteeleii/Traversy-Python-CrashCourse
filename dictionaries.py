# A Dictionary is a collection which is unorder, changeable, and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use a constructor
# person2 = dict(first_name='Jane', last_name='Goodall')

# Get value
# print(person['first_name']) # in JS you would write person.name, here we only use square brackets and quotation marks
# print(person.get('last_name')) # Get method

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
# print(person.keys())

# Get dict items
# print(person.items())

# Copy a dict
person2 = person.copy() # similar to the spread operator
person2['city'] = 'New York City'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Length
print(len(person2))

# List of dict
people =[
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])

print(person, type(person))