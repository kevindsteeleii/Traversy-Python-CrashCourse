# A Tuple is a collection which is ordered and UNCHANGEABLE. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes')) # create using a constructor

# Single value needs a trailing comma
fruits2 = ('Apples',) 

# Get a value
print(fruits[1])

# Unlike with a list, tuples cannot change the value
# fruits[0] = 'Pears'

# Delete tuple
# del fruits2

# Get length
print(len(fruits))

# print(fruits2)

# print(fruits, fruits2)

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Remove from set
fruits_set.remove('Grapes')

# Clear set, but the set itself persists
# fruits_set.clear()

# Delete
# del fruits_set

# No duplicate members
fruits_set.add('Mango') # it ignores it!!


print(fruits_set)