
def listSixLetterFruits (*fruits):
    for fruit in fruits:
        if len(fruit) == 6: print(fruit)

listSixLetterFruits ("apple","orange","mango","banana","durian","grapes")


def listSixLetterFruits (*fruits):
    for fruit in fruits:
        print (fruit)

listSixLetterFruits ("apple",20,"orange",)
print("\n")

x = [10,20,30,40,50]
y=x
print(x)
print(y)
x[2] = 35
print(x)
print(y)


y = []
for i in x:
    y.append(i)
print("=" * 40)
print(x)
print(y)
x[2] = 35
print(x)
print(y)



x = [10,20,30,40,50]
y = x.copy()
print("=" * 40)
print(x)
print(y)
x[2] = 35
print(x)
print(y)


x = list([10,20,30,40,50])
print(x)
x = list([12,22,33,42,52])
print(x)








