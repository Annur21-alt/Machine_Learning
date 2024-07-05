def is_pangram(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    
    # Create a set to store unique letters
    letters = set()
    
    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is a letter
        if 'a' <= char <= 'z':
            letters.add(char)
    
    # Check if the set contains all 26 letters
    return len(letters) == 26

# Get user input
sentence = input("Enter a sentence: ")

# Check if the sentence is a pangram
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
