import random, time

def decrypt(ciphertext, key):
    plaintext = ""
    index = 0

    while index < len(ciphertext):
        plaintext += ciphertext[index]
        index += key + 1

    return plaintext

# Main program starts here...
# Input...
ciphertext = input("Enter the encrypted message (ciphertext): ")
key = int(input("Input the key as a number between 1 and 10: "))
while not (key >= 1 and key <= 10):
    print("Invalid key, try again!")
    key = int(input("Input the key as a number between 1 and 10: "))

# Process...
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
