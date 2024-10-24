# Function to generate the key in a repeating pattern of the length of the message
def generate_key(message, keyword):
    keyword = list(keyword)
    if len(message) == len(keyword):
        return keyword
    else:
        for i in range(len(message) - len(keyword)):
            keyword.append(keyword[i % len(keyword)])
    return "".join(keyword)

# Function to encrypt the message
def encrypt_vigenere(message, key):
    encrypted_text = []
    for i in range(len(message)):
        char = message[i]

        if char.isupper():  # For uppercase characters
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
        elif char.islower():  # For lowercase characters
            encrypted_char = chr((ord(char) + ord(key[i].lower()) - 2 * ord('a')) % 26 + ord('a'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Non-alphabet characters remain unchanged

    return "".join(encrypted_text)

# Function to decrypt the message
def decrypt_vigenere(encrypted_message, key):
    decrypted_text = []
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]

        if char.isupper():  # For uppercase characters
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
        elif char.islower():  # For lowercase characters
            decrypted_char = chr((ord(char) - ord(key[i].lower()) + 26) % 26 + ord('a'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)  # Non-alphabet characters remain unchanged

    return "".join(decrypted_text)

# Main function to take input from the user
if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt a message: ").lower()
    message = input("Enter the message: ")
    keyword = input("Enter the keyword: ")

    key = generate_key(message, keyword)

    if choice == 'encrypt':
        encrypted_message = encrypt_vigenere(message, key)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'decrypt':
        decrypted_message = decrypt_vigenere(message, key)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")
