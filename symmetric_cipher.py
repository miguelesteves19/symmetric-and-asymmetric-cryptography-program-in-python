from cryptography.fernet import Fernet

def generate_symmetric_key():
    return Fernet.generate_key()

def symmetric_encrypt(data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

def symmetric_decrypt(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data
