# rsa_encryption.py
import rsa
import base64

(public_key, private_key) = rsa.newkeys(512)

def rsa_encrypt(plain_text):
    encrypted = rsa.encrypt(plain_text.encode(), public_key)
    return base64.b64encode(encrypted).decode()

def rsa_decrypt(cipher_text):
    decrypted = rsa.decrypt(base64.b64decode(cipher_text), private_key)
    return decrypted.decode()
