from cryptography.fernet import Fernet
import os

SECRET_KEY_PATH = "encryption_key.key"

if not os.path.exists(SECRET_KEY_PATH):
    with open(SECRET_KEY_PATH, "wb") as key_file:
        key_file.write(Fernet.generate_key())

with open(SECRET_KEY_PATH, "rb") as key_file:
    SECRET_KEY = key_file.read()

cipher_suite = Fernet(SECRET_KEY)

def encrypt_data(data):
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt_data(data):
    return cipher_suite.decrypt(data.encode()).decode()