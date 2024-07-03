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
if not exists(filename):
    open(filename,"xt")
