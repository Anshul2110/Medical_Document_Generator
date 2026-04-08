# import hashlib

# def anonymize_patient(name: str) -> str:
#     return hashlib.sha256(name.encode()).hexdigest()[:12]

# Generate a key (store this securely!)

from cryptography.fernet import Fernet
import base64

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_name(name: str) -> str:
    return cipher.encrypt(name.encode()).decode()

def decrypt_name(encrypted_name: str) -> str:
    return cipher.decrypt(encrypted_name.encode()).decode()