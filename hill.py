# Function to generate the key matrix (3x3 matrix for this example)
def generate_key_matrix(key):
    key_matrix = []
    for char in key.upper():
        key_matrix.append(ord(char) % 65)
    
    # Reshape the key into a 3x3 matrix
    key_matrix = [key_matrix[i:i+3] for i in range(0, 9, 3)]
    return key_matrix

# Function to prepare the message (pad with 'X' if necessary)
def prepare_message(message):
    message = message.upper().replace(' ', '')
    if len(message) % 3 != 0:
        message += 'X' * (3 - len(message) % 3)  # Padding with 'X' to make length a multiple of 3
    return message

# Function to perform matrix multiplication mod 26
def matrix_multiply(matrix, vector):
    result = []
    for row in matrix:
        result.append((row[0] * vector[0] + row[1] * vector[1] + row[2] * vector[2]) % 26)
    return result

# Function to find the determinant of a 3x3 matrix mod 26
def determinant(matrix):
    det = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
           - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
           + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])) % 26
    return det

# Function to find the modular inverse of a number mod 26
def mod_inverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to find the cofactor matrix
def cofactor_matrix(matrix):
    cofactors = [
        [(matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) % 26,
         -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) % 26,
         (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) % 26],
        [-(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]) % 26,
         (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) % 26,
         -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]) % 26],
        [(matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) % 26,
         -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]) % 26,
         (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26]
    ]
    
    # Adjust negative values mod 26
    for i in range(3):
        for j in range(3):
            cofactors[i][j] = cofactors[i][j] % 26
    
    return cofactors

# Function to transpose a matrix
def transpose(matrix):
    return [[matrix[j][i] for j in range(3)] for i in range(3)]

# Function to find the inverse of a key matrix mod 26
def inverse_key_matrix(matrix):
    det = determinant(matrix)
    det_inv = mod_inverse(det, 26)
    
    if det_inv is None:
        raise ValueError("The key matrix is not invertible mod 26. Please use a different key.")
    
    cofactor_mat = cofactor_matrix(matrix)
    adjugate = transpose(cofactor_mat)

    # Multiply adjugate matrix by the modular inverse of the determinant
    inverse_matrix = [[(adjugate[i][j] * det_inv) % 26 for j in range(3)] for i in range(3)]
    
    return inverse_matrix

# Function to encrypt the message using the Hill Cipher
def encrypt_hill(message, key_matrix):
    encrypted_message = ""
    message = prepare_message(message)
    
    # Encrypt the message 3 characters at a time (as we are using a 3x3 key matrix)
    for i in range(0, len(message), 3):
        # Convert the block of 3 characters into a vector
        message_vector = [ord(char) % 65 for char in message[i:i + 3]]
        
        # Multiply the key matrix with the message vector
        encrypted_vector = matrix_multiply(key_matrix, message_vector)
        
        # Convert the encrypted vector back to characters
        for num in encrypted_vector:
            encrypted_message += chr(num + 65)
    
    return encrypted_message

# Function to decrypt the message using the Hill Cipher
def decrypt_hill(encrypted_message, key_matrix):
    decrypted_message = ""

    # Find the inverse of the key matrix mod 26
    key_matrix_inv = inverse_key_matrix(key_matrix)

    # Decrypt the message 3 characters at a time
    for i in range(0, len(encrypted_message), 3):
        # Convert the block of 3 characters into a vector
        encrypted_vector = [ord(char) % 65 for char in encrypted_message[i:i + 3]]
        
        # Multiply the inverse key matrix with the encrypted vector
        decrypted_vector = matrix_multiply(key_matrix_inv, encrypted_vector)
        
        # Convert the decrypted vector back to characters
        for num in decrypted_vector:
            decrypted_message += chr(num + 65)
    
    return decrypted_message

# Main function to take input from the user
if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt a message: ").lower()
    message = input("Enter the message: ")
    key = input("Enter a 9-letter keyword (to form a 3x3 matrix): ")

    if len(key) != 9:
        print("Invalid key length. Please enter a 9-letter keyword.")
    else:
        key_matrix = generate_key_matrix(key)
        
        # Check if the key matrix is invertible before encryption/decryption
        try:
            if choice == 'encrypt':
                encrypted_message = encrypt_hill(message, key_matrix)
                print(f"Encrypted message: {encrypted_message}")
            elif choice == 'decrypt':
                decrypted_message = decrypt_hill(message, key_matrix)
                print(f"Decrypted message: {decrypted_message}")
            else:
                print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")
        except ValueError as e:
            print(e)
