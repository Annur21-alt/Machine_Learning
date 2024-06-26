# Whenever you want to iterate a list of items then you must use for loop
fruits = ["apple", "rambutan", "orange", "durian", "mango", "cempedak", "banana", "mangosteen", "grapes"]
# print all the items in the list
for fruit in fruits:
    print(fruit)

# print all the items in the even position
for fruit in fruits[::2]:
    print(fruit)

# print only fruits with 6 letters
for fruit in fruits:
    if (len(fruit) == 6):
        print(fruit)

# I want to print each fruit together with the idex (position)
position = 0
for fruit in fruits:
    print(position, fruit)
    position += 1
