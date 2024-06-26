# 4 types built in data structure
# list,tuple,set,dictionary

fruits = (["apple","orange","manggo","banana"])
print (fruits)

fruits.append("durian")
print(fruits)

fruits.insert(1,"rambutan")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.pop()
print(fruits)
'''
greeting = "Good morning"
del greeting
print (greeting)
'''
del fruits[3]
print(fruits)

fruits.clear()
print(fruits)


del fruits
#print(fruits)

fruits = (["apple","manggo","orange","manggo","banana","apple","manggo","orange"])
print(fruits.index("manggo"))

newfruits = fruits[2:] 
print (fruits.index("manggo") + 1)

print(list(enumerate(fruits)))

for item in enumerate(fruits):
    if item [1] == "manggo" : print("manggo in position:", item[0])

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

for fruit in list(enumerate(fruits)):
    print (fruit)




