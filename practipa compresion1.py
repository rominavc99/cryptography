from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key","wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    enconded_message = message.enconde()
    f = Fernet(key)
    encrypted_message = f.encrypt(enconded_message)

    print(encrypted_message)

if __name__ = "__main__":
    encrypt_message("CHINGAS A TU MADRE MEMO")