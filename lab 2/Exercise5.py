#Write a Python program that takes a single character as input 
#and checks whether it is a vowel or consonant.

print("This program will show the single character that user input and check whether it is a vowel or consonant")

character = input("Please input one character of alphabet in lowercase:")

vowel1 = "a"
vowel2 = "e"
vowel3 = "i"
vowel4 = "o"
vowel5 = "u"

if(character == vowel1 or character == vowel2 or character == vowel3 or character == vowel4 or character == vowel5):
    print(character,"is vowel.")
else:
    print(character,"is consonant.")


