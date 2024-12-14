from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


def encrypt_message(key, message):
    iv = os.urandom(16)

   
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()
    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()
    return iv + encrypted_message


def main():
    
    message = input("Enter the message to encrypt: ")
    key = os.urandom(16)
    encrypted_message = encrypt_message(key, message)
    print(f"Encrypted message (ciphertext): {encrypted_message.hex()}")


if __name__ == "__main__":
    main()
