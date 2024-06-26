print ("Hello World !!!")

def sayHelloWorld():
    print ("Hello World inside the function !!!")

sayHelloWorld ()

def greeting (name):
    print ("Good morning",name)

greeting("Aida")


def total(x,y,z):
    result = x + y + z
    print ("Result:",result)

total (10,20,30)

def buylunch (makan, minum):
    print (makan,minum)
    for food in makan:
        if (food == "nasi"):
            print ()
















itemprices = buylunch (["nasi","sayur"], ["nescafe"])
total = 0
for price in itemprices:
    total = total + price
print ("Total to be paid:", total)




