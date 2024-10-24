from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

# Function to encrypt a plaintext using DES
def encrypt(plaintext, key):
    # Create a DES cipher object
    cipher = DES.new(key, DES.MODE_CBC)
    
    # Pad the plaintext to be a multiple of 8 bytes
    padded_plaintext = pad(plaintext.encode(), DES.block_size)
    
    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_plaintext)
    
    return cipher.iv, ciphertext  # Return the IV and ciphertext

# Function to decrypt a ciphertext using DES
def decrypt(iv, ciphertext, key):
    # Create a DES cipher object
    cipher = DES.new(key, DES.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext)
    
    # Unpad the plaintext
    plaintext = unpad(padded_plaintext, DES.block_size).decode()
    
    return plaintext

# Main function
if __name__ == "__main__":
    # 8-byte key for DES (must be exactly 8 bytes)
    key = input("Enter an 8-byte key (e.g., 'abcdefgh'): ").encode()

    if len(key) != 8:
        print("Key must be exactly 8 bytes long.")
    else:
        # Ask user for the operation to perform
        option = input("Choose an option:\n1. Encrypt\n2. Decrypt\nEnter 1 or 2: ")

        if option == '1':
            plaintext = input("Enter the plaintext to encrypt: ")
            iv, ciphertext = encrypt(plaintext, key)
            print("Ciphertext (hex):", ciphertext.hex())
            print("IV (hex):", iv.hex())  # Display the IV in hexadecimal
        elif option == '2':
            ciphertext_hex = input("Enter the ciphertext (hex) to decrypt: ")
            iv_hex = input("Enter the IV (hex) used for encryption: ")

            # Convert hex strings to bytes
            iv = bytes.fromhex(iv_hex)
            ciphertext = bytes.fromhex(ciphertext_hex)

            decrypted_text = decrypt(iv, ciphertext, key)
            print("Decrypted text:", decrypted_text)
        else:
            print("Invalid option. Please choose 1 or 2.")
