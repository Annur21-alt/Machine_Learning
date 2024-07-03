def compress_string(s):
    # Handle edge case of empty string
    if not s:
        return ""

    compressed = []
    count = 1

    # Iterate over the string, count consecutive characters
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    # Append the last character and its count
    compressed.append(s[-1] + str(count))

    # Convert the list to a string
    compressed_string = ''.join(compressed)

    # Return the original string if compressed string is not smaller
    return compressed_string if len(compressed_string) < len(s) else s

# Example usage with user input
input_string = input("Enter a string to compress: ")
compressed_string = compress_string(input_string)
print("Compressed string:", compressed_string)
