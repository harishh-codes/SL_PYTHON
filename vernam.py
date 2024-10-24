import random

# Function to generate a random key
def generate_key(length):
    # Generate a random key consisting of uppercase letters
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

# Function to encrypt the message using the Vernam cipher
def encrypt_vernam(plaintext, key):
    ciphertext = []
    for p_char, k_char in zip(plaintext, key):
        # Convert characters to 0-25 range
        p_val = ord(p_char) - ord('A')
        k_val = ord(k_char) - ord('A')

        # Apply the Vernam cipher formula
        c_val = (p_val + k_val) % 26
        ciphertext.append(chr(c_val + ord('A')))
    
    return ''.join(ciphertext)

# Function to decrypt the message using the Vernam cipher
def decrypt_vernam(ciphertext, key):
    plaintext = []
    for c_char, k_char in zip(ciphertext, key):
        # Convert characters to 0-25 range
        c_val = ord(c_char) - ord('A')
        k_val = ord(k_char) - ord('A')

        # Apply the Vernam cipher formula
        p_val = (c_val - k_val + 26) % 26
        plaintext.append(chr(p_val + ord('A')))
    
    return ''.join(plaintext)

# Main function to take input from the user
if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt a message: ").lower()
    message = input("Enter the message (uppercase letters only): ").replace(" ", "").upper()

    if choice == 'encrypt':
        # Generate a key of the same length as the message
        key = generate_key(len(message))
        encrypted_message = encrypt_vernam(message, key)
        print(f"Encrypted message: {encrypted_message}")
        print(f"Key: {key}")  # Display the key used for encryption
    elif choice == 'decrypt':
        key = input("Enter the key (uppercase letters only): ").upper()
        if len(key) != len(message):
            print("Error: Key length must match the message length.")
        else:
            decrypted_message = decrypt_vernam(message, key)
            print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")
