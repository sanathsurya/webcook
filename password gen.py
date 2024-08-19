import random
import string
import pyperclip
import os
from cryptography.fernet import Fernet

# Function to generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Function to encrypt data
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Function to decrypt data
def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

# Function to generate a strong password
def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")

    return ''.join(random.choice(characters) for _ in range(length))

# Function to save password securely
def save_password(password):
    key_file = 'encryption_key.key'
    if os.path.exists(key_file):
        with open(key_file, 'rb') as key_file:
            key = key_file.read()
    else:
        key = generate_key()
        with open(key_file, 'wb') as key_file:
            key_file.write(key)

    encrypted_password = encrypt_data(password, key)
    with open('passwords.txt', 'ab') as password_file:
        password_file.write(encrypted_password + b'\n')

# Main function to interact with the user
def main():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
    
    print(f"Generated Password: {password}")

    # Copy to clipboard
    copy_to_clipboard = input("Do you want to copy the password to clipboard? (y/n): ").strip().lower()
    if copy_to_clipboard == 'y':
        pyperclip.copy(password)
        print("Password copied to clipboard.")

    # Save securely
    save_password_option = input("Do you want to save this password securely? (y/n): ").strip().lower()
    if save_password_option == 'y':
        save_password(password)
        print("Password saved securely.")
        
    print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()
