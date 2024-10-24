# Function to decrypt the message using a specific shift
def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    
    for char in ciphertext:
        # Decrypt uppercase characters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char  # Non-alphabet characters remain unchanged
    
    return decrypted_text

# Function to perform a brute force attack on the Caesar cipher
def brute_force_caesar(ciphertext):
    print("Brute force decryption attempts:")
    
    for shift in range(1, 26):  # Try all possible shifts (1 to 25)
        decrypted_message = decrypt_caesar(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_message}")

# Main function to take input from the user
if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext to be decrypted: ")
    brute_force_caesar(ciphertext)
