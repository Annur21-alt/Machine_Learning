# how to represent binary number
# you can use 0b followed by the binary number
# however it is stil an integer
# by adding 0b python starts reading it as one one one
# instead one hundred eleven

owner_permission = 0b111
print(owner_permission)

filepermission = 0b111101001 # now owner can read, write and execute
# group can read and execute
# others can execute only

# in datascience/machine learning when you were given
# categorical data you must convert to numbers
# which machine can understand
# this itself called "feature engineering"
# gender representation 01 for female and 10 for male
# race representation 1000 for malay and 0100 for chinese

# this bit extraction can be use using bitwise and operator
mask = 0b000111000
print(filepermission & mask)
#print("{0:b}".format((filepermission & mask)>>3))
print ((filepermission & mask) >> 3) # we manage to get group permission over the file


# in order to perform bit extraction we use bitwise & operator
# we are interested in 4, 5, 6 bits only
# Original Data             111101001  &
# Our mask                  000111000
# 4,5,6 bits extracted      000101000
# shift it to right 3 times 000000101 >> 3
print (bin((filepermission & mask) >> 3))


# Original Data              111101001  Or
# Our mask                   000111000
# 4,5,6 bits extracted       000101000
# shift it to right 3 times  111111001
# the operator is used to set specified bit to 1
# Please remember there is no way to set a specific bit to 0 using or operator
# Or operator is also used in extracting region of interest in a image
print(bin(filepermission | mask))


# Original Data              111101001  ^
# Our mask                   000111000
# 4,5,6 bits extracted       111010001
# shift it to right 3 times  
# xor is used for encryption
message = 0b001011 # my content "3"
key = 0b00101100




givennumber = 5
print(~givennumber) #1s complement
print(~givennumber + 1) #2s complement

print(-givennumber) #unary negative
print(+givennumber) #unary positive




