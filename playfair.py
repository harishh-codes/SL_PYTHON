# Function to generate the Playfair cipher key matrix
def generate_key_matrix(keyword):
    # Remove duplicates from the keyword and convert to uppercase
    keyword = "".join(sorted(set(keyword), key=keyword.index)).upper()

    # Create the matrix, initializing it with the alphabet (excluding 'J')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    for char in keyword:
        if char in alphabet:
            matrix.append(char)
            alphabet = alphabet.replace(char, '')

    # Add the rest of the alphabet to the matrix
    matrix.extend(alphabet)

    # Convert the list to a 5x5 matrix
    key_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]
    return key_matrix

# Function to prepare the message (insert X between repeated letters, handle odd length)
def prepare_message(message):
    message = message.upper().replace('J', 'I')
    prepared_message = ""
    i = 0
    while i < len(message):
        if i + 1 < len(message) and message[i] == message[i + 1]:
            prepared_message += message[i] + 'X'
            i += 1
        else:
            prepared_message += message[i]
            i += 1

    # If the length is odd, add an 'X' at the end
    if len(prepared_message) % 2 != 0:
        prepared_message += 'X'
    
    return prepared_message

# Function to find the position of a character in the key matrix
def find_position(char, key_matrix):
    for row in range(5):
        for col in range(5):
            if key_matrix[row][col] == char:
                return row, col

# Function to encrypt the message using the Playfair cipher
def encrypt_playfair(message, key_matrix):
    encrypted_message = ""
    message = prepare_message(message)

    # Process the message two letters at a time
    for i in range(0, len(message), 2):
        char1, char2 = message[i], message[i+1]
        row1, col1 = find_position(char1, key_matrix)
        row2, col2 = find_position(char2, key_matrix)

        # If both letters are in the same row
        if row1 == row2:
            encrypted_message += key_matrix[row1][(col1 + 1) % 5]
            encrypted_message += key_matrix[row2][(col2 + 1) % 5]
        # If both letters are in the same column
        elif col1 == col2:
            encrypted_message += key_matrix[(row1 + 1) % 5][col1]
            encrypted_message += key_matrix[(row2 + 1) % 5][col2]
        # If neither, form a rectangle by swapping columns
        else:
            encrypted_message += key_matrix[row1][col2]
            encrypted_message += key_matrix[row2][col1]

    return encrypted_message

# Function to decrypt the message using the Playfair cipher
def decrypt_playfair(encrypted_message, key_matrix):
    decrypted_message = ""

    # Process the encrypted message two letters at a time
    for i in range(0, len(encrypted_message), 2):
        char1, char2 = encrypted_message[i], encrypted_message[i+1]
        row1, col1 = find_position(char1, key_matrix)
        row2, col2 = find_position(char2, key_matrix)

        # If both letters are in the same row
        if row1 == row2:
            decrypted_message += key_matrix[row1][(col1 - 1) % 5]
            decrypted_message += key_matrix[row2][(col2 - 1) % 5]
        # If both letters are in the same column
        elif col1 == col2:
            decrypted_message += key_matrix[(row1 - 1) % 5][col1]
            decrypted_message += key_matrix[(row2 - 1) % 5][col2]
        # If neither, form a rectangle by swapping columns
        else:
            decrypted_message += key_matrix[row1][col2]
            decrypted_message += key_matrix[row2][col1]

    return decrypted_message

# Main function to take input from the user
if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt a message: ").lower()
    message = input("Enter the message: ")
    keyword = input("Enter the keyword: ")

    key_matrix = generate_key_matrix(keyword)

    if choice == 'encrypt':
        encrypted_message = encrypt_playfair(message, key_matrix)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'decrypt':
        decrypted_message = decrypt_playfair(message, key_matrix)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")
