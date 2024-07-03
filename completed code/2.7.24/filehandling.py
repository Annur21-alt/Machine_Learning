#open('fruits.txt', 'xt')

#import os
#os.path.exists('filename')
#from os import path
#path.exists('filename')
from os.path import exists

def keyboardInput(datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while(isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if (value.strip() == ""):
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def doMenu(filename):
    choice = -1
    while (choice != 0):
        print("---------------")
        print("|  0 - Exit   |")
        print("|  1 - List   |")
        print("|  2 - Add    |")
        print("|  3 - Edit   |") 
        print("|  4 - Delete |") 
        print("---------------")
        choice = keyboardInput(int, "Choice [0,1,2,3,4]: ", "Choice must be Integer")
        if (choice == 0):
            print ("Thank you for using our system")
            break  
        elif (choice == 1):
            printProduct(filename)
        elif (choice == 2):
            addProduct(filename)
            printProduct(filename)
        elif (choice == 3):
            editProduct(filename)
        elif (choice == 4):
            deleteProduct(filename)


#filename = "fruits.txt"
#if exists(filename):
#    pass
#else:
#    open(filename, 'xt')


def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename,"xt")
        except Exception as e:
            print("Something went wrong when we create the file:", e)
        else:
            createTitle(filename)
        finally:
            filehandler.close()


def createTitle(filename):
    try:
        with open(filename,'wt') as filehandler:
            # here | (pipe) is used as delimiter
            # we can use delimiter to split the line into
            # multiple data
            # Television201455.55
            # Television | 20 |1455.55
            filehandler.write("Product|Quality|Price")
    except Exception as e:
        print("Something went wrong when we create the header:", e)


def addProduct(filename):
    try:
        product = keyboardInput(str,"Product: ","Product must be string")
        quantity = keyboardInput(int,"Quantity: ", "Quantity must be integer")
        price = keyboardInput(float,"Price: ", "Price must be Float")
        print("\n")
        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:
        print("Something went wrong when we add the product:", e)


def printProduct(filename):
    try:        
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            product, quantity, price = line.strip().split("|")
            if (index == 0):
                print(f"{"No. ":5}{product:40}{(quantity):>20}{(price):>20}")
                print("=" * 80)
            else:
                print(f"{index}. {product:40}{int(quantity):>20}{float(price):>20}")
    except Exception as e:
        print ("Something went wrong when we add the product:", e)


def editProduct(filename):
    try:
        # lines = None
        with open (filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in index product:","index must integer")
        #print (data)
        #data [1][1] = 15
        if (index >= len(lines)):
            print("sorry product not available")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str, "Are you sure you want edit [y/n]", "response not valid")
            if confirm == "y":
                # print("we will change list")
                newproduct = keyboardInput(str,f"Product:({product}): ","Product must be string")
                newquantity = keyboardInput(int,f"Quantity({quantity}): ", "Quantity must be integer")
                newprice = keyboardInput(float,f"Price({price}):", "Price must be Float")
                data[index] = [newproduct,newquantity,newprice]
                newlines = []
                for product in data:
                    line = "|".join(map(str,product)) +"\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename,"wt") as filehandler:
                    filehandler.writelines(newlines)                
    except Exception as e:
        print("Something went wrong when we edit the products:", e)


def deleteProduct(filename):
    try:
        # lines = None
        with open (filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in index product:","index must integer")
        #print (data)
        #data [1][1] = 15
        if (index >= len(lines)):
            print("sorry product not available")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str, "Are you sure you want to delete this product [y/n]", "response not valid")
            if confirm == "y":                
                del data[index] 
                newlines = []
                for product in data:
                    line = "|".join(map(str,product)) +"\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename,"wt") as filehandler:
                    filehandler.writelines(newlines)                
    except Exception as e:
        print("Something went wrong when we edit the products:", e)


filename = "fruits.txt"
createFile(filename)
doMenu(filename)
#addProduct(filename)
#printProduct(filename)
