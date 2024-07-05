# A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, 
# so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
# For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.
# Example: The quick brown fox jumps over the lazy dog.
# Your task is to figure out if a sentence is a pangram.


print("This program will figure out if a sentence is a pangram")

def isPangram(sentence):
    # sentence to lowercase
    sentence = sentence.lower()

    # set to store unique letters
    letters = set()

    # iterate through each character
    for character in sentence:

        # check the condition all 26 letters
        if 'a' <= character <= 'z':
            letters.add(character)

    return len(letters) == 26

#user input
sentence = input("Please enter the sentence:")

# check sentence
if isPangram(sentence):
    print("The sentence is pangram sentence.")
else:
    print("The sentence is a not pangram sentence.")
