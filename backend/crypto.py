import base64
import hashlib
from cryptography.fernet import Fernet

def key_to_fernet(key_bits):
    key_str = "".join(map(str, key_bits))
    hashed = hashlib.sha256(key_str.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

def encrypt(message, key_bits):
    key = key_to_fernet(key_bits)
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

def decrypt(token, key_bits):
    key = key_to_fernet(key_bits)
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()