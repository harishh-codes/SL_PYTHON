# Function to encrypt the message using the transposition cipher
def encrypt_transposition(plaintext, key):
    # Create a list of empty strings for each column
    columns = [''] * key
    
    # Fill the columns by iterating through the plaintext
    for index, char in enumerate(plaintext):
        column_index = index % key
        columns[column_index] += char
    
    # Join the columns to get the ciphertext
    ciphertext = ''.join(columns)
    return ciphertext

# Function to decrypt the message using the transposition cipher
def decrypt_transposition(ciphertext, key):
    # Calculate the number of complete columns and the remainder
    num_columns = len(ciphertext) // key
    remainder = len(ciphertext) % key
    
    # Calculate the number of rows
    num_rows = num_columns + (1 if remainder > 0 else 0)

    # Create a list to hold the plaintext
    plaintext = [''] * num_rows

    # Fill in the plaintext from the ciphertext
    col = 0
    row = 0
    for char in ciphertext:
        plaintext[row] += char
        row += 1

        # If we reach the end of a column, go back to the start
        if (row == num_rows) or (col < remainder and row == num_columns + 1):
            row = 0
            col += 1

    # Join the rows to get the final plaintext
    return ''.join(plaintext)

# Main function to take input from the user
if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt a message: ").lower()
    message = input("Enter the message: ")
    key = int(input("Enter the key (number of columns): "))

    if choice == 'encrypt':
        encrypted_message = encrypt_transposition(message, key)  # Pass the key here
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'decrypt':
        decrypted_message = decrypt_transposition(message, key)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")
