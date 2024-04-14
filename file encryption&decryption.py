from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename):
    with open(filename, 'rb') as f:
        return f.read()

def encrypt_file(key, filename, output_filename=None):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(filename, 'rb') as f:
        data = pad(f.read(), AES.block_size)
    encrypted_data = cipher.iv + cipher.encrypt(data)
    if output_filename:
        with open(output_filename, 'wb') as f:
            f.write(encrypted_data)
    else:
        with open(filename, 'wb') as f:
            f.write(encrypted_data)

def decrypt_file(key, filename, output_filename=None):
    with open(filename, 'rb') as f:
        iv = f.read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(f.read()), AES.block_size)
    if output_filename:
        with open(output_filename, 'wb') as f:
            f.write(decrypted_data)
    else:
        with open(filename, 'wb') as f:
            f.write(decrypted_data)

if __name__ == "__main__":

    key = generate_key()
    save_key(key, 'key.txt')

    key = load_key('key.txt')

    
    encrypt_file(key, 'plaintext.txt', 'encrypted.txt')
    decrypt_file(key, 'encrypted.txt', 'decrypted.txt')
