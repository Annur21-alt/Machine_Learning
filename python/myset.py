# set uses {}
# set is modifiable (add, edit and delete)
# set is unordered (the items does not retain its position)
# set is not indexed (Do not have 0, 1, 2, 3, 4......)
# set does not allow duplicates

# in python this is the first time we are using {}
x = {10, 20, 30, 10, 40, 50, 20, 60, 70}
print(x)
# what do you observe
# 1) numbers are not in the same order as it was created
# 2) duplicate numbers are missing

# selection and indexing
# since set is not indexed you cannot retrieve the values using [] syntax
# to retrive the items inside the set
# only way is to use for loop
for i in x:
    print(i)

# modifiable
fruits = {"apple", "orange", "mango"}
print(fruits)
fruits.add("durian") # add at a random place
print(fruits)

# to delete an item in the set
fruits.remove("orange")
print(fruits)
# pop => randomly removes an item in the set
fruits.pop()
print(fruits)

# if you want to update an item
# 1) remove the item
# 2) add the new item

fruits =["apple", "orange", "mango","banana","apple"]
uniquefruits = set(fruits)
print(uniquefruits)

overseafruits = {"apple","orange","mango","grapes"}
localfruit = {"durian","rambutan","cempedak","banana","mangosteen"}
print(overseafruits.union(localfruit))
print(overseafruits.intersection(localfruit))
print(overseafruits.difference(localfruit))
print(localfruit.difference(overseafruits))

favoritefruits = {"durian","rambutan","mangosteen"}
print(favoritefruits.issubset(localfruit))
print(favoritefruits.issuperset(localfruit))
print(favoritefruits.isdisjoint(overseafruits))


emailcontent = """Article Writing Format: Suppose you have some opinions regarding a 
topic and you want to tell people about it. How will you do so? You can tell the opinions to 
persons near you. But what if you want to tell not only those people but, say, the world? How 
will you do so? You will write those opinions, isnt it?"""

words = emailcontent.split()
print(len(words))

uniquewords = set(words)
print(len(uniquewords))

print(uniquewords)

clean_word = []
for word in words:
    word = word.replace(",","")
    clean_word.append(word)

uniquewords = set(clean_word)
print(len(uniquefruits))
print(uniquewords)
