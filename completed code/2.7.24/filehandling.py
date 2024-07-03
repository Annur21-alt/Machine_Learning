#open('fruits.txt', 'xt')

#import os
#os.path.exists('filename')
#from os import path
#path.exists('filename')
from os.path import exists

filename = "fruits.txt"
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
        finally:
            filehandler.close()


filename = "fruits.txt"
createFile(filename)