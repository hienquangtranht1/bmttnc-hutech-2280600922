def encrypt_message(key, message):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import os

    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad

    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

def generate_aes_key():
    from Crypto.Random import get_random_bytes
    return get_random_bytes(32)  # AES-256 key size

def generate_rsa_key_pair():
    from Crypto.PublicKey import RSA
    return RSA.generate(2048)