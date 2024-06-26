# tuple is nothing but readonly list
# tuple uses []
# tuple is not modifiable (cannot append, edit and delete)
# tuple is ordered (the items retain its position)
# tuple is indexed (0, 1, 2, 3, 4......)
# tuple allows duplicates

x = (10, 20, 30, 40, 50, 60, 70)
print(x)
print(type(x))

# selection and indexing 
# refer to variableparttwo.py
print(x[0])

# it is not modifiable
# which means you do not have append, insert, remove
# however you can delete the entire tuple using del keyword
# del x[0] # i repeat this is not allowed
del x

fruits = ("apple", "orange", "apple", "mango", "apple")
print(fruits.count("apple"))

# tuple is does not have many features as list
# why we use tuple ?
# since tuple do not have many feature obviously
# 1) take less space
# 2) faster than list
# normally python handles its collects using tuple
def returnFruits():
    # return keyword cannot return more than one value
    # so python must convert the values to "tuple"
    # whenever python automatically converts data to collection it is always a tuple
    return "apple", "orange"

print(type(returnFruits()))

def total(*numbers):
    print(type(numbers))
    result = 0
    for number in numbers:
        result = result + number
    return result

# As i mention earlier whenever python has to convert the data to a collection
# it will always use tuple
print(total(10, 20, 30, 40, 50, 60))

# one last feature in tuple
# tuple can auto explode
# explode means create 1 variable for every item in the tuple
fruits = ("apple", "orange", "mango")
fruit01 = fruits[0]
fruit02 = fruits[1]
fruit03 = fruits[2]
# however in python you no need to explode manually
fruit01, fruit02, fruit03 = fruits
# in other words we are assigning multiple items in the tuple to multiple variables

# there is a problem to highlight in tuple
x = (10)
# now python really confused is it tuple or expression
# python gives priority for expression than tuple
# automatically 10 (integer) is assigned to x
print(type(x))
# to ensure the data is in tuple format please add an extra comma
x = (10,)
print(type(x))