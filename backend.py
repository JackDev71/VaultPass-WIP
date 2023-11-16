import json
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass
from pathlib import Path

# Function to hash the password using a salt and multiple iterations
def hash_password(password, salt, iterations):
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations)
    return hashed_password

# Function to encrypt the data using AES-256 in CBC mode
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Function to decrypt the data
def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode()

# Function to save passwords to a file
def save_passwords(passwords, filename, key):
    encrypted_passwords = encrypt_data(json.dumps(passwords), key)
    with open(filename, "wb") as file:
        file.write(encrypted_passwords)

# Function to load passwords from a file
def load_passwords(filename, key):
    with open(filename, "rb") as file:
        encrypted_passwords = file.read()
    decrypted_passwords = decrypt_data(encrypted_passwords, key)
    passwords = json.loads(decrypted_passwords)
    return passwords

# Function to generate a secure encryption key
def generate_encryption_key():
    key = Fernet.generate_key()
    return key

# Function to get a secure master password from the user
def get_master_password():
    while True:
        password = getpass("Enter your master password: ")
        confirm_password = getpass("Confirm your master password: ")
        if password == confirm_password:
            return password
        else:
            print("Passwords do not match. Please try again.")

# Function to derive a secure encryption key from the master password
def derive_encryption_key(master_password, salt, iterations):
    key = hashlib.pbkdf2_hmac('sha256', master_password.encode(), salt, iterations)
    return key

# Example usage
passwords = {
    "website1": {
        "username": "user1",
        "password": "password1"
    },
    "website2": {
        "username": "user2",
        "password": "password2"
    }
}

filename = "E:\Development Work\Cyber Security\Password Manager\passwords.dat"
salt = b'somesalt'  # Add your own salt value
iterations = 100000  # Choose a suitable number of iterations

# Generate or derive the encryption key
master_password = get_master_password()
encryption_key = derive_encryption_key(master_password, salt, iterations)

# Save passwords to a file
save_passwords(passwords, filename, encryption_key)

# Load passwords from a file
loaded_passwords = load_passwords(filename, encryption_key)

# Print the loaded passwords
print(loaded_passwords)
