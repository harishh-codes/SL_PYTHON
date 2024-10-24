# Function to encrypt the message
def encrypt(text, shift):
    result = ""

    # Traverse the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # For non-alphabet characters, leave them unchanged
        else:
            result += char

    return result

# Function to decrypt the message
def decrypt(text, shift):
    result = ""

    # Traverse the text
    for i in range(len(text)):
        char = text[i]

        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)

        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        
        # For non-alphabet characters, leave them unchanged
        else:
            result += char

    return result

# Main function to take input from the user
if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt a message: ").lower()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'encrypt':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'decrypt':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")
