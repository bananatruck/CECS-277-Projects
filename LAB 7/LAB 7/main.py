# CECS 277
# Keshav Jindal
# Lab 1 - 15

from atbash import AtbashCipher
from caesar_cipher import CaesarCipher

# Main function to initiate the program
def main():
    # Prompting the user to choose between encryption or decryption
    choice = input("Secret Decoder Ring:\n1. Encrypt\n2. Decrypt\n")
    # Handling user's choice
    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    else:
        print("Invalid choice.")  # Handling invalid input

# Function to handle encryption process
def encrypt():
    # Prompting user to choose encryption type
    cipher_type = input("Enter encryption type:\n1. Atbash\n2. Caesar\n")
    # Getting message from the user
    message = input("Enter message: ")
    # Handling encryption type chosen by the user
    if cipher_type == "1":
        cipher = AtbashCipher()  \
    elif cipher_type == "2":
        shift = int(input("Enter shift value: "))  # Getting shift value from the user
        cipher = CaesarCipher(shift)  # Creating CaesarCipher object with specified shift
    else:
        print("Invalid encryption type.")  # Handling invalid encryption type
        return
    # Encrypting the message
    encrypted_message = cipher.encrypt_message(message)
    with open("message.txt", "w") as file:
        file.write(encrypted_message)
    # Confirming the encryption and saving message to a file
    print('Encrypted message saved to "message.txt".')

# Function to handle decryption process
def decrypt():
    # Prompting user to choose decryption type
    cipher_type = input("Enter decryption type:\n1. Atbash\n2. Caesar\n")
    # Handling decryption type chosen by the user
    if cipher_type == "1":
        cipher = AtbashCipher()  # Creating AtbashCipher object
    elif cipher_type == "2":
        shift = int(input("Enter shift value: "))  # Getting shift value from the user
        cipher = CaesarCipher(shift)  # Creating CaesarCipher object with specified shift
    else:
        print("Invalid decryption type.")  # Handling invalid decryption type
        return
    # Reading encrypted message from a file
    with open("message.txt", "r") as file:
        encrypted_message = file.read()
    # Decrypting the message
    decrypted_message = cipher.decrypt_message(encrypted_message)
    # Displaying decrypted message
    print(f"Decrypted message: {decrypted_message}")

# Ensuring the main function is called when the script is executed
if __name__ == "__main__":
    main()
