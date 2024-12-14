import hashlib

def encrypt_message(message):

    sha256 = hashlib.sha256()    
    sha256.update(message.encode('utf-8'))
    encrypted_message = sha256.hexdigest()
    return encrypted_message


def main():

    message = input("Enter the message to encrypt: ")
    encrypted_message = encrypt_message(message)
    print(f"Encrypted message (SHA-256): {encrypted_message}")


if __name__ == "__main__":
    main()
