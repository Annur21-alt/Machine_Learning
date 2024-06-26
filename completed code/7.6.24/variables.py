# product is the variable 
# "Television" is the string value/literal
# to differentiate the variables from values we use double quote ""
# or single quote ''
# product = 'Television'
product = "Television" # string
quantity = 2 # integer
price = 1455.25 # float
available = True # True / False (boolean value/literal)
print("Product:", product)
print("Quantity:", quantity)
print("Price:", price)
print("Available:", available)

# type is another built in function that tell us what is the
# data type of the variables (dynamically assigned by python)
# ((a + b) * c)
print(type(product))
print(type(quantity))
print(type(price))
print(type(available))

total = quantity * price
print("Total:", total)

# In real world use cases the 10 will not be hard coded
# the 10 is coming from an input device (keyboard)
# So the input value can be a string which needs to be converted
quantity = "10"
print(type(quantity))
price = "1455.55"
# print(quantity * price)

# type casting
# convert one data type to another
# to convert string to integer we have a built in function int
# to convert string to float we have a built in function float
total = int(quantity) *  float(price)
print(total)

x = 100
print(x)
# Now i want to know the address location where 100 is
# we can use a built in function called id
print(id(x))

y = 100
# however in python, the object 100 is not created first
# python scan first and if the object 100 already exists then
# python will reuse the object instead of re-creating the object
print(id(y))

a = "Hello"
b = "Hello"
print(id(a))
print(id(b))

# So far we have seen how to assign single value to a single variable
# in one line of statement
# x = 100

# how to assign more than one value to more than one variable
# in one line of statement
x, y = 101, 102

# you can also do this
x, y = 101 + 1, 102 + 1
x, y = x + 1, y + 1
print(x, y)

# In some programming language you can assign
# multiple variables with a single value
# x, y = 501 # however in python this is not allowed

# In other programming language we call these as variable initialization
# But in python there is no way for you to create a variable
# without assigning a value
y = 0 # numeric initialization
y = "" # string initialization / empty string
y = None
print(type(y))

# functions can be treated as variable but will have side effects
# print = 10
# print(print)
# keywords cannot be variables
# if = 10