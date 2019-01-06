# A List a collection which is ordered and changeable. Allows duplicate members. You know like an array

# Create a list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
# Use a constructor
# numbers2 = list((1,2,3,4,5))

# Get a value, it's 0 based like arrays
print(fruits[1])

# Get length
print(len(fruits))

# Append to END of list
fruits.append('Mango')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Change Value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)


print(fruits)