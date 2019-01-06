# A function is a block of code which only runs when it is called. In Python, we don not use curly brackets, we use indentation with tabs or space

# Create function
def say_hello():
    name = input('Enter name here and then press enter:\n')
    print(f'Hello {name}')

# say_hello()

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total
num = getSum(3, 4)
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions. 

lamdaSum = lambda num1, num2: num1 + num2

print(lamdaSum(10, 3))