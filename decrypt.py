def decrypt(ciphertext, key):
    plaintext = ""
    index = 0

    while index < len(ciphertext):
        plaintext += ciphertext[index]
        index += key + 1

    return plaintext


# Main program starts here...
# Input...
plaintext = input("Enter a message to encrypt (plaintext): ")
key = int(input("Input a key as a number between 1 and 10: "))
while not (key >= 1 and key <= 10):
    print("Invalid key, try again!")
    key = int(input("Input a key as a number between 1 and 10: "))

# Process...
print("...")
time.sleep(1)
print("Encrypting plaintext...")
time.sleep(1)
print("...")
time.sleep(1)
ciphertext = encrypt(plaintext, key)

# Output...
print("Ciphertext:")
print(ciphertext)

# Decryption process...
print("...")
time.sleep(1)
print("Decrypting ciphertext...")
time.sleep(1)
print("...")
time.sleep(1)
decrypted_plaintext = decrypt(ciphertext, key)

# Output...
print("Decrypted Plaintext:")
print(decrypted_plaintext)
