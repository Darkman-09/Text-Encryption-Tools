# aes_encryption.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    pad_len = 16 - len(text) % 16
    return text + chr(pad_len) * pad_len

def unpad(text):
    return text[:-ord(text[-1])]

def aes_encrypt(plain_text, key):
    key = key.ljust(32)[:32].encode()
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(plain_text).encode())
    return base64.b64encode(iv + encrypted).decode()

def aes_decrypt(cipher_text, key):
    raw = base64.b64decode(cipher_text)
    key = key.ljust(32)[:32].encode()
    iv = raw[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(raw[16:])
    return unpad(decrypted.decode())
