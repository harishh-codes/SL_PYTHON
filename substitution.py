import string

# Function to create a substitution dictionary
def create_substitution_dict(key):
    # Create a mapping of plaintext letters to substitution letters
    substitution_dict = {}
    alphabet = string.ascii_uppercase  # Uppercase alphabet

    for plain_char, cipher_char in zip(alphabet, key):
        substitution_dict[plain_char] = cipher_char

    return substitution_dict

# Function to encrypt the message
def encrypt_substitution(plaintext, substitution_dict):
    ciphertext = []

    for char in plaintext:
        if char.upper() in substitution_dict:
            # Preserve case
            if char.isupper():
                ciphertext.append(substitution_dict[char])
            else:
                ciphertext.append(substitution_dict[char.upper()].lower())
        else:
            ciphertext.append(char)  # Non-alphabet characters remain unchanged

    return ''.join(ciphertext)

# Function to decrypt the message
def decrypt_substitution(ciphertext, substitution_dict):
    # Create a reverse substitution dictionary for decryption
    reverse_dict = {v: k for k, v in substitution_dict.items()}
    plaintext = []

    for char in ciphertext:
        if char.upper() in reverse_dict:
            # Preserve case
            if char.isupper():
                plaintext.append(reverse_dict[char])
            else:
                plaintext.append(reverse_dict[char.upper()].lower())
        else:
            plaintext.append(char)  # Non-alphabet characters remain unchanged

    return ''.join(plaintext)

# Main function to take input from the user
if __name__ == "__main__":
    # Define a substitution key (custom mapping of letters)
    key = input("Enter the substitution key (26 unique uppercase letters): ").upper()

    if len(key) != 26 or len(set(key)) != 26 or not all(char in string.ascii_uppercase for char in key):
        print("Error: Key must contain 26 unique uppercase letters.")
    else:
        choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt a message: ").lower()
        message = input("Enter the message: ")

        substitution_dict = create_substitution_dict(key)

        if choice == 'encrypt':
            encrypted_message = encrypt_substitution(message, substitution_dict)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'decrypt':
            decrypted_message = decrypt_substitution(message, substitution_dict)
            print(f"Decrypted message: {decrypted_message}")
        else:
            print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")
