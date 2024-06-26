message = 0b01001010 # my content "J"
key = 0b00101100 # encryption key ","
encrypted_message = message ^ key
print(bin(encrypted_message))
decrypted_message = encrypted_message ^ key
print(bin(decrypted_message))

